import os
from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv

load_dotenv()
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

app = Flask(__name__)

def notify(image_path):
    message = client.messages \
        .create(
        body="Threat Detected. Should lockdown be initiated?",
        media_url = image_path,
        from_  = '+12056289601',
        to = '+16783926866'
    )
@app.route("/sms", methods=["GET", "POST"])
def receive_sms():
    resp = MessagingResponse()
    inbound_message = request.form.get("Body")
    if inbound_message == "Yes" or "yes" or "y":
        resp.message("Lockdown initiated")
    elif inbound_message == "No" or "no" or "n":
        resp.message("Lockdown canceled")
    else:
        resp.message("Please enter an accepted command")
    return str(resp)









