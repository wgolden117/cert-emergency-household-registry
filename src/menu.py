from database_manager import DatabaseManager
from record_manager import RecordManager


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
                self.import_records()
            elif choice == "4":
                self.export_records()
            elif choice == "5":
                print("Goodbye!")
                self.db.close()
                break
            else:
                print("Invalid choice. Please try again.")

    # ---- Placeholder methods for future features ---- #

    def view_records(self):
        print("\n[View Records] Feature not implemented yet.\n")

    def add_record(self):
        manager = RecordManager(self.db)
        manager.add_new_record()

    def import_records(self):
        print("\n[Import Records] Feature not implemented yet.\n")

    def export_records(self):
        print("\n[Export Records] Feature not implemented yet.\n")
