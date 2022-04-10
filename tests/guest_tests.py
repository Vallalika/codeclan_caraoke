import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.item import Item

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Room 1", 3)
        self.lazy_song = Song("The Lazy Song", "Bruno Mars", "Pop")
        self.jane = Guest("Jane", 50.00, self.lazy_song)
        self.chips = Item("Chips", "Food", 4.00)
        self.gin_tonic = Item("Gin Tonic", "Drink", 6.00)
    
    def test_setup(self):
        self.assertEqual("Jane",self.jane.name)
        self.assertEqual(50.00,self.jane.money)
        self.assertEqual(self.lazy_song,self.jane.favourite_song)
        self.assertIsNone(self.jane.tab)
        self.assertEqual(False, self.jane.has_cheered)
    
    # @unittest.skip
    def test_pay_entry_fee(self):
        self.jane.pay_entry_fee(self.room_1)
        self.assertEqual(40.00, self.jane.money)


    # @unittest.skip
    def test_buy_item(self):
        self.jane.buy_item(self.chips)
        self.assertEqual(46.00, self.jane.money)
        

    # @unittest.skip
    def test_song_cheer(self):
        self.room_1.guest_checkin(self.jane)
        self.room_1.add_song(self.lazy_song)
        self.assertEqual("Jane: Yeaaaaaaaaaahhhhhh!!!!!!!!!!!!!!!!!!!!!!", self.jane.song_cheer())