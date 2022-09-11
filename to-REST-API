from mitmproxy import http
import json
import requests

def handle_statement(response_json):
    try:
        response = requests.post("http://gopa.koonek.net/public/api/statement", json=response_json)
        if response.status_code == 200 or response.status_code == 201:
            print("")
            print("")
            print("-")
            print("")
            print("")

            print("NEW DESK STATEMENT DATA (GOPA SNIFFER)")
            dataResponse = json.dumps(response.json())
            print("--------------------------------------")

            #print(dataResponse)

            array = json.loads(dataResponse)

            print("")
            print("SERVER STATUS:")
            print("[ + ]", response.status_code, "-", response.url)

            print("")
            print("MESSAGE:")
            print("[ ? ] " + array["message"])

            print("")
            print("PROCESSED DESKS:")

            if array["message"] != "Desk Already Exist":
                for item in range(len(array["processed_desk"])):
                    print("[",item,"]", array["processed_desk"][item])

            if array["message"] == "Desk Already Exist":
                print("[ ! ] No Processed Desks because Statement Data Already Exist")

            print("")
            print("PROCESSED PLAYERS:")

            if array["message"] != "Desk Already Exist":
                for item in range(len(array["processed_players"])):
                   print("[",item,"]", array["processed_players"][item])
            
            if array["message"] == "Desk Already Exist":
                print("[ ! ] No Processed Players because Statement Data Already Exist")

            print("")
            print("NEW PLAYERS:")
            
            if array["message"] != "Desk Already Exist":
                if not array["new_players"]:
                    print("[ ! ] No New Players in this Statement Data")
                for item in range(len(array["new_players"])):
                    print("[",item,"]", array["new_players"][item])
            
            if array["message"] == "Desk Already Exist":
                print("[ ! ] No New Players because Statement Data Already Exist")

            print("")
            print("-------------------------")
            print("BLACKLISTED PLAYERS LIST:")

            if array["message"] != "Desk Already Exist":
                if not array["blacklist_players"]:
                    print("[ ! ] No Blacklisted Players in this Statement Data")
                for item in range(len(array["blacklist_players"])):
                    print("[",item,"]", array["blacklist_players"][item])
            
            if array["message"] == "Desk Already Exist":
                print("[ ! ] No Blacklisted Players because Statement Data Already Exist")
        else:
            print("server code :", response.status_code)
            print("server response", response.json())
    except Exception as error: 
        print(error)

def handle_players(response_json):
    try:
        response = requests.post("http://gopa.koonek.net/public/api/players",json=response_json)
        if response.status_code == 200 or response.status_code == 201:
            print("")
            print("-------------------------")            
            print(response.json())
        else:
            print("server code :", response.status_code)
            print("server response", response.json())
    except Exception as error: 
        print(error)

def handle_blacklist(response_json):
    try:
        response = requests.post("http://gopa.koonek.net/public/api/blacklist",json=response_json)
        if response.status_code == 200 or response.status_code == 201:
            print("")
            print("-------------------------")
            print(response.json())
        else:
            print("server code :", response.status_code)
            print("server response", response.json())
    except Exception as error: 
        print(error)


def response(flow: http.HTTPFlow):
    req_from = flow.request
    try:
        if req_from.path == "/apigame/getUnionRecord2":
            handle_statement(
                response_json=flow.response.json()
            )
        if req_from.path == "/apigame/getUserHead":
            handle_players(
                response_json=flow.response.json()
            )
        if req_from.path == "/apigame/getUserHead":
            handle_blacklist(
                response_json=flow.response.json()
            )
    except Exception as e:
        print(e)
