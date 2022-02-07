from unittest import TestCase

from DependendClassCallDuringUnitTestException import *
from Trip import *
from TripService import TripService
from UserNotLoggedInException import UserNotLoggedInException
from User import User


class TripServiceTest(TestCase):
    def setUp(self) -> None:
        self.tripService = TestableTripService()
        pass

    def test_should_throw_an_exception_when_user_is_not_logged_in(self):
        self.tripService.setLoggedInUser(TripServiceTest.GUEST)
        self.assertRaises(UserNotLoggedInException,
                          self.tripService.getTripsByUser, TripServiceTest.UNUSED_USER)

    def test_should_not_return_any_trips_when_users_are_not_friends(self):
        self.tripService.setLoggedInUser(TripServiceTest.REGISTERED_USER)
        friend = User()
        friend.addFriend(TripServiceTest.ANOTHER_USER)
        friend.addTrip(TripServiceTest.TO_BRAZIL)
        trips = self.tripService.getTripsByUser(friend)
        self.assertEqual(len(trips), 0, "no trips")

    def test_should_return_friend_trips_when_users_are_friends(self):
        self.tripService.setLoggedInUser(TripServiceTest.REGISTERED_USER)
        friend = User()
        friend.addFriend(TripServiceTest.ANOTHER_USER)
        friend.addFriend(TripServiceTest.REGISTERED_USER)
        friend.addTrip(TripServiceTest.TO_BRAZIL)
        friend.addTrip(TripServiceTest.TO_LONDON)

        trips = self.tripService.getTripsByUser(friend)
        self.assertEqual(len(trips), 2, "two trips")

    GUEST = None
    UNUSED_USER = None
    REGISTERED_USER = User()
    ANOTHER_USER = User()
    TO_BRAZIL = Trip()
    TO_LONDON = Trip()


class TestableTripService(TripService):
    def getLoggedInUser(self):
        return self.loggedInUser

    def setLoggedInUser(self, logged_in_user):
        self.loggedInUser = logged_in_user

    def findTripsByUser(self, user):
        return user.getTrips()
