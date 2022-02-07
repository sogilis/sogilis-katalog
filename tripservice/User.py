class User:

    def __init__(self):
        self.trips = []
        self.friends = []

    def getFriends(self):
        return self.friends

    def addFriend(self, user):
        self.friends.append(user)

    def addTrip(self, trip):
        self.trips.append(trip)

    def getTrips(self):
        return self.trips

    def isFriendsWith(self, user):
        return user in self.friends
