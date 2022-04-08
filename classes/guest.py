class Guest:
    
    def __init__(self, input_name, input_money, input_favourite_song):
        self.name = input_name
        self.money = input_money
        self.favourite_song = input_favourite_song
    
    def pay_entry_fee(self, room):
        if self.money >= room.entry_fee:
            self.money -= room.entry_fee