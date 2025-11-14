from database_manager import DatabaseManager

def main():
    print("Testing database setup...")
    db = DatabaseManager()
    print("Database initialized! ✔")
    db.close()

if __name__ == "__main__":
    main()
