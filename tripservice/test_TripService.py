from unittest import TestCase

from DependendClassCallDuringUnitTestException import *
from Trip import *
from TripService import TripService
from UserBuilder import UserBuilder
from UserNotLoggedInException import UserNotLoggedInException
from User import User


class TripServiceTest(TestCase):
    def setUp(self) -> None:
        self.tripService = TestableTripService()
        pass

    def test_should_throw_an_exception_when_user_is_not_logged_in(self):
        self.assertRaises(UserNotLoggedInException,
                          self.tripService.getTripsByUser, TripServiceTest.UNUSED_USER, TripServiceTest.GUEST)

    def test_should_not_return_any_trips_when_users_are_not_friends(self):
        friend = UserBuilder.aUser().friendsWith(
            [TripServiceTest.ANOTHER_USER])\
            .withTrips([TripServiceTest.TO_BRAZIL]).build()
        trips = self.tripService.getTripsByUser(
            friend, TripServiceTest.REGISTERED_USER)
        self.assertEqual(len(trips), 0, "no trips")

    def test_should_return_friend_trips_when_users_are_friends(self):
        friend = UserBuilder.aUser()\
            .friendsWith([TripServiceTest.ANOTHER_USER, TripServiceTest.REGISTERED_USER])\
            .withTrips([TripServiceTest.TO_BRAZIL, TripServiceTest.TO_LONDON]).build()

        trips = self.tripService.getTripsByUser(
            friend, TripServiceTest.REGISTERED_USER)
        self.assertEqual(len(trips), 2, "two trips")

    GUEST = None
    UNUSED_USER = None
    REGISTERED_USER = User()
    ANOTHER_USER = User()
    TO_BRAZIL = Trip()
    TO_LONDON = Trip()


class TestableTripService(TripService):
    def findTripsByUser(self, user):
        return user.getTrips()
