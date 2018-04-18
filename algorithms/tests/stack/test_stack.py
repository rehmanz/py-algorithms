from unittest import TestCase
from algorithms.src.stack import push

class TestJoke(TestCase):
    def test_push(self):
        s = push()
        self.assertEqual(s, "Push something on the stack")