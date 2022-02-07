from unittest import TestCase

from DependendClassCallDuringUnitTestException import *
from Trip import *
from TripService import TripService
from UserNotLoggedInException import UserNotLoggedInException


class TripServiceTest(TestCase):
    def setUp(self) -> None:
        pass

    def test_should_throw_an_exception_when_user_is_not_logged_in(self):
        pass

    def test_should_not_return_any_trips_when_users_are_not_friends(self):
        pass

    def test_should_return_friend_trips_when_users_are_friends(self):
        pass


class TestableTripService(TripService):
    def getTripsByUser(self, user):
        pass
