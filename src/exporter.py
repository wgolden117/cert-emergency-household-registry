import csv
import os
from datetime import datetime

OUTPUT_DIR = "output"

EXPORT_FIELDS = [
    "id", "adults", "children", "pets", "dogs",
    "critical_meds", "meds_need_refrigeration", "special_needs",
    "propane_tank", "natural_gas", "address", "phone", "email",
    "medical_training", "knows_neighbors", "has_spare_key",
    "wants_newsletter", "allow_contact_non_disaster",
    "created_at", "updated_at"
]


def export_records(db_manager):
    """Export all records from the database into a timestamped CSV file."""
    print("\n=== Export Records ===")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    filename = f"Exported Records {timestamp}.csv"
    filepath = os.path.join(OUTPUT_DIR, filename)

    try:
        records = db_manager.fetch_all_records()

        with open(filepath, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(EXPORT_FIELDS)  # header row

            for row in records:
                writer.writerow(row)

        print(f"\n✔ Records successfully exported to:\n{filepath}\n")

    except Exception as e:
        print(f"\n✘ Error exporting records: {e}\n")
