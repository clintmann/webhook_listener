
from flask import Flask, request, Response
import os
import requests
import json

room_ID = os.environ['ROOMID']
Token = os.environ['TOKEN']
app= Flask(__name__)

@app.route('/', methods=['GET'])
def mainPage ():
    return ('Webhook listener for Alerts')

@app.route('/alerts', methods=['POST'])
def receiveAlerts():
    data = request.json
    if not len(data) == 0:
        return(postAlerts(data))
    else: 
        return("Alert not posted")

def postAlerts(data):
    alert = json.dumps(data)
    url = "https://webexapis.com/v1/messages"
    room_id = room_ID
    token = Token
    headers = {'Content-Type': 'application/json',
               'Authorization': f'Bearer {token}'
    }

    payload = {'roomId': room_id,
               'text': alert
    }
    print(payload)
    response = requests.post(url,headers=headers, json=payload)
    print(response)
    return 'complete'

if __name__ == "__main__":
    app.run()
    
