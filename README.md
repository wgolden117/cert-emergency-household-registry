# CERT Emergency Household Registry

A Python command-line application designed to help Community Emergency Response Teams (CERT) collect, store, and manage household emergency preparedness information. This initial prototype uses a local SQLite database and supports viewing, adding, editing, importing, and exporting household records.

---
## Project Purpose

This project was developed for Arizona State University as part of a disaster preparedness software prototype. 
It empowers CERT teams to quickly identify at-risk individuals and households during emergencies such as 
earthquakes, floods, and wildfires.

## Features

- Command-line interface (no GUI required)  
- Store household data in a local SQLite database  
- Add new household records with input validation  
- View and edit existing records  
- Import records from a CSV file  
- Export records to timestamped CSV files  
- Fully modular project structure for scalability  

---

## Requirements

- Python 3.10+  
- No external dependencies required (uses built-in libraries like `sqlite3`, `csv`, and `datetime`)

---

## How to Run

From the project root directory:

```bash
python src/main.py
````

This will launch the main menu:

1. View Records
2. Add New Record
3. Import Records
4. Export Records
5. Quit

## Exported CSV Files

All exported files will appear in:

/output/

Each export is named:
- Exported_Records_YYYY-MM-DD_HHMMSS.csv

## Importing CSV Files
To import records, provide the path to a properly formatted CSV file.
A sample file is included:

- sample_import.csv

## Future Enhancements (Phase 2 and beyond)
- Web-based interface (Flask or FastAPI)
- Centralized SQL or cloud database
- Authentication and role-based access
- Data encryption
- Automated backups
- Reporting dashboard