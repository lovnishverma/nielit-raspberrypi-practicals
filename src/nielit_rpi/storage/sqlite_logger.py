import sqlite3
import logging
import datetime
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)

class SensorDataLogger:
    """
    A logger that saves sensor readings into an SQLite database.
    """
    
    def __init__(self, db_path: str = 'sensor_data.db', table_name: str = 'readings'):
        """
        Initialize the SQLite logger.
        
        Args:
            db_path (str): Path to the SQLite database file.
            table_name (str): Name of the table to store data in.
        """
        self.db_path = db_path
        self.table_name = table_name
        logger.info(f"Initializing SensorDataLogger (DB: {db_path}, Table: {table_name})")
        
        self.conn = sqlite3.connect(self.db_path)
        # Configure connection to return rows as dictionaries
        self.conn.row_factory = sqlite3.Row
        
    def create_table(self, columns: Dict[str, str]) -> None:
        """
        Create the table if it does not exist.
        
        Args:
            columns (Dict[str, str]): Dictionary of column names and their SQLite types
                                      (e.g., {'temperature': 'REAL', 'humidity': 'REAL'})
        """
        # Always add an auto-incrementing ID and a timestamp
        col_defs = ["id INTEGER PRIMARY KEY AUTOINCREMENT", 
                    "timestamp DATETIME DEFAULT CURRENT_TIMESTAMP"]
                    
        for col_name, col_type in columns.items():
            col_defs.append(f"{col_name} {col_type}")
            
        columns_sql = ", ".join(col_defs)
        query = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({columns_sql})"
        
        logger.debug(f"Creating table with query: {query}")
        cursor = self.conn.cursor()
        cursor.execute(query)
        self.conn.commit()

    def execute_query(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """
        Execute a raw SQL query with optional parameters.

        Args:
            query (str): SQL query string.
            params (tuple): Parameters for query substitution.

        Returns:
            sqlite3.Cursor: Executed cursor.
        """
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor
        
    def log_reading(self, **kwargs) -> None:
        """
        Insert a new sensor reading into the table.
        
        Args:
            **kwargs: Column names and their corresponding values.
        """
        if not kwargs:
            return
            
        columns = ", ".join(kwargs.keys())
        placeholders = ", ".join(["?"] * len(kwargs))
        values = tuple(kwargs.values())
        
        query = f"INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})"
        
        logger.debug(f"Inserting data: {kwargs}")
        cursor = self.conn.cursor()
        cursor.execute(query, values)
        self.conn.commit()
        
    def get_readings(self, limit: int = 100) -> List[Dict[str, Any]]:
        """
        Retrieve the most recent readings.
        
        Args:
            limit (int): Maximum number of rows to return.
            
        Returns:
            List[Dict]: A list of dictionaries representing the rows.
        """
        query = f"SELECT * FROM {self.table_name} ORDER BY timestamp DESC LIMIT ?"
        cursor = self.conn.cursor()
        cursor.execute(query, (limit,))
        
        return [dict(row) for row in cursor.fetchall()]
        
    def get_latest(self) -> Optional[Dict[str, Any]]:
        """
        Retrieve the single most recent reading.
        
        Returns:
            Dict or None: A dictionary representing the latest row, or None if empty.
        """
        readings = self.get_readings(limit=1)
        return readings[0] if readings else None
        
    def close(self) -> None:
        """Close the database connection."""
        if hasattr(self, 'conn') and self.conn:
            logger.info("Closing database connection")
            self.conn.close()
            
    def __enter__(self):
        return self
        
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
