from __init__ import cursor
from models import User, Recycling


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
        user = User(id=row[0][0], lastName=row[0][1], firstName=row[0][2], username=row[0][3], email=row[0][4])
        return user
    except Exception:
        return None


def get_user_by_email(email):
    cursor.execute('select * from public.users where email = %s', (email,))
    row = cursor.fetchall()
    try:
        user = User(id=row[0][0], lastName=row[0][1], firstName=row[0][2], username=row[0][3], email=row[0][4])
        return user
    except Exception:
        return None


def get_recycle_by_barcode(barcode):
    cursor.execute('select * from public.recycling where id = %s', (barcode,))
    row = cursor.fetchall()
    try:
        recycle = Recycling(id=row[0][0], id_user=row[0][1], recycleDate=row[0][2], allocatedPoints=row[0][3])
        return recycle
    except Exception:
        return None


def insert_user(user):
    cursor.execute(
        'insert into public.users values (%s, %s, %s, %s, %s)',
        (user.id, user.lastName, user.firstName, user.username,
         user.email)
    )
    cursor.commit()


def get_leaderboard():
    cursor.execute('select username, total_points from public.users order by total_points limit 10')
    row = cursor.fetchall()
    try:
        users = []
        cursor.execute('select count(*) from users')
        nr = cursor.fetchone()
        if nr[0] < 10:
            for i in range(nr[0]):
                user = [row[i][0], row[i][1]]
                users.append(user)
            return users
        else:
            for i in range(10):
                user = [row[i][0], row[i][1]]
                users.append(user)
            return users
    except Exception:
        return None
