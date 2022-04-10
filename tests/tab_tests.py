import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.tab import Tab


class TestTab(unittest.TestCase):

    def setUp(self):
        self.jane = Guest("Jane", 50.00, self.lazy_song)
        self.janes_tab = Tab(self.jane)
    
    @unittest.skip
    def test_set_up(self):
        self.assertEqual(self.jane.name,self.janes_tab.name)
        self.assertEqual({},self.janes_tab.bought_items)
        self.assertEqual(0.00,self.janes_tab.total_spent)