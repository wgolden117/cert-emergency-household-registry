from validators import (
    validate_integer,
    validate_yes_no,
    validate_phone,
    validate_email,
    validate_address
)

class RecordManager:
    def __init__(self, db):
        self.db = db

    def add_new_record(self):
        print("\n=== Add New Household Record ===")

        # ----- Required Questions -----
        adults = validate_integer("Number of adults: ")
        children = validate_integer("Number of children: ")

        pets = validate_yes_no("Are there pets? (yes/no): ")
        dogs = None
        if pets == "yes":
            dogs = validate_yes_no("Are there any dogs? (yes/no): ")

        critical_meds = validate_yes_no("Does anyone require critical medications? (yes/no): ")
        meds_need_refrigeration = None
        if critical_meds == "yes":
            meds_need_refrigeration = validate_yes_no("Do those medications need refrigeration? (yes/no): ")

        special_needs = validate_yes_no("Any special needs requiring evacuation help? (yes/no): ")
        propane_tank = validate_yes_no("Large propane tank? (yes/no): ")
        natural_gas = validate_yes_no("Natural gas connection? (yes/no): ")

        address = validate_address("Enter the household address: ")

        # ----- Optional Questions -----
        phone = validate_phone("Contact phone (optional, press Enter to skip): ", optional=True)
        email = validate_email("Contact email (optional, press Enter to skip): ", optional=True)
        medical_training = validate_yes_no("Anyone with medical training? (yes/no, Enter to skip): ", optional=True)
        knows_neighbors = validate_yes_no("Do they know their neighbors? (yes/no, Enter to skip): ", optional=True)
        has_spare_key = validate_yes_no("Do they have a neighbor's spare key? (yes/no, Enter to skip): ", optional=True)
        wants_newsletter = validate_yes_no("Receive CERT newsletter? (yes/no, Enter to skip): ", optional=True)
        allow_contact_non_disaster = validate_yes_no(
            "Allow CERT to use contact info for non-disaster purposes? (yes/no, Enter to skip): ",
            optional=True
        )

        # ----- Build dictionary for database insertion -----
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
            "allow_contact_non_disaster": allow_contact_non_disaster
        }

        self.db.insert_record(record_data)
        print("\n✔ Record added successfully!\n")
