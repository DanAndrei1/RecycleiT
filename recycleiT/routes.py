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


if __name__ == "__main__":
    app.run(debug=True)
