class Guest:
    
    def __init__(self, input_name, input_money, input_favourite_song):
        self.name = input_name
        self.money = input_money
        self.favourite_song = input_favourite_song
        self.has_cheered = False
        self.tab = None
    
    def pay_entry_fee(self, room):
        self.money -= room.entry_fee.price
    
    def buy_item(self, item):
        self.money -= item.price

    def song_cheer(self):
        return self.name+": Yeaaaaaaaaaahhhhhh!!!!!!!!!!!!!!!!!!!!!!"