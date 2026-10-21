# University LMS — Role-Based Access Control

> University seminar paper · Course VI-10 "Software Engineering" · University of Kragujevac · 2024

A minimal Learning Management System (LMS) built with Flask, demonstrating role-based access control (RBAC) with four user roles.

---

## What it does

| Role | Permissions |
|---|---|
| **Admin** | View all users, promote users to Professor role |
| **Professor** | Upload and edit course materials |
| **Student** | View course materials uploaded by professors |
| **Guest** | Read-only access to public content |

---

## Project Structure

```
src/flask_app/
├── app.py                  # Main Flask application
├── templates/
│   ├── login.html          # Login page
│   ├── admin.html          # Admin dashboard
│   ├── professor.html      # Professor panel (upload/edit materials)
│   ├── student.html        # Student view (read materials)
│   └── guest.html          # Guest page
└── static/
    └── welcome.jpg
```

---

## Quick Start

```bash
cd src/flask_app
pip install flask
python app.py
```

Navigate to `http://localhost:5000` and log in with:

| Username | Password | Role |
|---|---|---|
| `admin` | `adminpass` | Admin |
| `professor` | `professorpass` | Professor |
| `student` | `studentpass` | Student |
| `guest` | `guestpass` | Guest |

---

## Tech Stack

`Python` · `Flask` · `Jinja2` · `HTML`


## Demo scope and security

Run this coursework locally only. The listed accounts are intentional public demo
credentials, not leaked production passwords. Users and materials are held in memory.
The app uses a random session-signing key per process unless `SECRET_KEY` is supplied,
and the development server binds to loopback with debug disabled.

This is not a deployable LMS: persistent storage, password hashing, CSRF protection,
rate limiting and a fuller authorization model are still needed. A random session key
does not make the publicly known demo accounts safe for internet deployment.
