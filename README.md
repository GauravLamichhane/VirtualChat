# Task Management Platform

A modern Task Management web application built with **Django REST Framework (DRF)** and React.  
It allows users to create, update, and manage tasks efficiently with secure authentication and role-based access.

---

## 📝 Project Description

This project is a full-stack task management system. Features include:

- User registration and login
- CRUD operations for tasks
- Task assignment to users
- Audit logs for task actions
- RESTful API endpoints
- Interactive API documentation (Swagger & ReDoc)

---

## 🛠 Tech Stack

**Backend:**  
- Python 3.11+  
- Django 5.2  
- Django REST Framework (DRF)  
- drf-spectacular (OpenAPI 3 / Swagger docs)  
- PostgreSQL (for production)  

**Frontend:**  
- React.js  
- Tailwind CSS  

**Other Tools:**  
- Git / GitHub  
- Vercel / Render (for deployment)  

---

## ⚡ Setup Instructions

### Backend (Django)

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/task-management-platform.git
cd task-management-platform/server
```
2. **Create and activate a virtual environment**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt

```
4. **Set up environment variables**

Create a .env file based on .env.example:
```bash
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

5. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run the development server**
```bash
python manage.py runserver
```

## Frontend (React)

1. **Navigate to the client folder**
```bash
cd ../client
```

2. **Install dependencies**
```bash
npm install
```

3. **Run the frontend server**
```bash
npm start
```
## API Documentation
```bash
The API is documented using drf-spectacular (Swagger & ReDoc).

Swagger UI (interactive): http://127.0.0.1:8000/api/docs/swagger/

ReDoc UI: http://127.0.0.1:8000/api/docs/redoc/

OpenAPI JSON schema: http://127.0.0.1:8000/api/schema/

All endpoints, parameters, request/response formats, and authentication details are available here.
```
## Environment Variables
```bash
Variable	Description
SECRET_KEY	Django secret key
DEBUG	True for development, False for production
DB_NAME	PostgreSQL database name
DB_USER	PostgreSQL user
DB_PASSWORD	PostgreSQL password
DB_HOST	Database host (default localhost)
DB_PORT	Database port (default 5432)
```
## Deployment Links
Frontend: https://task-management-platform.vercel.app

Backend API: https://task-management-platform.onrender.com

## Screenshots 
