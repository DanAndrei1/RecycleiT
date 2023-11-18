import os

from __init__ import app


@app.route("/")
@app.route("/home")
def index():
    return "Hello"


@app.route("/leaderboard")
def leaderboard():
    return "Leaderboard"


@app.route("/profile")
def profile():
    return "Profile"


@app.route("/guide")
def guide():
    return "Guide"


@app.route("/maps")
def maps():
    return "Map"


@app.route('/login')
def login():
    return 'Login'


@app.route('/register')
def register():
    return 'Register'


if __name__ == "__main__":
    if not os.environ.get('IS_CONTAINER'):
        app.run(debug=True, port=8080)
    else:
        port = os.environ.get('PORT')
        if port is None:
            port = '8080'
        app.run(host=f'0.0.0.0:{port}')
