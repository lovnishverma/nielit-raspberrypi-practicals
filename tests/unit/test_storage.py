import sqlite3
import os
from nielit_rpi.storage import SensorDataLogger

def test_sensor_data_logger(tmp_db):
    logger = SensorDataLogger(tmp_db, "sensors")
    logger.create_table({"temperature": "REAL", "humidity": "REAL"})
    
    # Verify table creation
    conn = sqlite3.connect(tmp_db)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='sensors'")
    assert cursor.fetchone() is not None
    conn.close()
    
    try:
        logger.log_reading(temperature=25.5, humidity=60.0)
        logger.log_reading(temperature=26.0, humidity=58.0)
    finally:
        logger.close()
