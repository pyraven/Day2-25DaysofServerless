from datetime import datetime
import os
from twilio.rest import Client

account_sid = os.environ.get('SID')
auth_token = os.environ.get('TOKEN')
me = os.environ.get('MYNUMBER')
lucy = os.environ.get('LUCY')

def send_text(sms):
	client = Client(account_sid, auth_token)
	message = client.messages.create(body=sms,from_=me, to=lucy)
	print(message.sid)

def main(event=None, context=None):
    instructions = {
        "00": "start the coffee, set out 4 cups",
        "25": "pour two cups",
        "30": "light the candles",
        "35": "deliver the coffee to Mom and Dad",
        "39": "return to kitchen, fill two more cups",
        "40": "relight the candles",
        "45": "deliver the coffee to Sister and Brother",
        "49": "return to kitchen, take a break!"
    }
    minutes = str(datetime.now().strftime("%M"))
    if minutes in instructions:
        message = instructions[minutes]
        send_text(message)
    return "Reminder Sent."