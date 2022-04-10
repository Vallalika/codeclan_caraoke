import unittest
from classes.guest import Guest
from classes.room import Room
from classes.song import Song
from classes.tab import Tab
from classes.item import Item

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

        # Foods
        self.chips = Item("Chips", "Food", 4.00)
        self.gin_tonic = Item("Gin Tonic", "Drink", 6.00)

    def test_room_setup(self):
        self.assertEqual("Room 1", self.room_1.name)
        self.assertEqual(3, self.room_1.capacity)
        self.assertEqual(0, self.room_1.number_of_guests_in)
        self.assertEqual([], self.room_1.tab_list)
        self.assertEqual(10.00, self.room_1.entry_fee.price)
    
    # @unittest.skip
    def test_check_in_if_enough_space(self):

        self.room_1.guest_checkin(self.jane)
        self.assertEqual(1, self.room_1.number_of_guests_in)

        self.room_1.guest_checkin(self.gary)
        self.room_1.guest_checkin(self.alison)

        self.assertEqual(3, self.room_1.number_of_guests_in)
        self.assertEqual(3, self.room_1.capacity)

        self.assertEqual([self.jane,self.gary,self.alison], self.room_1.guest_list)

        # Checking tab list now contains jane's, gary's and alison's tabs
        self.assertEqual([self.jane.tab, self.gary.tab, self.alison.tab], self.room_1.tab_list)

        # Checking Jane's tab was updated
        self.assertEqual({"Entry Fee": 1}, self.jane.tab.bought_items)
    
    # @unitest.skip
    def test_check_in_if_NOT_enough_space(self):
        
        # Adding 3 guests, room capacity is 3
        self.room_1.guest_checkin(self.jane)
        self.room_1.guest_checkin(self.alison)
        self.room_1.guest_checkin(self.gary)

        # Trying to add 4th guest
        self.assertEqual("Sorry, come back later!", self.room_1.guest_checkin(self.kerry))

        # Checking tab list now contains jane's, alison's and gary's tabs
        self.assertEqual([self.jane.tab, self.alison.tab, self.gary.tab], self.room_1.tab_list)


    # @unittest.skip
    def test_check_in_if_enough_space_and_money(self):
        self.room_1.guest_checkin(self.jane)
        self.assertEqual(10.00,self.room_1.money_made)
        self.assertEqual(40.00,self.jane.money)
        self.assertEqual(1,self.room_1.number_of_guests_in)
        self.assertEqual([self.jane],self.room_1.guest_list)
        self.assertEqual([self.jane.tab], self.room_1.tab_list)

    # @unittest.skip
    def test_check_in_if_enough_space_but_NOT_enough_money(self):
        
        # Emptying Kerry's wallet
        self.room_1.guest_checkin(self.kerry)
        self.room_1.guest_checkout(self.kerry)
        self.room_1.guest_checkin(self.kerry)
        self.room_1.guest_checkout(self.kerry)

        # Checking room 1's variables are up to date
        self.assertEqual(20.00,self.room_1.money_made)
        self.assertEqual(0.00,self.kerry.money)
        self.assertEqual(0,self.room_1.number_of_guests_in)
        self.assertEqual([],self.room_1.guest_list)
        self.assertEqual([], self.room_1.tab_list)

        # Kerry is now broke
        self.assertEqual("Sorry, come back later!", self.room_1.guest_checkin(self.kerry))

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
        self.assertEqual([self.alison, self.gary], self.room_1.guest_list)
        self.assertEqual([self.alison.tab, self.gary.tab], self.room_1.tab_list)

        self.room_1.guest_checkout(self.gary)
        self.room_1.guest_checkout(self.alison)
        self.assertEqual(0, self.room_1.number_of_guests_in)
        self.assertEqual(3, self.room_1.capacity)
        self.assertEqual([], self.room_1.guest_list)
        self.assertEqual([], self.room_1.tab_list)
    
    # @unittest.skip
    def test_add_song(self):
        self.assertEqual([],self.room_1.playlist)
        self.room_1.add_song(self.one_headlight)
        self.room_1.add_song(self.billie_jean)
        self.assertEqual([self.one_headlight, self.billie_jean],self.room_1.playlist)
    
    # @unittest.skip
    def test_add_song_with_guest_cheer(self):

        # Test for song cheers where guests are already checked in and new song is added to playlist

        self.room_1.guest_checkin(self.jane)
        self.assertEqual("Jane: Yeaaaaaaaaaahhhhhh!!!!!!!!!!!!!!!!!!!!!!", self.room_1.add_song(self.lazy_song))
        self.room_1.guest_checkin(self.gary)
        self.assertEqual("Gary: Yeaaaaaaaaaahhhhhh!!!!!!!!!!!!!!!!!!!!!!", self.room_1.add_song(self.one_headlight))
    
    # @unittest.skip
    def test_check_in_with_guest_cheer(self):

        # Test for song cheers where guests are checking in and the song is already in the playlist

        self.room_1.add_song(self.lazy_song)
        self.room_1.add_song(self.one_headlight)
        self.assertEqual("Gary: Yeaaaaaaaaaahhhhhh!!!!!!!!!!!!!!!!!!!!!!", self.room_1.guest_checkin(self.gary))
    
        
    # @unittest.skip
    def test_clear_playlist(self):
        self.room_1.add_song(self.lazy_song)
        self.room_1.add_song(self.living_on_a_prayer)
        self.room_1.guest_checkin(self.kerry)
        self.room_1.clear_playlist()
        self.assertEqual([], self.room_1.playlist)
        self.assertEqual(False, self.kerry.has_cheered)
    
    # @unittest.skip
    def test_sell_item_enough_money(self):
        self.room_1.guest_checkin(self.jane)
        self.assertEqual({"Entry Fee": 1}, self.jane.tab.bought_items)
        self.room_1.sell_item(self.jane, self.chips)
        self.assertEqual(36.00, self.jane.money)
        self.assertEqual(14.00, self.room_1.money_made)
        self.assertEqual({"Entry Fee": 1, "Chips": 1}, self.jane.tab.bought_items)
        self.assertEqual(14.00, self.jane.tab.total_spent)
        self.assertEqual([self.jane.tab], self.room_1.tab_list)
    
    # @unittest.skip
    def test_sell_item_NOT_enough_money(self):
        self.room_1.guest_checkin(self.kerry)
        self.assertEqual({"Entry Fee": 1}, self.kerry.tab.bought_items)
        self.room_1.sell_item(self.kerry, self.gin_tonic)
        self.assertEqual(4.00, self.kerry.money)
        self.assertEqual(16.00, self.room_1.money_made)
        self.assertEqual({"Entry Fee": 1, "Gin Tonic": 1}, self.kerry.tab.bought_items)
        self.assertEqual(16.00, self.kerry.tab.total_spent)
        self.assertEqual([self.kerry.tab], self.room_1.tab_list)
        self.room_1.sell_item(self.kerry, self.gin_tonic)
        self.assertEqual(4.00, self.kerry.money)
        self.assertEqual(16.00, self.room_1.money_made)
        self.assertEqual({"Entry Fee": 1, "Gin Tonic": 1}, self.kerry.tab.bought_items)

    # @unittest.skip
    def test_tab_tracking_on_customer_check_out(self):
        self.room_1.guest_checkin(self.kerry)
        self.room_1.sell_item(self.kerry, self.gin_tonic)
        self.room_1.guest_checkout(self.kerry)
        self.assertIsNone(self.kerry.tab)