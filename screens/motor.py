from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

from calculator import MotorFormula

class MotorAdjustButton(Button):
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


class MotorScreen(Screen):


    def reset(self, instance=None):
        self.ids.displacement_input.text = '' 
        self.ids.flow_input.text = ''
        self.ids.pressure_input.text = ''
        self.ids.output_label.text = 'Motor torque: 0\nMotor speed: 0'

    def go_back(self, instance=None):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "home"

    def calculate(self, instance=None):
        try:
            displacement = float(self.ids.displacement_input.text)
            flow = float(self.ids.flow_input.text)
            pressure = float(self.ids.pressure_input.text)

            
            calc = MotorFormula(
                displacement=displacement,
                flow=flow,
                pressure=pressure
            )

            torque = calc.motor_torque()
            motor_speed = calc.motor_speed()


            self.ids.output_label.text = (
                f"Motor torque: {torque:,.0f} ft-lbs.\n"
                f"Motor speed: {motor_speed:,.0f} RPM."
            )


        except ValueError:
            self.ids.output_label.text = (
                "Invalid input."
            )

        except ZeroDivisionError:
            self.ids.output_label.text = (
                    "Motor torque: 0 ft-lbs.\n"
                    "Motor speed: 0 RPM."
            )
