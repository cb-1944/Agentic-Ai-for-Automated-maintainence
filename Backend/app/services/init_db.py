from app.services.db import get_connection

def init_db():
    conn = get_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_id TEXT,
            date TEXT,
            time TEXT,
            status TEXT
                 
                
        )
    """)
    conn.commit()
    print("table created")
init_db() ; 
