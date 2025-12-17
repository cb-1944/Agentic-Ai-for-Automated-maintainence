from fastapi import APIRouter, Request
from app.agents.schedule import schedule_service

router = APIRouter()

@router.post("/whatsapp/webhook")
async def whatsapp_webhook(request: Request):
    data = await request.json()
    reply = data.get("ButtonText")
    phone = data.get("From")

    if reply == "YES":
        result = schedule_service(phone)
        return {"status": result}

    return {"status": "NO_ACTION"}
