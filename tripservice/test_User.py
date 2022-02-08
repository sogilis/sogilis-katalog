import unittest
from User import User

from UserBuilder import UserBuilder


class MyTestCase(unittest.TestCase):
    def test_users_are_not_friends(self):
        user = UserBuilder.aUser().friendsWith([MyTestCase.BOB]).build()
        self.assertFalse(user.isFriendsWith(
            MyTestCase.PAUL), "not friends with Paul")

    BOB = User()
    PAUL = User()

    def test_users_are_friends(self):
        pass


if __name__ == '__main__':
    unittest.main()
