import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.join("database", "cert.db")

class DatabaseManager:
    def __init__(self):
        self.connection = sqlite3.connect(DB_PATH)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS household_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                -- Required fields
                adults INTEGER NOT NULL,
                children INTEGER NOT NULL,
                pets TEXT NOT NULL,                     -- 'yes' or 'no'
                dogs TEXT,                              -- 'yes' or 'no' or NULL
                critical_meds TEXT NOT NULL,            -- 'yes' or 'no'
                meds_need_refrigeration TEXT,           -- 'yes' or 'no' or NULL
                special_needs TEXT NOT NULL,            -- 'yes' or 'no'
                propane_tank TEXT NOT NULL,             -- 'yes' or 'no'
                natural_gas TEXT NOT NULL,              -- 'yes' or 'no'
                address TEXT NOT NULL,

                -- Optional fields
                phone TEXT,
                email TEXT,
                medical_training TEXT,
                knows_neighbors TEXT,
                has_spare_key TEXT,
                wants_newsletter TEXT,
                allow_contact_non_disaster TEXT,

                -- Metadata
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );
        """)

        self.connection.commit()

    def insert_record(self, record_data):
        """Insert a new household record into the DB."""
        record_data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        record_data["updated_at"] = record_data["created_at"]

        columns = ", ".join(record_data.keys())
        placeholders = ", ".join(["?"] * len(record_data))

        self.cursor.execute(f"""
            INSERT INTO household_records ({columns})
            VALUES ({placeholders})
        """, list(record_data.values()))

        self.connection.commit()

    def fetch_all_records(self):
        self.cursor.execute("SELECT * FROM household_records ORDER BY id")
        return self.cursor.fetchall()

    def fetch_record_by_id(self, record_id):
        self.cursor.execute("SELECT * FROM household_records WHERE id = ?", (record_id,))
        return self.cursor.fetchone()

    def update_record(self, record_id, updated_data):
        updated_data["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        assignments = ", ".join([f"{key} = ?" for key in updated_data.keys()])

        self.cursor.execute(f"""
            UPDATE household_records
            SET {assignments}
            WHERE id = ?
        """, list(updated_data.values()) + [record_id])

        self.connection.commit()

    def close(self):
        self.connection.close()
