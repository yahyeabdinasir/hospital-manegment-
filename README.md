
# Odoo Hospital Management Module

A comprehensive Hospital Management System module for Odoo 15.0, designed to streamline healthcare operations, patient management, and medical workflows.

##  Features

### Core Functionalities
- **Patient Management**: Complete patient registration, history tracking, and profile management
- **Appointment Scheduling**: Book, reschedule, and manage patient appointments
- **Doctor Management**: Doctor profiles, specialties, availability, and workload tracking
- **Medical Records**: Digital medical history, prescriptions, and treatment plans
- **Department Management**: Hospital departments with specialized workflows
- **Lab Management**: Lab test requests, results, and tracking
- 
## 🚀 Installation

### Prerequisites
- Odoo 15.0 Community or Enterprise Edition
- Python 3.7+
- PostgreSQL 10+

### Method 1: Manual Installation
1. Clone this repository to your Odoo addons directory:
```bash
cd /path/to/odoo/addons
git clone https://github.com/yahyeabdinasir/hospital-manegment-.git


module structure 
om_hospital/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── patient.py
│   ├── doctor.py
│   ├── appointment.py
│   ├── department.py
│   └── billing.py
├── views/
│   ├── patient_views.xml
│   ├── doctor_views.xml
│   ├── appointment_views.xml
│   ├── department_views.xml
│   └── menu_views.xml
├── security/
│   ├── ir.model.access.csv
│   └── hospital_security.xml
├── data/
│   └── hospital_data.xml
├── static/
│   ├── description/
│   │   └── icon.png
│   └── src/
│       ├── css/
│       └── js/
└── reports/
    ├── patient_report.xml
    └── appointment_report.xml
