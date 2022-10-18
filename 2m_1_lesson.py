class Car:
    def __init__(self, the_model, the_color, the_year, penalties=0.0):
        self.model = the_model
        self.color = the_color
        self.year = the_year
        self.penalties = penalties


bmw_car = Car("BMW X6", "Blue", 2020)
print(bmw_car)
