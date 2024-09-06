from User import User


class UserBuilder:
    def __init__(self):
        self.trips = []
        self.friends = []

    def aUser():
        return UserBuilder()

    def friendsWith(self, friends):
        self.friends = friends
        return self

    def withTrips(self, trips):
        self.trips = trips
        return self

    def build(self):
        user = User()
        self._addTripsTo(user)
        self._addFriendsTo(user)
        return user

    def _addFriendsTo(self, user):
        for friend in self.friends:
            user.addFriend(friend)

    def _addTripsTo(self, user):
        for trip in self.trips:
            user.addTrip(trip)
