
import unittest
from app import client

class TestApp(unittest.TestCase):

  def test_connection(self):
    self.assertTrue(client)

if __name__ == '__main__':
  unittest.main()
