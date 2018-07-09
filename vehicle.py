class Vehicle():

    def __init__(self, v_type="vehicle"):
        self.name = "Vehicle"
        self.v_type = v_type
        self.is_transformed = False

    #Definition of a Vehicle

    def add_wheels(self, wheel_num):
        self.wheels = wheel_num

    def _add_rockets(self, num):
        self.rockets = num

    def transformerize(self, bot_name, rocket_num):
        self.wheels = 0
        self.is_transformed = True
        self._add_rockets = (rocket_num)
        self.bot_name = bot_name

    def __str__ (self):
        return f"This vehicles name is {self.name}"