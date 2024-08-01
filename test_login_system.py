import unittest
from login_system import UserSystem

class TestUserSystem(unittest.TestCase):
    def setUp(self):
        self.user_system = UserSystem()

    def test_register_user(self):
        result = self.user_system.register_user("testuser", "testpassword")
        self.assertEqual(result, "User registered successfully")
        self.assertIn("testuser", self.user_system.users)

    def test_register_existing_user(self):
        self.user_system.register_user("testuser", "testpassword")
        with self.assertRaises(ValueError):
            self.user_system.register_user("testuser", "testpassword")

    def test_login_user(self):
        self.user_system.register_user("testuser", "testpassword")
        result = self.user_system.login_user("testuser", "testpassword")
        self.assertEqual(result, "User logged in successfully")

    def test_login_nonexistent_user(self):
        with self.assertRaises(ValueError):
            self.user_system.login_user("nonexistent", "password")

    def test_login_incorrect_password(self):
        self.user_system.register_user("testuser", "testpassword")
        with self.assertRaises(ValueError):
            self.user_system.login_user("testuser", "wrongpassword")

if __name__ == "__main__":
    unittest.main()
