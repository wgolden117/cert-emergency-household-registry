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

        # ----- Required -----
        adults = self.prompt_new_required("Number of adults: ", validate_integer)
        children = self.prompt_new_required("Number of children: ", validate_integer)

        pets = self.prompt_new_required("Are there pets? (yes/no): ", validate_yes_no)
        dogs = None
        if pets == "yes":
            dogs = self.prompt_new_required("Are there any dogs? (yes/no): ", validate_yes_no)

        critical_meds = self.prompt_new_required("Does anyone require critical medications? (yes/no): ",
                                                 validate_yes_no)
        meds_need_refrigeration = None
        if critical_meds == "yes":
            meds_need_refrigeration = self.prompt_new_required(
                "Do those medications need refrigeration? (yes/no): ",
                validate_yes_no
            )

        special_needs = self.prompt_new_required("Any special needs requiring evacuation help? (yes/no): ",
                                                 validate_yes_no)
        propane_tank = self.prompt_new_required("Large propane tank? (yes/no): ", validate_yes_no)
        natural_gas = self.prompt_new_required("Natural gas connection? (yes/no): ", validate_yes_no)

        address = self.prompt_new_required("Enter the household address: ", validate_address)

        # ----- Optional -----
        phone = self.prompt_new_optional("Contact phone (optional): ", validate_phone)
        email = self.prompt_new_optional("Contact email (optional): ", validate_email)
        medical_training = self.prompt_new_optional("Anyone with medical training? (yes/no): ", validate_yes_no)
        knows_neighbors = self.prompt_new_optional("Do they know their neighbors? (yes/no): ", validate_yes_no)
        has_spare_key = self.prompt_new_optional("Do they have a neighbor's spare key? (yes/no): ", validate_yes_no)
        wants_newsletter = self.prompt_new_optional("Receive CERT newsletter? (yes/no): ", validate_yes_no)
        allow_contact_non_disaster = self.prompt_new_optional(
            "Allow CERT to use contact info for non-disaster purposes? (yes/no): ",
            validate_yes_no
        )

        # ----- Build dict -----
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

    def edit_record(self, record):
        print("\n=== Edit Household Record ===")

        # record is a tuple, so convert to dict with fieldnames
        fields = [
            "id", "adults", "children", "pets", "dogs",
            "critical_meds", "meds_need_refrigeration", "special_needs",
            "propane_tank", "natural_gas", "address", "phone", "email",
            "medical_training", "knows_neighbors", "has_spare_key",
            "wants_newsletter", "allow_contact_non_disaster",
            "created_at", "updated_at"
        ]

        record_dict = {field: value for field, value in zip(fields, record)}

        print("\nPress Enter to keep current value.\n")

        # ---- REQUIRED FIELDS ----
        record_dict["adults"] = self.prompt_edit("Adults", record_dict["adults"], validate_integer)
        record_dict["children"] = self.prompt_edit("Children", record_dict["children"], validate_integer)

        record_dict["pets"] = self.prompt_edit("Pets (yes/no)", record_dict["pets"], validate_yes_no)

        # follow-up dogs
        if record_dict["pets"] == "yes":
            record_dict["dogs"] = self.prompt_edit("Dogs (yes/no)", record_dict["dogs"], validate_yes_no)
        else:
            record_dict["dogs"] = None

        record_dict["critical_meds"] = self.prompt_edit("Critical Meds (yes/no)", record_dict["critical_meds"],
                                                        validate_yes_no)

        if record_dict["critical_meds"] == "yes":
            record_dict["meds_need_refrigeration"] = self.prompt_edit(
                "Meds Need Refrigeration (yes/no)",
                record_dict["meds_need_refrigeration"],
                validate_yes_no
            )
        else:
            record_dict["meds_need_refrigeration"] = None

        record_dict["special_needs"] = self.prompt_edit("Special Needs (yes/no)", record_dict["special_needs"],
                                                        validate_yes_no)
        record_dict["propane_tank"] = self.prompt_edit("Propane Tank (yes/no)", record_dict["propane_tank"],
                                                       validate_yes_no)
        record_dict["natural_gas"] = self.prompt_edit("Natural Gas (yes/no)", record_dict["natural_gas"],
                                                      validate_yes_no)

        record_dict["address"] = self.prompt_edit("Address", record_dict["address"], validate_address)

        # ---- OPTIONAL FIELDS ----
        record_dict["phone"] = self.prompt_edit("Phone", record_dict["phone"], validate_phone, optional=True)
        record_dict["email"] = self.prompt_edit("Email", record_dict["email"], validate_email, optional=True)
        record_dict["medical_training"] = self.prompt_edit("Medical Training", record_dict["medical_training"],
                                                           validate_yes_no, optional=True)
        record_dict["knows_neighbors"] = self.prompt_edit("Knows Neighbors", record_dict["knows_neighbors"],
                                                          validate_yes_no, optional=True)
        record_dict["has_spare_key"] = self.prompt_edit("Has Spare Key", record_dict["has_spare_key"], validate_yes_no,
                                                        optional=True)
        record_dict["wants_newsletter"] = self.prompt_edit("Wants Newsletter", record_dict["wants_newsletter"],
                                                           validate_yes_no, optional=True)
        record_dict["allow_contact_non_disaster"] = self.prompt_edit("Allow Contact Non-Disaster",
                                                                     record_dict["allow_contact_non_disaster"],
                                                                     validate_yes_no, optional=True)

        # Remove id + metadata — DB handles timestamps
        updated_data = {k: v for k, v in record_dict.items() if k not in ("id", "created_at", "updated_at")}

        self.db.update_record(record_dict["id"], updated_data)
        print("\n✔ Record updated successfully!\n")

    def prompt_new_required(self, prompt, validator):
        while True:
            value = input(prompt).strip()
            try:
                return validator(value)
            except ValueError as e:
                print(e)

    def prompt_new_optional(self, prompt, validator):
        while True:
            value = input(prompt).strip()
            if value == "":
                return None
            try:
                return validator(value, optional=True)
            except ValueError as e:
                print(e)

    def prompt_edit(self, label, current_value, validator, optional=False):
        prompt = f"{label} [{current_value}]: "
        value = input(prompt).strip()

        if value == "":
            return current_value

        try:
            return validator(value, optional=optional) if optional else validator(value)
        except ValueError as e:
            print(e)
            return current_value

