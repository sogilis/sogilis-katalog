import unittest

from UserBuilder import *


class MyTestCase(unittest.TestCase):
    def test_users_are_not_friends(self):
        user = aUser().friendsWith([MyTestCase.BOB]).build()
        self.assertFalse(user.isFriendsWith(MyTestCase.PAUL), "not friends with Paul")

    def test_users_are_friends(self):
        user = aUser().friendsWith([MyTestCase.PAUL, MyTestCase.BOB]).build()
        self.assertTrue(user.isFriendsWith(MyTestCase.BOB), "friends with Bob")

    BOB = User()
    PAUL = User()


if __name__ == '__main__':
    unittest.main()
