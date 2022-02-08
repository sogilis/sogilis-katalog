from TripDAO import TripDAO
from UserSession import UserSession
from UserNotLoggedInException import UserNotLoggedInException


class TripService:
    def getTripsByUser(self, user):
        if self.getLoggedInUser() == None:
            raise UserNotLoggedInException()
        if user.isFriendsWith(self.getLoggedInUser()):
            return self.findTripsByUser(user)
        else:
            return []

    def getLoggedInUser(self):
        return UserSession.getInstance().getLoggedUser()

    def findTripsByUser(self, user):
        return TripDAO.findTripsByUser(user)
