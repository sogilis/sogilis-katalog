from TripDAO import TripDAO
from UserSession import UserSession
from UserNotLoggedInException import UserNotLoggedInException


class TripService:
    def getFriendsTrips(self, friend, loggedInUser):
        if loggedInUser == None:
            raise UserNotLoggedInException()
        if friend.isFriendsWith(loggedInUser):
            return self.findTripsByUser(friend)
        else:
            return self._noTrips()

    def findTripsByUser(self, user):
        return TripDAO.findTripsByUser(user)

    def _noTrips(self):
        return []
