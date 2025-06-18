# CV Generator (Django)

A Django-based web application that allows users to generate CVs by filling out a multi-step form and download them as PDFs.  
Includes REST API support and Swagger documentation.

## Features
- Multi-step CV form
- PDF generation
- Bootstrap styling
- REST API using Django REST Framework
- Swagger UI

## Tech Stack
- Django
- SQLite
- Bootstrap
- Django REST Framework
- xhtml2pdf

## Run Locally

```bash
git clone https://github.com/rahimjonovali/CV-generator.git
cd cv_generator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
