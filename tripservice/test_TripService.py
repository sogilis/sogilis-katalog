from unittest import TestCase

from DependendClassCallDuringUnitTestException import *
from Trip import *
from TripService import TripService
from UserNotLoggedInException import UserNotLoggedInException
from User import User


class TripServiceTest(TestCase):
    def setUp(self) -> None:
        pass

    def test_should_throw_an_exception_when_user_is_not_logged_in(self):
        tripService = TestableTripService()
        tripService.setLoggedInUser(TripServiceTest.GUEST)
        self.assertRaises(UserNotLoggedInException,
                          tripService.getTripsByUser, TripServiceTest.UNUSED_USER)

    def test_should_not_return_any_trips_when_users_are_not_friends(self):
        pass

    def test_should_return_friend_trips_when_users_are_friends(self):
        pass

    GUEST = None
    UNUSED_USER = None


class TestableTripService(TripService):
    def getLoggedInUser(self):
        return self.loggedInUser

    def setLoggedInUser(self, logged_in_user):
        self.loggedInUser = logged_in_user
