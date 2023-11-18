class User:
    def __init__(self, id, firstName, lastName, username, email, password, totalPoints):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.email = email
        self.password = password
        self.totalPoints = totalPoints


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
