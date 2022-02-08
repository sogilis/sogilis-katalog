from TripDAO import TripDAO
from UserSession import UserSession
from UserNotLoggedInException import UserNotLoggedInException


class TripService:
    def getTripsByUser(self, user, loggedInUser):
        if loggedInUser == None:
            raise UserNotLoggedInException()
        if user.isFriendsWith(loggedInUser):
            return self.findTripsByUser(user)
        else:
            return self._noTrips()

    def findTripsByUser(self, user):
        return TripDAO.findTripsByUser(user)

    def _noTrips(self):
        return []
