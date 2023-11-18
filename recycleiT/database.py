from RecycleiT.recycleiT import login_manager, cursor
from RecycleiT.recycleiT.models import User


@login_manager.user_loader
def load_user(user_id):
    cursor.execute('select * from public.users where id = %s', (user_id,))
    row = cursor.fetchall()
    try:
        user = User(id=row[0][0], username=row[0][1], email=row[0][2], password=row[0][3], budget=row[0][4])
        return user
    except Exception:
        return None


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
