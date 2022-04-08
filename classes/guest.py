class Guest:
    
    def __init__(self, input_name, input_money):
        self.name = input_name
        self.money = input_money
    
    def pay_entry_fee(self, room):
        if self.money >= room.entry_fee:
            self.money -= room.entry_fee