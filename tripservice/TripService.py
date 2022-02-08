from TripDAO import TripDAO
from UserSession import UserSession
from UserNotLoggedInException import UserNotLoggedInException


class TripService:
    def getTripsByUser(self, user):
        logged_in_user = self.getLoggedInUser()
        tripList = []
        if logged_in_user:
            isFriend = user.isFriendsWith(logged_in_user)
            if isFriend:
                tripList = self.findTripsByUser(user)
            return tripList
        else:
            raise UserNotLoggedInException()

    def getLoggedInUser(self):
        return UserSession.getInstance().getLoggedUser()

    def findTripsByUser(self, user):
        return TripDAO.findTripsByUser(user)
