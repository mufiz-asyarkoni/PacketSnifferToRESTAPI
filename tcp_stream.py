from scapy.compat import raw, bytes_base64, bytes_encode
from scapy.layers.http import HTTPRequest, HTTPResponse
import scapy.all as scapy
from scapy.layers.inet import IP, TCP
from scapy.sessions import TCPSession
from lib.http_response_packet import JsonResponsePacket


class TcpStream:

    def __init__(self, iface, request_map, callback):
        self.sniffer = None
        self.iface = iface
        self.request_map = request_map
        self.callback = callback
        self.request_list = []
        self.request_ip = ""
        self.response_ip = ""
        self.current_url = ""

    def get_in_session(self):
        return self.current_url != "" and self.request_ip != "" and self.request_ip != ""

    def _set_session(self, uri="", reqip="", resip=""):
        self.current_url = uri
        self.request_ip = reqip
        self.response_ip = resip

    def _http_request(self, packet):
        if self.get_in_session() == 0:
            ip = packet[IP]
            http = packet[HTTPRequest]
            uri = http.Path.decode()
            if packet.haslayer(HTTPRequest):
                for key in self.request_map:
                    key_value = self.request_map[key]
                    if key_value == uri:
                        self._set_session(uri=uri, reqip=ip, resip=ip.dst)

    def on_http_respnse(self, packet):
        in_session = self.get_in_session()
        http = packet[HTTPResponse]
        if in_session:
            is_json = "application/json" in http.Content_Type.decode()
            if is_json:
                self.callback(JsonResponsePacket(packet={
                    'path': self.current_url,
                    'payload': bytes_base64(packet[HTTPResponse].payload).decode("utf-8")
                }))
                self._set_session()



    def start_snif(self):
        print("start sniff on:", self.iface)
        self.sniffer = scapy.sniff(
            session=TCPSession(),
            prn=self.on_packet,
            iface='wlp3s0',
            store=False,
            filter='tcp'
        )


def http_stream_listener(iface, request_map, callback):
    streamer = TcpStream(iface=iface, request_map=request_map, callback=callback)
    streamer.start_snif()
