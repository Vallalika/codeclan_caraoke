class Tab:

    def __init__(self, input_guest):
        self.guest_name = input_guest.name
        self.bought_items = {}
        self.total_spent = 0
    
    def add_to_tab(self, item):
        if item.name in self.bought_items.keys():
            self.bought_items[item.name] +=1
        else:
            self.bought_items[item.name] = 1