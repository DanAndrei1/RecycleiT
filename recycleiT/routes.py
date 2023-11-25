import os
import uuid

from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required

from scancode import get_text
from database import *
from models import User
from forms import RegisterForm, LoginForm

from __init__ import app


@app.route("/")
@app.route("/home")
def index():
    return render_template('home.html')


@app.route("/leaderboard")
@login_required
def leaderboard():
    users = get_leaderboard()
    return render_template('leaderboard.html', users=users)


@app.route('/<username>')
@login_required
def about(username):
    user = get_user_by_username(username)
    return render_template('profile.html', user=user)


@app.route('/guide')
def guide():
    return render_template('guide.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.is_submitted() and form.validate_username(form.username.data):
        attempted_user = get_user_by_username(form.username.data)
        if attempted_user is not None:
            login_user(attempted_user)
            flash(f'Succes! You are logged in as:{attempted_user.username}', category='success')
            return redirect(url_for('about', username=attempted_user.username))
        else:
            flash(f'Username-ul si parola nu sunt corecte', category='danger')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.is_submitted() and form.validate_username(form.username.data) and form.validate_email(form.email.data):
        user_to_create = User(id=str(uuid.uuid4()),
                              firstName=form.first_name.data,
                              lastName=form.last_name.data,
                              username=form.username.data,
                              email=form.email.data,
                              password=form.password1.data,
                              totalPoints=0
                              )
        insert_user(user_to_create)
        login_user(user_to_create)
        flash(f'Account created successfully! You are logged in as {user_to_create.username}', category='success')
        return redirect(url_for('about', username=user_to_create.username))
    elif form.errors != {}:
        redirect(url_for('guide'))

    return render_template('register.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have been logged out", category='info')
    return redirect(url_for('index'))


@app.route('/scanner')
@login_required
def scan():
    return render_template('scanner.html')


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file:
        file.save(file.filename)
        barcode = get_text(file.filename)
        add_barcode(barcode)
        return redirect('scanner')


if __name__ == "__main__":
    if not os.environ.get('IS_CONTAINER'):
        app.run(debug=True, port=8080)
    else:
        port = os.environ.get('PORT')
        if port is None:
            port = '8080'
        app.run(host=f'0.0.0.0:{port}')
