from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

from calculator import PumpFormula

class PumpAdjustButton(Button):
    key = StringProperty()
    amount = NumericProperty()
    screen = ObjectProperty()
    
    def on_press(self):


        hint = self.screen.ids[f"{self.key}_input"].text
        try:
            value = float(hint)
        except ValueError:
            value = 0
            self.screen.ids[f"{self.key}_input"].text = "0"

        new_value = value + self.amount

        if new_value < 0:
            return
        
        self.screen.ids[f"{self.key}_input"].text = str(new_value)

        self.screen.calculate()


class PumpScreen(Screen):


    def reset(self, instance=None):
        self.ids.displacement_input.text = '' 
        self.ids.rpm_input.text = ''
        self.ids.pressure_input.text = ''
        self.ids.output_label.text = (
            "Pump output: 0 \n"
            "Horsepower: 0 \n"
            "Driving torque: 0"
            )

    def go_back(self, instance=None):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "home"

    def calculate(self, instance=None):
        try:
            displacement = float(self.ids.displacement_input.text)
            rpm = float(self.ids.rpm_input.text)
            pressure = float(self.ids.pressure_input.text)

            calc = PumpFormula(
                displacement=displacement,
                rpm=rpm,
                pressure=pressure
            )

            pump_flow = calc.output_flow()
            horse_power = calc.horse_power()
            torque = calc.torque()


            self.ids.output_label.text = (
                f"Pump output: {pump_flow:,.0f} GPM.\n"
                f"Pump horsepower: {horse_power:,.0f} HP.\n"
                f"Driving torque: {torque:.0f} ft-lbs."
            )


        except ValueError:
            self.ids.output_label.text = (
                "Invalid input."
            )
