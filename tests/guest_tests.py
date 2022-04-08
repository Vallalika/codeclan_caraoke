import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.jane = Guest("Jane", 50.00)
        self.room_1 = Room("Room 1", 3)
    
    def test_setup(self):
        self.assertEqual("Jane",self.jane.name)
        self.assertEqual(50.00,self.jane.money)
    
    # @unittest.skip
    def test_pay_entry_fee(self):
        self.jane.pay_entry_fee(self.room_1)
        self.assertEqual(40.00, self.jane.money)


