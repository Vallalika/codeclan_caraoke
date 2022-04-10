import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.tab import Tab
from classes.item import Item

class TestItem(unittest.TestCase):
    
    def setUp(self):
        
        self.entry_fee = Item("Entry fee", "Service", 10.00)
        self.chips = Item("Chips", "Food", 4.00)
        self.gin_tonic = Item("Gin Tonic", "Drink", 6.00)

    # @unittest.skip
    def test_setup(self):
        self.assertEqual("Entry fee", self.entry_fee.name)
        self.assertEqual("Service", self.entry_fee.type)
        self.assertEqual(10.00, self.entry_fee.price)