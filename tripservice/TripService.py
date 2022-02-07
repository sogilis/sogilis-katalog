from TripDAO import TripDAO
from UserNotLoggedInException import UserNotLoggedInException


class TripService:
    def getFriendsTrips(self, friend, loggedInUser):
        self.validate(loggedInUser)
        if friend.isFriendsWith(loggedInUser):
            return self.findTripsByUser(friend)
        else:
            return self.noTrips()

    def validate(self, loggedInUser):
        if loggedInUser == None:
            raise UserNotLoggedInException()

    def noTrips(self):
        return []

    def findTripsByUser(self, user):
        return TripDAO.findTripsByUser(user)
