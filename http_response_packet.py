import base64
import json
import subprocess
from base64 import b64encode

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


class JsonResponsePacket:

    def __init__(self, packet):
        self.payload = packet['payload']
        self.path = packet['path']

    def _normalize_json(self):
        return self.payload.replace('\\\\"', "") \
            .replace('\\"', '"') \
            .replace('}",', "},") \
            .replace('}",', "}',") \
            .replace('""', "") \
            .replace(":,", '"",') \
            .replace("\\", "") \
            .replace('"""', ':""') \
            .replace('"{', "'{") \
            .replace('l":\'', 'l":\"') \
            .replace('l":"', 'l":') \
            .replace("http", '"http') \
            .replace('deal":g', 'deal:{g')\
            .replace('""', '":"')\
            .replace('mgu:"', 'mgu":"')\
            .replace(',"is_select', ',"is_select')\
            .replace('","name"', '","name"')\

    def data(self):
        return self._normalize_json()

    def json(self):
        return base64.b64decode(self.payload).decode("utf-8")
        # return json.loads(self.data())
