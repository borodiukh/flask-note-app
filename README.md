### Flask-note-app
Note management application.

### 2 versions in 2 branches 
- There are 2 versions of the note app project. 
- The first version uses PostgreSQL and is available on the `main` branch. 
- The second version uses SQLite and is available on the `sqlite_branch` branch.

# Deployment 
You can visit the website and use my (Note app) [https://erere.pythonanywhere.com/]

# Functionalities:

- possibility to register
- possibility to log in
- possibility to create and delete notes
- possibility to view all your notes


# Technology Stack:

- Python with Flask framework (for backend logic)
- PostgreSQL database (for storing Users and Notes)
- SQLAlchemy - Object-Relational Mapping (ORM) for efficient data management
- Jinja - templating engine for generating dynamic HTML content
- Bootstrap - for enhanced user interface (UI) and user experience (UX)
- Flask-Login - for secure login functionality and session management

# Running the app:

To clone the repository, use the command `git clone`.
Follow these steps to set up the project:
1. Navigate to the project directory.
2. Make sure you have Python installed.
3. Create a virtual environment with the command `python -m venv venv`. (command for Windows)
4. Activate the virtual environment with `source ./venv/Scripts/activate`. (command for Windows)
5. Install the required packages by running `pip install -r requirements.txt`.
6. Ensure that PostgreSQL is installed on your computer and that a database named `note_app` exists.
7. Create a new `.env` file in the main directory.
8. Paste the required configuration values into the `.env` file, including the `DB_USER` and `DB_PASSWORD` for PostgreSQL.
9. Finally, navigate back to the project main directory and run `python main.py`.