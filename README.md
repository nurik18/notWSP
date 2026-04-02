# 🎓 NotWSP — Student Portal System

NotWSP is a web application designed to help students manage their academic activities in one place.
The system provides access to schedules, courses, grades, and assignments through a clean and user-friendly interface.

This project is inspired by existing university systems and represents an improved and simplified version of a student portal.

---

## 🚀 Features

* 🔐 JWT Authentication (Login / Logout)
* 📚 View enrolled courses
* 🗓️ Check weekly schedule
* 📊 View grades by course
* 📝 Manage assignments (CRUD)
* 🔎 Filter and organize academic data
* ⚠️ Error handling for API requests

---

## 🛠️ Tech Stack

### Frontend

* Angular (v17+)
* TypeScript
* Angular Routing
* FormsModule (ngModel)
* HttpClient

### Backend

* Django
* Django REST Framework (DRF)
* Token-based authentication
* PostgreSQL / SQLite

---

## 🧩 Project Structure

### Backend Models

* User (Django default)
* Course
* ScheduleItem (linked to Course & User)
* Grade (linked to Course & User)
* Assignment (linked to Course)

---

## 🔗 API Endpoints (examples)

* `POST /api/login/`
* `POST /api/logout/`
* `GET /api/courses/`
* `GET /api/schedule/`
* `GET /api/grades/`
* `GET /api/assignments/`
* `POST /api/assignments/`
* `PUT /api/assignments/{id}/`
* `DELETE /api/assignments/{id}/`

---

## 🖥️ Frontend Pages

* `/login` — User authentication
* `/dashboard` — Overview of student data
* `/courses` — List of courses
* `/schedule` — Weekly schedule
* `/grades` — Academic performance
* `/assignments` — Assignment management

---

## ⚙️ Setup Instructions

### Backend

```bash
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
ng serve
```

---

## 👥 Team Members

* Tursyn Akhad — Frontend
* Daulet Yerdos — Frontend
* Tasbolat Nurdaulet — Backend

---

## 📌 Project Goal

The goal of this project is to demonstrate full-stack development skills using Angular and Django REST Framework by building a functional and user-friendly student portal system.

---

## 📎 Additional

* Postman collection included in repository
* All API requests tested
* Error handling implemented
* CORS configured for frontend-backend communication

---

## 💡 Inspiration

Inspired by real university systems, NotWSP reimagines a more intuitive and accessible student experience.

---

## 🏁 Status

In development
