# flask-note-app
Note management application.

Functionalities:

- possibility to register
- possibility to log in
- possibility to create and delete notes
- possibility to view all your notes


Technology Stack:

- Python with Flask framework (for backend logic)
- PostgreSQL database (for storing Users and Notes)
- SQLAlchemy - Object-Relational Mapping (ORM) for efficient data management
- Jinja - templating engine for generating dynamic HTML content
- Bootstrap - for enhanced user interface (UI) and user experience (UX)
- Flask-Login - for secure login functionality and session management

Running the app:

1. Navigate to the project directory.
2. Run `python -m venv venv`.
3. Run `source .//venv//Scripts//activate`.
4. Run `pip install -r requirements.txt`.
5. Create a new `.env` file in the main directory.
6. Paste the required configuration values into the `.env` file.
7. Navigate back to the project main directory and run `python main.py`.