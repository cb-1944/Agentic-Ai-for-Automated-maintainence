import json
from datetime import datetime
from langchain_core.prompts import PromptTemplate
from twilio.rest import Client
import os 
from dotenv import load_dotenv
load_dotenv()
from langchain_ollama import OllamaLLM

from app.services.appointment_save import save_booking
from twilio.rest import Client


# Twilio credentials
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FROM_WHATSAPP_NUMBER = os.getenv("FROM_WHATSAPP_NUMBER")

client = Client(ACCOUNT_SID, AUTH_TOKEN)


# -------- LLM SETUP --------
llm = OllamaLLM(
   model = "gpt-oss:120b-cloud" , 
   base_url="http://localhost:11434",
   temperature = 0,  
)

# -------- PROMPT --------
prompt = PromptTemplate(
    input_variables=["text"],
    template="""
You are a date-time extraction system.

Extract the date and time from the message below.

Rules:
- Output ONLY valid JSON
- Do NOT include explanation
- Do NOT include markdown
- Do NOT include text

Return EXACTLY this format:
{{
  "date": "YYYY-MM-DD",
  "time": "HH:MM"
}}

Message: {text}
"""
)


# -------- SAFE PARSER --------
def parse_llm_json(raw: str) -> dict:
    raw = raw.strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON from LLM: {raw}")


# -------- MAIN FUNCTION --------
def extract_datetime_and_store(text: str, vehicle_id: str) -> dict:
    """
    Extracts date & time from user message,
    stores appointment in DB,
    returns booking info.
    """

    # 1. Run LLM
    response = llm.invoke(prompt.format(text=text))

    # 2. Parse JSON safely
    parsed = parse_llm_json(response)

    date = parsed["date"]
    time = parsed["time"]

    # 3. Persist booking
    save_booking(
        vehicle_id=vehicle_id,
        date=date,
        time=time,
       
    )
   


 
    message = client.messages.create(
    from_= FROM_WHATSAPP_NUMBER ,
    content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
    
    content_variables = json.dumps({
    "1": date, 
    "2": time
    
}),
    to='whatsapp:+919665070980'
     )
 


    # 4. Return response
    # 
    return {
        "vehicle_id": vehicle_id,
        "date": date,
        "time": time,
        "status": "BOOKED"
    }

 
