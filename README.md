# PrashantSaxe-StudyChamber

## Overview
PrashantSaxe-StudyChamber is a **Django-based web application** designed to facilitate **online study discussions**. Users can join different study rooms, engage in conversations, and collaborate on various topics. The project follows the **MVC (Model-View-Controller) architecture**, making it modular and easy to extend.

## Features
- **User Authentication** – Secure login and registration system.
- **Study Rooms** – Users can create and join topic-based discussion rooms.
- **Real-time Conversations** – Engage in discussions with other users.
- **Topic Categorization** – Rooms are organized based on study topics.
- **Responsive UI** – Built using Django templates for seamless user experience.

---

## Tech Stack
### Backend:
- **Framework** – Django (Python)
- **Database** – SQLite (default, can be extended to PostgreSQL)
- **Authentication** – Django Authentication System
- **Template Engine** – Django Templates

### Frontend:
- **HTML & CSS** – Django template rendering
- **JavaScript** – For interactive UI components

---

## Directory Structure
```
prashantsaxe-studychamber/
├── README.md
├── apiexample.html
├── db.sqlite3
├── manage.py
├── requirements.txt
├── base/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       ├── 0001_initial.py
│       └── __init__.py
├── static/
│   ├── images/
│   │   ├── 1868782.jfif
│   │   ├── 35072868.jfif
│   │   └── icons/
│   ├── js/
│   │   └── script.js
│   └── styles/
│       ├── main.css
│       └── style.css
├── studyChamber/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── __pycache__/
├── templates/
│   ├── main.html
│   └── navbar.html
└── theme/
    ├── activity.html
    ├── create-room.html
    ├── delete.html
    ├── edit-user.html
    ├── index.html
    ├── login.html
    ├── profile.html
    ├── room.html
    ├── script.js
    ├── settings.html
    ├── signup.html
    ├── style.css
    ├── topics.html
    ├── .prettierrc
    └── assets/
        └── icons/
```

---

## Setup Instructions
### Prerequisites:
- Python 3.8+
- Virtual Environment (recommended)

### Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/PrashantSaxe-StudyChamber.git
   cd PrashantSaxe-StudyChamber
   ```
2. **Setup Virtual Environment**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Apply Migrations**
   ```sh
   python manage.py migrate
   ```
5. **Start the Development Server**
   ```sh
   python manage.py runserver
   ```
6. **Open in Browser**
   - http://127.0.0.1:8000/

---

## API Endpoints
### Authentication
- `POST /auth/signup/` – Register a new user
- `POST /auth/login/` – Authenticate user

### Study Room Management
- `GET /rooms/` – Fetch all study rooms
- `GET /rooms/:id/` – Get details of a specific room
- `POST /rooms/create/` – Create a new study room
- `DELETE /rooms/:id/` – Delete a study room (Admin only)

### Discussions
- `POST /rooms/:id/comment/` – Add a comment
- `GET /rooms/:id/comments/` – Fetch comments

---

## Contributing
We welcome contributions! To contribute:
1. **Fork the repository**
2. **Create a new branch** (`feature/your-feature`)
3. **Commit your changes**
4. **Push and open a pull request**

---

## License
**No License** – This project does not currently have a license.

---

## Contact
For inquiries or collaboration, feel free to reach out!

