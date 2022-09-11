import json

import requests


def makerequest(url, data):
    try:
        response = requests.post(
            url=url,
            json=json.loads(data),
            headers={
                "accept": "application/json",
                "content-type": "application/json"
            }
        )
        if response.status_code == 500:
            return False
        else:
            print(response.text)
            return True
    except json.JSONDecodeError as e:
        print("invalid json data: ", e)
        return False



