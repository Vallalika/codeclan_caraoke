import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.tab import Tab


class TestSong(unittest.TestCase):

    def setUp(self):
        self.one_headlight = Song("One Headlight","The Wallflowers","Rock")
    
    # @unittest.skip
    def test_set_up(self):
        self.assertEqual("One Headlight",self.one_headlight.name)
        self.assertEqual("The Wallflowers",self.one_headlight.artist)
        self.assertEqual("Rock",self.one_headlight.genre)
