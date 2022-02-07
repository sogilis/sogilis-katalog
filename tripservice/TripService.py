from TripDAO import TripDAO
from UserSession import UserSession
from UserNotLoggedInException import UserNotLoggedInException


class TripService:
    def getTripsByUser(self, user):
        logged_user = self.getLoggedInUser()
        isFriend = False
        tripList = []
        if logged_user:
            for friend in user.getFriends():
                if friend is logged_user:
                    isFriend = True
                    break
            if isFriend:
                tripList = TripDAO.findTripsByUser(user)
            return tripList
        else:
            raise UserNotLoggedInException()

    def getLoggedInUser(self):
        return UserSession.getInstance().getLoggedUser()
