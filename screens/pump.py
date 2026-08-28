from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button
from kivy.properties import StringProperty, NumericProperty, ObjectProperty

from calculator import MotorFormula # pump formula


class PumpAdjustButton(Button): # works univerally, test and debug
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


    def reset(self, instance=None): # Good to go
        self.ids.displacement_input.text = '' 
        self.ids.rpm_input.text = ''
        self.ids.pressure_input.text = ''
        self.ids.output_label.text = "Pump output flow: 0 \nHorsepower: 0 "

    def go_back(self, instance=None): # Good to go
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = "home"

    def calculate(self, instance=None): # needs calculator.py updated + internal logic
        return
        try:
            displacement = float(self.ids.displacement_input.text)
            rpm = float(self.ids.rpm_input.text)
            pressure = float(self.ids.pressure_input.text)


            if pressure == 0:
                self.ids.output_label.text = (
                    "Pump outlet flow: 0\n"
                    "Horsepower: 0"
                )
            
            calc = MotorFormula(
                displacement=displacement,
                rpm=rpm,
                pressure=pressure
            )

            torque = calc.motor_torque()
            motor_speed = calc.motor_speed()


            self.ids.output_label.text = (
                f"Motor torque: {torque:,.0f} ft-lbs.\n"
                f"Motor speed: {motor_speed:,.0f} rpm."
            )


        except ValueError:
            self.ids.output_label.text = (
                "Invalid input."
            )

        except ZeroDivisionError:
            self.ids.output_label.text = (
                    "Motor torque: 0\n"
                    "Motor speed: 0"
            )
