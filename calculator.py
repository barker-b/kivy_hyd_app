import math

class CylFormula():
    def __init__(self, bore, rod, pressure):
        self.bore = bore
        self.rod = rod
        self.pressure = pressure

    def piston_area(self):
        return math.pi * self.bore**2 / 4

    def annulus(self):
        return math.pi * self.bore**2 / 4 - math.pi * self.rod**2 / 4

    def cyl_ext_force(self):
        return self.pressure * self.piston_area()

    def cyl_ret_force(self):
        return self.pressure * self.annulus()