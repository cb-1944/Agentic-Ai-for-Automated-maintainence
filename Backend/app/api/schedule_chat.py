from fastapi import APIRouter
from app.agents.schedule import extract_datetime_and_store


router = APIRouter()

@router.post("/chat/schedule")
def schedule_chat(data: dict):
    user_text = data["message"]
    vehicle_id = data["vehicle_id"]

    booking = extract_datetime_and_store(user_text, vehicle_id)

    return {
        "reply": f"✅ Service scheduled on {booking['date']} at {booking['time']}"
    }
