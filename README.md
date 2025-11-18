# CERT Emergency Household Registry  
A Python command-line application designed to help Community Emergency Response Teams (CERT) collect, store, and manage household emergency preparedness information.  
This initial prototype supports storing household data, editing records, importing and exporting CSV files, and managing a local SQLite database.

---

## Project Purpose

This project was developed for Arizona State University's SER416 Final Project (Phase 1 – Prototype).  

The goal is to provide CERT volunteers with a local, reliable, and easy-to-use tool for collecting household preparedness data in emergencies where internet access may be unavailable.  

This information helps CERT teams quickly identify:
- At-risk individuals (elderly, disabled, special needs)
- Homes with critical medical dependencies
- Households with potential hazards (e.g., large propane tanks)
- Useful resources (e.g., medically trained individuals)

---

## Features Implemented

### Core Functionality
- Command-line interface (no GUI)
- Local SQLite database for persistent household records
- Full create / read / update / delete (CRUD) support:
  - Add new records  
  - View all records  
  - Edit any existing record  
  - Delete records with confirmation  

### Data Management
- Import records from CSV
  - Validates numeric, yes/no, phone, and email fields  
  - Supports optional fields  
  - Skips invalid rows with error messages  
  - A sample import file is included: sample_import.csv

- Export records to timestamped CSV
  - Files saved to `/output/`
  - Includes full field set and timestamps  
  - Automatically generates filenames like:  
    `Exported Records 2025-11-18 14-37-33.csv`  

### User-Friendly Enhancements
- Clean, user-facing numbering of records (1, 2, 3… regardless of SQLite ID gaps)  
- Automatic handling of optional values (blank allowed)  
- Address format validation for manual entry  
- Modular, scalable project structure (future web version ready)

---

## Requirements

- Python 3.10+ 
- No external dependencies  
  (uses only built-in modules including `sqlite3`, `csv`, `os`, `datetime`, and `re`)

---

## How to Run

From the root project directory:

```bash
python src/main.py
```
The main menu will open:

===== CERT Household Registry =====
1. View Records
2. Add New Record
3. Import Records
4. Export Records
5. Quit

## Validation Rules

Required fields
- Integer counts (adults, children)
- Yes/No fields (pets, dogs, critical meds, etc.)
- Address in format:
```
  7001 E Williams Field Rd, Mesa, AZ 85212
```
Optional fields, all validated only if provided.
- Phone
- Email
- Medical training
- Newsletter preference 

## Future Enhancements (Beyond Phase 1)
- Web-based interface (Phase 2)
- User authentication and access control
- Cloud-based storage
- Integration with CERT dispatch systems
- Geolocation mapping of households
