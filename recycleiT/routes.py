import os
import uuid

from flask import render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_user

# from flask_login import login_user, logout_user, login_required, current_user

from database import *
from server import app
from models import User
from forms import RegisterForm, LoginForm

from __init__ import app


@app.route("/")
@app.route("/home")
def index():
    return render_template('home.html')


@app.route("/leaderboard")
def leaderboard():
    users = get_leaderboard()
    return render_template('leaderboard.html', users=users)


@app.route('/<username>')
def about(username):
    user = get_user_by_username(username)
    print(user)
    return render_template('profile.html', user=user)


@app.route('/guide')
def guide():
    return render_template('guide.html')


@app.route('/map')
def maps():
    return render_template('map.html')


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = get_user_by_username(form.username.data)
        if attempted_user is not None:
            # login_user()
            flash(f'Succes! You are logged in as:{attempted_user.username}', category='success')
            return redirect(url_for(about, username=attempted_user.username))
        else:
            flash(f'Username-ul si parola nu sunt corecte', category='danger')
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
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
        return redirect(url_for('profile'))

    if form.errors != {}:
        for err_msg in form.errors.values():
            flash(f'There was an error{err_msg}', category='danger')

    return render_template('register.html', form=form)


if __name__ == "__main__":
    if not os.environ.get('IS_CONTAINER'):
        app.run(debug=True, port=8080)
    else:
        port = os.environ.get('PORT')
        if port is None:
            port = '8080'
        app.run(host=f'0.0.0.0:{port}')
