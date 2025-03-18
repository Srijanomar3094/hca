# Project Setup-> HealthCare-Application(HCA) for WhatBytes  

## Prerequisites
- Python 3.x installed
- PostgreSQL installed and running
- Virtual environment package (optional but recommended)

## Setup Instructions

### 1. Clone the Repository
```sh
git clone https://github.com/Srijanomar3094/hca
cd hca
```

### 2. Create and Configure `.env` File
Create a `.env` file in the project root and add the following credentials:
```ini
DB_NAME="your_database_name"
DB_USER="your_database_user"
DB_PASSWORD="your_database_password"
DB_HOST="your_database_host"
DB_PORT="your_database_port"
```

### 3. Create and Activate Virtual Environment
```sh
python -m venv venv
# Activate virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 4. Install Dependencies
```sh
pip install -r requirements.txt
```

### 5. Apply Migrations
```sh
python manage.py migrate
```

### 6. Start the Server
```sh
python manage.py runserver
```

### 7. Test APIs
Use Postman or any API testing tool to test all defined API endpoints.

1. Authentication APIs

POST /api/auth/register/ 

POST /api/auth/login/

2. Patient Management APIs

POST /api/patients/ 

GET /api/patients/ 

GET /api/patients/<id>/

PUT /api/patients/<id>/ 

DELETE /api/patients/<id>/ 

3. Doctor Management APIs

POST /api/doctors/ - Add a new doctor (Authenticated users only).

GET /api/doctors/ 

GET /api/doctors/<id>/ 

PUT /api/doctors/<id>/ 

DELETE /api/doctors/<id>/ 

4. Patient-Doctor Mapping APIs

POST /api/mappings/ 

GET /api/mappings/ 

GET /api/mappings/<patient_id>/ 

DELETE /api/mappings/<id>/ 

----

