# Mecko Integration Platform

http://mekcosupply.com

This Django-based project was developed for **Mecko**, a Canadian company, to create a seamless integration between **Lightspeed** (a POS system) and **Zoho** (a suite of business applications). The platform automates data synchronization and facilitates real-time communication between the two systems.

## Features

- 🔄 Synchronizes customer and product data between Lightspeed and Zoho
- 📦 Syncs inventory levels and updates
- 🧾 Transfers sales data from Lightspeed to Zoho
- ✅ Error logging and retry mechanisms
- 🛠️ Modular design for easy maintenance and extension

## Tech Stack

- **Backend**: Django (Python)
- **APIs Used**:
  - Lightspeed Retail API
  - Zoho CRM / Inventory API
- **Database**: PostgreSQL (or your preferred DB engine)
- **Environment**: Docker-ready (optional)

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/mohammad0x/Server.git
   cd Server

   python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate

