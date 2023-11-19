from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, firstName, lastName, username, email, password, totalPoints):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.email = email
        self.password = password
        self.totalPoints = totalPoints

    @property
    def prettier_points(self):
        if len(str(self.totalPoints)) > 3:
            return f'{str(self.totalPoints)[:-3]},{str(self.totalPoints)[-3:]}'
        return str(self.totalPoints)


class Recycling:
    def __init__(self, id, idUser, recycleDate, allocatedPoints):
        self.id = id
        self.idUser = idUser
        self.recycleDate = recycleDate
        self.allocatePoints = allocatedPoints


class Friendship:
    def __init__(self, id1, id2, friendsSince):
        self.id1 = id1
        self.id2 = id2
        self.friendsSince = friendsSince
