class Tab:

    def __init__(self, input_guest):
        self.guest_name = input_guest.name
        self.bought_items = {}
        self.total_spent = 0
