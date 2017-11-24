import unittest
import dog

class TestDogfood(unittest.TestCase):


    def test_can_a_dog_eat_alcohol(self):
        assert "No, a dog must not eat alcohol" in dog.can_eat("alcohol")


    def test_can_a_dog_eat_kibbles(self):
        assert "Yes, a dog can eat kibbles" in dog.can_eat("kibbles")
