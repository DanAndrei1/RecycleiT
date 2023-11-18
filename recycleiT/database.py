from __init__ import cursor
from recycleiT.models import User


# @login_manager.user_loader
# def load_user(user_id):
#     cursor.execute('select * from public.users where id = %s', (user_id,))
#     row = cursor.fetchall()
#     try:
#         user = User(id=row[0][0], username=row[0][1], email=row[0][2], password=row[0][3], budget=row[0][4])
#         return user
#     except Exception:
#         return None


def get_user_by_username(username):
    cursor.execute('select * from public.users where username = %s', (username,))
    row = cursor.fetchall()
    try:
        user = User(id=row[0][0], username=row[0][1], email=row[0][2], password=row[0][3], budget=row[0][4])
        return user
    except Exception:
        return None


def get_user_by_email(email):
    cursor.execute('select * from public.users where email = %s', (email,))
    row = cursor.fetchall()
    try:
        user = User(id=row[0][0], username=row[0][1], email=row[0][2], password=row[0][3], budget=row[0][4])
        return user
    except Exception:
        return None


def get_leaderboard():
    cursor.execute('select (username, total_points) from users order by total_points limit 10')
    row = cursor.fetchall()
    try:
        users = [[None] * 10]
        for i in range(10):
            users[i][0] = row[i][0]
            users[i][1] = row[i][1]
        return users
    except Exception:
        return None
