from app.services.whatsapp_service import send_vehicle_alert






def engage_customer(telemetry, diagnosis):
    send_vehicle_alert(
        phone=telemetry["phone"],
        vehicle_id=telemetry["vehicle_id"],
        diagnosis=diagnosis,
       
    )
    return "WHATSAPP_SENT"
