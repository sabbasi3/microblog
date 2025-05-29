# Microblog

A multilingual, full-featured microblogging web application built with Flask, SQLAlchemy, HTML, JavaScript, and Elasticsearch.

Check it out at: https://blog.safanabbasi.com

---

## Features

- User registration, login, and profile management
- Password reset via email
- Follow/unfollow users and see posts from followed users
- Full-text search powered by Elasticsearch
- Multilingual support (English, Spanish, Urdu)
- Post translation using Microsoft Translator API
- Responsive Bootstrap 5 UI
- Background task processing with Redis and RQ
- Email notifications for admins and users
- Error logging and reporting
- REST API endpoints
- Docker support for deployment

---

## Project Structure

```
.
├── app/
│   ├── api/            # REST API blueprint
│   ├── auth/           # Authentication blueprint
│   ├── errors/         # Error handlers blueprint
│   ├── main/           # Main application blueprint
│   ├── static/         # Static files
│   ├── templates/      # Jinja2 templates
│   ├── translations/   # Babel translations
│   ├── __init__.py     # App factory and extensions
│   ├── cli.py          # CLI commands for translations
│   ├── email.py        # Email sending utilities
│   ├── models.py       # SQLAlchemy models
│   ├── search.py       # Elasticsearch integration
│   ├── tasks.py        # Background task definitions
│   └── translate.py    # Microsoft Translator integration
├── config.py           # Configuration
├── microblog.py        # App entry point
├── reindex_posts.py    # Script to reindex posts in Elasticsearch
├── send_email.py       # Script to send a test email
├── tests.py            # Unit tests
├── .env                # Environment variables
├── .flaskenv           # Flask environment variables
├── .gitignore
├── app.db              # SQLite database
├── logs/               # Log files
├── migrations/         # Database migrations
├── safanvenv/          # Virtual environment (Windows)
├── safanvenv_wsl/      # Virtual environment (WSL/Linux)
└── requirements.txt    # Python dependencies
```

---

## Setup

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd microblog
```

### 2. Create a virtual environment

#### **On Linux/macOS (recommended):**
```sh
python3 -m venv venv
source venv/bin/activate
```

#### **On Windows (Command Prompt):**
```sh
python -m venv venv
venv\Scripts\activate
```

#### **On WSL2:**
```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```

### 4. Set environment variables

Create a `.env` file in the project root with the following content (edit values as needed):

```
SECRET_KEY=your-secret-key
MAIL_SERVER=smtp.sendgrid.net
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=apikey
MAIL_PASSWORD=your-sendgrid-api-key
MAIL_DEFAULT_SENDER=contact@yourdomain.com
ADMINS=your-email@example.com
POSTS_PER_PAGE=5
LANGUAGES=en,es,ur_PK
MS_TRANSLATOR_KEY=your-microsoft-translator-key
ELASTICSEARCH_URL=http://localhost:9200
DATABASE_URL=sqlite:///absolute/path/to/app.db
REDIS_URL=redis://
```

> **Tip:** For SQLite, use an absolute path for `DATABASE_URL` that matches your OS (e.g., `sqlite:////home/username/microblog/app.db` on Linux/WSL2).

### 5. Initialize the database

```sh
flask init  # Only needed the first time to set up migrations
flask db migrate -m "Initial migration"
flask db upgrade
```

### 6. Update the database after model changes

Whenever you make changes to your models (add, remove, or modify fields), run:

```sh
flask db migrate -m "Describe your change"
flask db upgrade
```

This will generate a new migration script and apply it to your database.

---

### 7. (Optional) Reindex existing posts for search

```sh
python reindex_posts.py
```

### 8. Run Redis server (for background tasks)

```sh
redis-server
```

### 9. Start the RQ worker (in a new terminal)

```sh
source venv/bin/activate  # or safanvenv_wsl/bin/activate
rq worker microblog-tasks
```

### 10. Run the application

```sh
flask run
```

---

## Testing

Run the unit tests with:

```sh
python tests.py
```

---

## Search & Translation

- **Search:** Requires a running Elasticsearch instance (e.g., via Docker).
- **Translation:** Requires a valid Microsoft Translator API key.

---

## License

This project is licensed under the MIT License.

---

**Note:**  
- For translation/localization commands, see [`app/cli.py`](app/cli.py).
- For more details on configuration, see [`config.py`](config.py).