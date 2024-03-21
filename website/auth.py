from flask import Blueprint, render_template, request, flash, redirect, url_for
import re
from .models import User, Note, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


# A regular expression for validating an Email
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

auth = Blueprint('auth', __name__)


def check_input_for_register(email, firstName, password1, password2, error=None):
    if not email:
        error = 'Email is required'
    elif re.fullmatch(EMAIL_REGEX, email) == False:
        error = 'Invalid email'
    elif not firstName:
        error = 'First name is required'
    elif not password1:
        error = 'Password is required'
    elif not password2:
        error = 'Please confirm your password'
    elif len(firstName) < 4:
        error = 'Username is too short'
    elif not firstName.isalnum():
        error = 'Only letters and digits'
    elif len(password1) < 8:
        error = 'Password is too short'
    elif not password1.isalnum():
        error = 'Only letters and digits'
    elif password1 != password2:
        error = 'Passwords are different, please input two same passwords'
    elif len(firstName) > 50 or len(password1) > 50:
        error = 'Too long username or password'
    return error


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', user=current_user)
    elif request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # get user from database if exist or 'None' if not exist
        user = session.query(User).filter_by(email=email).one_or_none()

        # if user is not exist in database
        if user is None:
            flash(f'Email does not exist.', category='error')
            return render_template('login.html', user=current_user)
        # if user exist in database
        else:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.index', user=current_user))
            else:
                flash('Incorrect password, try again.', category='error')
                return render_template('login.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html', user=current_user)
    elif request.method == 'POST':
        email = request.form['email']
        first_name = request.form['firstName']
        password1 = request.form['password1']
        password2 = request.form['password2']

        user = session.query(User).filter_by(email=email).one_or_none()
        # if user exist in database
        if user:
            flash('Email already exists.', category='error')
            return render_template('sign_up.html', user=current_user)

        error = check_input_for_register(email, first_name, password1, password2)

        # if we have bad input format
        if error is not None:
            flash(error, category='error')
            return render_template('sign_up.html', user=current_user)
        # if we have good input format
        elif error is None:
            new_user = User(email, generate_password_hash(password1), first_name)
            session.add(new_user)
            session.commit()
            login_user(new_user, remember=True)
            flash('Account created successfully.', category='success')
            return redirect(url_for('views.index', user=current_user))

