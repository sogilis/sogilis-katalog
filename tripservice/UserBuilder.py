from User import User


class UserBuilder:
    def __init__(self):
        self.trips = []
        self.friends = []

    def friendsWith(self, friends):
        self.friends = friends
        return self

    def withTrips(self, trips):
        self.trips = trips
        return self

    def build(self):
        user = User()
        self.addTripsTo(user)
        self.addFriendsTo(user)
        return user

    def addFriendsTo(self, user):
        for friend in self.friends:
            user.addFriend(friend)

    def addTripsTo(self, user):
        for trip in self.trips:
            user.addTrip(trip)


def aUser():
    return UserBuilder()
