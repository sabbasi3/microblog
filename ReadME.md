# Microblog

A multilingual, full-featured microblogging web application built with Flask, SQLAlchemy, HTML, JavaScript, and Elasticsearch.

## Features

- User registration, login, and profile management
- Password reset via email
- Follow/unfollow users and see posts from followed users
- Full-text search powered by Elasticsearch
- Multilingual support (English, Spanish, Urdu)
- Post translation using Microsoft Translator API
- Responsive Bootstrap 5 UI
- Error logging and email notifications for admins

## Project Structure

```
.
├── app/
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
│   └── translate.py    # Microsoft Translator integration
├── config.py           # Configuration
├── microblog.py        # App entry point
├── reindex_posts.py    # Script to reindex posts in Elasticsearch
├── send_email.py       # Script to send a test email
├── tests.py            # Unit tests
├── .flaskenv           # Flask environment variables
├── .gitignore
├── app.db              # SQLite database
├── logs/               # Log files
├── migrations/         # Database migrations
└── safanvenv/          # Virtual environment
```

## Setup

1. **Clone the repository and create a virtual environment:**

    ```sh
    git clone <your-repo-url>
    cd microblog
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

2. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Set environment variables:**

    Create a `.env` file or set variables in your shell for:

    - `SECRET_KEY`
    - `MAIL_SERVER`, `MAIL_PORT`, `MAIL_USE_TLS`, `MAIL_USERNAME`, `MAIL_PASSWORD`
    - `ADMINS` (comma-separated emails)
    - `ELASTICSEARCH_URL` (e.g., `http://localhost:9200`)
    - `MS_TRANSLATOR_KEY` (Microsoft Translator API key)

4. **Initialize the database:**

    ```sh
    flask db upgrade
    ```

5. **(Optional) Reindex existing posts for search:**

    ```sh
    python reindex_posts.py
    ```

6. **Run the application:**

    ```sh
    flask run
    ```

## Testing

Run the unit tests with:

```sh
python tests.py
```

## Search & Translation

- **Search:** Requires a running Elasticsearch instance (e.g., via Docker).
- **Translation:** Requires a valid Microsoft Translator API key.

## License

This project is licensed under the MIT License.

---

**Note:**  
- For translation/localization commands, see [`app/cli.py`](app/cli.py).
- For more details on configuration, see [`config.py`](config.py).