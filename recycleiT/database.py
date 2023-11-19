from datetime import datetime

from flask_login import current_user

from __init__ import cursor, login_manager, connect
from models import User, Recycling


@login_manager.user_loader
def load_user(user_id):
    cursor.execute('select * from users where id = %s', (user_id,))
    row = cursor.fetchall()
    try:
        user = User(id=row[0][0], lastName=row[0][1], firstName=row[0][2], username=row[0][3], email=row[0][4],
                    totalPoints=row[0][5], password=row[0][6])
        return user
    except Exception:
        return None


def get_user_by_username(username):
    cursor.execute('select * from users where username = %s', (username,))
    row = cursor.fetchall()
    try:
        user = User(id=row[0][0], lastName=row[0][1], firstName=row[0][2], username=row[0][3], email=row[0][4],
                    totalPoints=row[0][5], password=row[0][6])
        return user
    except Exception:
        return None


def get_user_by_email(email):
    cursor.execute('select * from users where email = %s', (email,))
    row = cursor.fetchall()
    try:
        user = User(id=row[0][0], lastName=row[0][1], firstName=row[0][2], username=row[0][3], email=row[0][4],
                    totalPoints=row[0][5], password=row[0][6])
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
        'insert into public.users values (%s, %s, %s, %s, %s,%s,%s)',
        (user.id, user.lastName, user.firstName, user.username,
         user.email, user.totalPoints, user.password)
    )
    connect.commit()


def get_leaderboard():
    cursor.execute('select username, total_points from public.users order by total_points desc limit 10')
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


def validate_barcode(id_barcode):
    recycle = get_recycle_by_barcode(id_barcode)
    if recycle is None:
        return True
    if recycle.id == id_barcode:
        return False
    return True


def add_points(id, points):
    cursor.execute('update users set total_points = total_points + %s where id = %s',
                   (points, id))
    connect.commit()


def add_barcode(barcode):
    data = barcode.split()
    try:
        nr = int(data[0])
        points = nr * 5
    except Exception:
        return None
    cursor.execute('insert into recycling values (%s, %s, %s, %s)',
                   (barcode, current_user.id, str(datetime.now()), points))
    add_points(current_user.id, points)
