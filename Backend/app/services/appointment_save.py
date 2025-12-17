from app.services.db import get_connection

def save_booking(vehicle_id, date, time):
    conn = get_connection()
    conn.execute(
        "INSERT INTO appointments (vehicle_id, date, time, status) VALUES (?, ?, ?, ?)",
        (vehicle_id, date, time, "BOOKED")
    )
    conn.commit()



print("done")