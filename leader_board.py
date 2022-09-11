import time
import os
import requests


class LeaderBoard:

    def __init__(self):
        self.current_rid = ""
        self.current_rid_list = ""
        self.current_uid = ""
        self.current_sign = ""
        self.current_user = ""

    def handle_macro(self, response_json, request_json):
        #os.system("clear")
        try:
            response = requests.post(
                "http://gopa.koonek.net/public/api/statement",
                 json=response_json
            )
            print(response.json())
        except Exception as error: 
            print(error)
