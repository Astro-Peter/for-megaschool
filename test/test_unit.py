import unittest
from src.main import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(id=1, name='John Doe', email='johndoe@example.com')
        self.assertEqual(user.id, 1)
        self.assertEqual(user.name, 'John Doe')
        self.assertEqual(user.email, 'johndoe@example.com')

if __name__ == '__main__':
    unittest.main()