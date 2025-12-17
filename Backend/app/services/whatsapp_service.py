from twilio.rest import Client
import json
from dotenv import load_dotenv
import os


# Twilio credentials
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN ")
FROM_WHATSAPP_NUMBER = os.getenv("FROM_WHATSAPP_NUMBER ")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def send_vehicle_alert(phone, vehicle_id, diagnosis):

 

 message = client.messages.create(
  from_= FROM_WHATSAPP_NUMBER ,
  content_sid= os.getenv("content_sid"),
  content_variables='{"1":"localhost:3000/schedule"}',
  to=os.getenv("to")
)
 
 print(message.sid)