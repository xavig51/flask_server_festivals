import unittest
from app import client
from pymongo.mongo_client import MongoClient

class TestApp(unittest.TestCase):

  def test_connection(self):
  	self.assertEquals(type(client), MongoClient)
  	self.assertTrue(client)


if __name__ == '__main__':
  unittest.main()
