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

class MotorFormula():
    def __init__(self, displacement, flow, pressure):
        self.displacement = displacement
        self.flow = flow
        self.pressure = pressure

    def motor_torque(self):
        return (self.pressure * self.displacement) / (2 * math.pi)

    def motor_speed(self):
        return 231 * self.flow / self.displacement
