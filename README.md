# Workforce Analytics Dashboard

A modern, Flask-based workforce analytics system built to help teams manage tasks and visualize progress through a clean, responsive dashboard. Each user logs in with their own account to view their assigned projects and tasks, track completion status, and monitor progress through interactive visual graphs.

🔗 **Live Demo:** [workforce-analytics-1yw2.onrender.com](https://workforce-analytics-1yw2.onrender.com/)

---

## Overview

This project demonstrates full-stack web development fundamentals — from backend routing and authentication to frontend templating and cloud deployment. It was built to simulate a real-world workforce management tool where individuals can track their own tasks and productivity in one place.

---

## Key Features

- 🔐 **User Authentication** — Secure login and registration system, with each user having their own account and dashboard
- 📊 **Progress Tracking** — Visual graphs showing tasks completed vs. tasks remaining
- 🗂️ **Task & Project Management** — Users can view and manage their assigned projects and tasks
- 🎯 **Interactive Dashboard** — Clean, card-based UI for an at-a-glance view of workload
- 🎨 **Modern, Responsive Design** — Built with clean CSS for a polished look across devices
- 🌐 **Fully Deployed** — Live and accessible as a hosted web application
- ⚡ **Lightweight & Fast** — Minimal, efficient Flask backend

---

## Tech Stack

| Layer        | Technology                                  |
|--------------|----------------------------------------------|
| Backend      | Python (Flask)                              |
| Frontend     | HTML5, CSS3, Jinja2 (Flask templating)      |
| Deployment   | Render (hosting), GitHub (version control)  |

---

## Project Structure

```
workforce-analytics/
├── app.py                 # Main Flask application
├── requirements.txt        # Project dependencies
├── templates/              # HTML pages
│   ├── dashboard.html
│   ├── login.html
│   └── register.html
├── static/                 # CSS and assets
│   └── style.css
└── venv/                   # Virtual environment (not deployed)
```

---

## How It Works

1. A user registers or logs into their account.
2. Authentication is handled via Flask routes.
3. Upon login, the user's personalized dashboard loads.
4. Assigned tasks and projects are displayed in structured UI cards.
5. Progress graphs update to reflect completed vs. remaining work.
6. The backend serves all pages dynamically using Jinja2 templates.

---

## Getting Started (Local Setup)

Clone the repository and set up the project locally:

```bash
git clone https://github.com/rashibaisla/workforce-analytics-.git
cd workforce-analytics-

pip install -r requirements.txt

python app.py
```

Then open your browser to:

```
http://127.0.0.1:5000
```

---

## Learning Outcomes

Building this project helped strengthen understanding of:

- Flask backend development
- Routing and template rendering
- Frontend–backend integration
- Structuring a full-stack project
- Deployment on cloud platforms
- Git & GitHub workflow

---

## Future Improvements

- 📈 Real-time analytics charts (Chart.js)
- 🗄️ Database integration (SQLite / PostgreSQL) for persistent task/project storage
- 👥 Role-based authentication (e.g., manager vs. employee views)
- ☁️ API-based data handling for dynamic task updates

---

Built with a focus on learning full-stack development and creating a real, deployable workforce management tool.





## Live Link
https://workforce-analytics-1yw2.onrender.com/
