class Carpark:
    def __init__(self, capacity):
        self.spaces = []
        self.capacity = capacity

    def add_car(self, car_reg):
        self.spaces.append(car_reg)

    def is_duplicate(self, reg_num):
        for car in self.spaces:
            if car == reg_num:
                return True
        return False