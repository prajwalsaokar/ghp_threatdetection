import os
from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from dotenv import load_dotenv
import rpi
from flask_ngrok import run_with_ngrok


load_dotenv()


account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

app = Flask(__name__)
run_with_ngrok(app)

def notify(image_path):
    message = client.messages \
        .create(
        body="Threat Detected. Should lockdown be initiated?",
        media_url = [image_path],
        from_  = '+12056289601',
        to = '+14705899932'
    )
@app.route("/sms", methods=["GET", "POST"])
def receive_sms():
    resp = MessagingResponse()
    inbound_message = request.form.get("Body")
    if inbound_message == "Yes" or "yes" or "y" or "lockdown":
        resp.message("Lockdown initiated")
        rpi.lockdown()
    elif inbound_message == "No" or "no" or "n" or "unlock":
        resp.message("Lockdown canceled")
        rpi.unlock()
    else:
        resp.message("Please enter an accepted command")
    return str(resp)

if __name__ == "__main__":
  app.run()






