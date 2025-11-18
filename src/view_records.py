class ViewRecordsManager:
    def __init__(self, db):
        self.db = db

    def display_records(self):
        print("\n=== View Household Records ===")

        records = self.db.fetch_all_records()

        if not records:
            print("\nNo records found.\n")
            return

        # Build a mapping: display index → real DB ID
        indexed_records = []
        print()

        for idx, record in enumerate(records, start=1):
            db_id = record[0]
            address = record[10]  # address column index
            indexed_records.append((idx, db_id))
            print(f"{idx}. {address}")

        print("\nPress Enter to return to the menu.")
        choice = input("Enter a record number to view details: ").strip()

        if choice == "":
            return

        if not choice.isdigit():
            print("\nInvalid input. Returning to menu.\n")
            return

        choice_num = int(choice)

        # Validate selection
        if not (1 <= choice_num <= len(indexed_records)):
            print("\nInvalid record number. Returning to menu.\n")
            return

        # Map display number → actual database ID
        _, record_id = indexed_records[choice_num - 1]

        record = self.db.fetch_record_by_id(record_id)

        if not record:
            print("\nRecord not found. Returning to menu.\n")
            return

        self.show_record_details(record)

    def show_record_details(self, record):
        print("\n===== Household Record Details =====")

        fields = [
            "ID", "Adults", "Children", "Pets", "Dogs",
            "Critical Meds", "Meds Need Refrigeration",
            "Special Needs", "Propane Tank", "Natural Gas",
            "Address", "Phone", "Email", "Medical Training",
            "Knows Neighbors", "Has Spare Key", "Wants Newsletter",
            "Allow Contact (Non-Disaster)",
            "Created At", "Updated At"
        ]

        for label, value in zip(fields, record):
            print(f"{label}: {value}")

        print("\nOptions:")
        print("1. Edit this record")
        print("2. Delete this record")
        print("Press Enter to return to the menu")

        choice = input("Select an option: ").strip()

        if choice == "1":
            from record_manager import RecordManager
            manager = RecordManager(self.db)
            manager.edit_record(record)

        elif choice == "2":
            # Confirm deletion
            confirm = input("Are you sure you want to delete this record? (yes/no): ").strip().lower()
            if confirm == "yes":
                self.db.delete_record(record[0])  # record[0] = ID
                print("\n✔ Record deleted successfully.\n")
                return
            else:
                print("\nDeletion cancelled.\n")
                return

        else:
            # Return to menu on Enter or invalid input
            return


