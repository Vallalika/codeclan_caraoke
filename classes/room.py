from classes.item import Item
from classes.tab import Tab

class Room:

    def __init__(self, input_name, input_capacity):
        self.name = input_name
        self.capacity = input_capacity
        self.number_of_guests_in = 0
        self.guest_list = []
        self.tab_list = []
        self.money_made = 0.00
        self.entry_fee = Item("Entry Fee", "Service", 10.00)
        self.playlist = []
    
    def guest_checkin(self, guest):
        if (self.capacity > self.number_of_guests_in) and (guest.money >= self.entry_fee.price):
            self.number_of_guests_in += 1
            self.guest_list.append(guest)
            guest.tab = Tab(guest)
            guest.pay_entry_fee(self)
            self.money_made += self.entry_fee.price
            guest.tab.add_to_tab(self.entry_fee)
            self.tab_list.append(guest.tab)
            if guest.favourite_song in self.playlist:
                guest.has_cheered = True
                return guest.song_cheer()
        else:
            return "Sorry, come back later!"

    def guest_checkout(self, guest):
        self.number_of_guests_in -= 1
        self.guest_list.remove(guest)
        self.tab_list.remove(guest.tab)
        guest.tab = None
    
    def sell_item(self, guest, item):
        if guest.money >= item.price:
            guest.buy_item(item)
            self.money_made += item.price
            guest.tab.add_to_tab(item)


    def add_song(self, song):
        self.playlist.append(song)
        for guest in self.guest_list:
            if (guest.favourite_song in self.playlist) and (guest.has_cheered == False):
                guest.has_cheered = True
                return guest.song_cheer()
    
    def clear_playlist(self):
        self.playlist.clear()
        for guest in self.guest_list:
            guest.has_cheered = False