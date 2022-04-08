import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        
        # Caraoke room
        self.room_1 = Room("Room 1", 3)
        
        # Songs
        self.one_headlight = Song("One Headlight", "The Wallflowers", "Rock")
        self.billie_jean = Song("Billie Jean", "Michael Jackson", "Pop")
        self.lazy_song = Song("The Lazy Song", "Bruno Mars", "Pop")
        self.living_on_a_prayer = Song("Living on a Prayer", "Bon Jovi", "Rock")

        # Guests
        self.jane = Guest("Jane", 50.00, self.lazy_song)
        self.gary = Guest("Gary", 30.00, self.one_headlight) 
        self.alison = Guest("Alison", 40.00, self.billie_jean)
        self.kerry = Guest("Kerry", 20.00, self.living_on_a_prayer)
        

    def test_setup(self):
        self.assertEqual("Room 1", self.room_1.name)
        self.assertEqual(3, self.room_1.capacity)
        self.assertEqual(0, self.room_1.number_of_guests_in)
    
    # @unittest.skip
    def test_check_in_if_enough_space(self):
        self.room_1.guest_checkin(self.jane)
        self.assertEqual(1, self.room_1.number_of_guests_in)
        self.room_1.guest_checkin(self.gary)
        self.room_1.guest_checkin(self.alison)
        self.assertEqual(3, self.room_1.number_of_guests_in)
        self.assertEqual(3, self.room_1.capacity)
        self.assertEqual(["Jane","Gary","Alison"], self.room_1.guest_list)
    
    # @unitest.skip
    def test_check_out_if_NOT_enough_space(self):
        # Adding in 3 guests, room capacity is 3
        self.room_1.guest_checkin(self.jane)
        self.room_1.guest_checkin(self.alison)
        self.room_1.guest_checkin(self.gary)

        # Trying to add a 4th guest
        self.assertEqual("Sorry, come back later!", self.room_1.guest_checkin(self.kerry))


    # @unittest.skip
    def test_check_in_if_enough_space_and_money(self):
        self.room_1.guest_checkin(self.jane)
        self.assertEqual(10.00,self.room_1.money_made)
        self.assertEqual(40.00,self.jane.money)
        self.assertEqual(1,self.room_1.number_of_guests_in)
        self.assertEqual(["Jane"],self.room_1.guest_list)

    # @unittest.skip
    def test_check_in_if_enough_space_but_NOT_enough_money(self):
        
        # Emptying Jane's wallet
        self.room_1.guest_checkin(self.jane)
        self.room_1.guest_checkin(self.jane)
        self.room_1.guest_checkin(self.jane)
        self.room_1.guest_checkin(self.jane)
        self.room_1.guest_checkin(self.jane)
        
        # Jane is now broke
        self.assertEqual("Sorry, come back later!", self.room_1.guest_checkin(self.jane))

    # @unittest.skip
    def test_check_in_if_NOT_enough_space_but_enough_money(self):
        
        self.room_1.guest_checkin(self.jane)
        self.room_1.guest_checkin(self.gary)
        self.room_1.guest_checkin(self.alison)
        
        # Room 1 now to full capacity, Kerry has enough money to pay the entry fee
        self.assertEqual("Sorry, come back later!", self.room_1.guest_checkin(self.kerry))


    # @unittest.skip
    def test_check_out(self):
        # Check in 3 guests
        self.room_1.guest_checkin(self.jane)
        self.room_1.guest_checkin(self.alison)
        self.room_1.guest_checkin(self.gary)

        # Check out guests
        self.room_1.guest_checkout(self.jane)
        self.assertEqual(2, self.room_1.number_of_guests_in)
        self.assertEqual(["Alison","Gary"], self.room_1.guest_list)
        self.room_1.guest_checkout(self.gary)
        self.room_1.guest_checkout(self.alison)
        self.assertEqual(0, self.room_1.number_of_guests_in)
        self.assertEqual(3, self.room_1.capacity)
        self.assertEqual([], self.room_1.guest_list)
    
    # unittest.skip
    def test_add_song(self):
        self.assertEqual([],self.room_1.playlist)
        self.room_1.add_song(self.one_headlight)
        self.room_1.add_song(self.billie_jean)
        self.assertEqual([self.one_headlight, self.billie_jean],self.room_1.playlist)
