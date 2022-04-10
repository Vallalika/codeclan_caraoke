# import unittest
# from classes.guest import Guest
# from classes.room import Room
# from classes.song import Song
# from classes.tab import Tab

# class TestRoom(unittest.TestCase):
    
#     def setUp(self):
        
#         # Caraoke room
#         self.room_1 = Room("Room 1", 3)
        
#         # Songs
#         self.one_headlight = Song("One Headlight", "The Wallflowers", "Rock")
#         self.billie_jean = Song("Billie Jean", "Michael Jackson", "Pop")
#         self.lazy_song = Song("The Lazy Song", "Bruno Mars", "Pop")
#         self.living_on_a_prayer = Song("Living on a Prayer", "Bon Jovi", "Rock")

#         # Guests
#         self.jane = Guest("Jane", 50.00, self.lazy_song)
#         self.gary = Guest("Gary", 30.00, self.one_headlight)
#         self.alison = Guest("Alison", 40.00, self.billie_jean)
#         self.kerry = Guest("Kerry", 20.00, self.living_on_a_prayer)

#     def test_room_setup(self):
#         self.assertEqual("Room 1", self.room_1.name)
#         self.assertEqual(3, self.room_1.capacity)
#         self.assertEqual(0, self.room_1.number_of_guests_in)
