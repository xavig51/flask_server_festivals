
import unittest
from app import hello

class TestHelloApp(unittest.TestCase):

  def test_hello(self):
    self.assertEqual(hello(), "primer despligue simple\n")

if __name__ == '__main__':
  unittest.main()
