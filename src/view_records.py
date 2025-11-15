class ViewRecordsManager:
    def __init__(self, db):
        self.db = db

    def display_records(self):
        print("\n=== View Household Records ===")

        records = self.db.fetch_all_records()

        if not records:
            print("\nNo records found.\n")
            return

        # Display list of records by ID + address (to identify)
        for record in records:
            record_id = record[0]
            address = record[10]  # address column index
            print(f"{record_id}. {address}")

        print("\nPress Enter to return to the menu.")
        choice = input("Enter a record ID to view details: ").strip()

        if choice == "":
            return

        if not choice.isdigit():
            print("\nInvalid input. Returning to menu.\n")
            return

        record_id = int(choice)
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

        print("\nPress Enter to return to the menu.")
        input()
