from database_manager import DatabaseManager
from record_manager import RecordManager
from view_records import ViewRecordsManager
from exporter import export_records
from importer import import_records

class Menu:
    def __init__(self):
        self.db = DatabaseManager()

    def display(self):
        while True:
            print("\n===== CERT Household Registry =====")
            print("1. View Records")
            print("2. Add New Record")
            print("3. Import Records")
            print("4. Export Records")
            print("5. Quit")

            choice = input("\nSelect an option: ").strip()

            if choice == "1":
                self.view_records()
            elif choice == "2":
                self.add_record()
            elif choice == "3":
                import_records(self.db)
            elif choice == "4":
                export_records(self.db)
            elif choice == "5":
                print("Goodbye!")
                self.db.close()
                break
            else:
                print("Invalid choice. Please try again.")

    def view_records(self):
        manager = ViewRecordsManager(self.db)
        manager.display_records()

    def add_record(self):
        manager = RecordManager(self.db)
        manager.add_new_record()


