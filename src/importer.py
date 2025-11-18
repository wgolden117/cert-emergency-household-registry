import csv
import os
from validators import (
    validate_integer,
    validate_yes_no,
    validate_phone,
    validate_email
)

REQUIRED_HEADERS = [
    "adults", "children", "pets", "dogs",
    "critical_meds", "meds_need_refrigeration", "special_needs",
    "propane_tank", "natural_gas", "address", "phone", "email",
    "medical_training", "knows_neighbors", "has_spare_key",
    "wants_newsletter", "allow_contact_non_disaster"
]


def normalize(value):
    """Convert empty strings or 'None' to None, leave others as-is."""
    if value is None:
        return None
    v = value.strip()
    if v == "" or v.lower() == "none":
        return None
    return v


def import_records(db_manager):
    """Import records from a user-provided CSV file."""
    print("\n=== Import Records ===")
    path = input("Enter the CSV filename (or full path): ").strip()

    if not os.path.exists(path):
        print("\nError: File does not exist.\n")
        return

    success_count = 0
    fail_count = 0

    try:
        with open(path, "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            # Validate headers
            missing = [h for h in REQUIRED_HEADERS if h not in reader.fieldnames]
            if missing:
                print(f"\nCSV is missing required headers: {missing}\n")
                return

            for row in reader:
                try:
                    # Required: numeric & yes/no
                    adults = validate_integer(row["adults"])
                    children = validate_integer(row["children"])

                    pets = validate_yes_no(row["pets"])
                    dogs = normalize(row["dogs"]) if pets == "yes" else None

                    critical_meds = validate_yes_no(row["critical_meds"])
                    meds_need_refrigeration = (
                        normalize(row["meds_need_refrigeration"])
                        if critical_meds == "yes" else None
                    )

                    special_needs = validate_yes_no(row["special_needs"])
                    propane_tank = validate_yes_no(row["propane_tank"])
                    natural_gas = validate_yes_no(row["natural_gas"])

                    # Address: NO validation (Option B)
                    address = normalize(row["address"])

                    # Optional fields
                    phone = validate_phone(row["phone"], optional=True)
                    email = validate_email(row["email"], optional=True)
                    medical_training = validate_yes_no(normalize(row["medical_training"]), optional=True)
                    knows_neighbors = validate_yes_no(normalize(row["knows_neighbors"]), optional=True)
                    has_spare_key = validate_yes_no(normalize(row["has_spare_key"]), optional=True)
                    wants_newsletter = validate_yes_no(normalize(row["wants_newsletter"]), optional=True)
                    allow_contact_non_disaster = validate_yes_no(normalize(row["allow_contact_non_disaster"]),
                                                                 optional=True)
                    record_data = {
                        "adults": adults,
                        "children": children,
                        "pets": pets,
                        "dogs": dogs,
                        "critical_meds": critical_meds,
                        "meds_need_refrigeration": meds_need_refrigeration,
                        "special_needs": special_needs,
                        "propane_tank": propane_tank,
                        "natural_gas": natural_gas,
                        "address": address,
                        "phone": phone,
                        "email": email,
                        "medical_training": medical_training,
                        "knows_neighbors": knows_neighbors,
                        "has_spare_key": has_spare_key,
                        "wants_newsletter": wants_newsletter,
                        "allow_contact_non_disaster": allow_contact_non_disaster,
                    }

                    db_manager.insert_record(record_data)
                    success_count += 1

                except Exception as e:
                    print(f"Skipping row due to error: {e}")
                    fail_count += 1

        print(f"\nImport complete! Successfully imported: {success_count}")
        if fail_count > 0:
            print(f"Failed to import: {fail_count} rows\n")

    except Exception as e:
        print(f"\nError reading CSV: {e}\n")
