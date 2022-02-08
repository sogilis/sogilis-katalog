from TripDAO import TripDAO
from UserSession import UserSession
from UserNotLoggedInException import UserNotLoggedInException


class TripService:
    def getTripsByUser(self, user):
        logged_in_user = self.getLoggedInUser()
        if logged_in_user == None:
            raise UserNotLoggedInException()
        if user.isFriendsWith(logged_in_user):
            return self.findTripsByUser(user)
        else:
            return []

    def getLoggedInUser(self):
        return UserSession.getInstance().getLoggedUser()

    def findTripsByUser(self, user):
        return TripDAO.findTripsByUser(user)
