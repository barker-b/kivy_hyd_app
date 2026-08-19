from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button
from kivy.properties import StringProperty, NumericProperty, ObjectProperty


from calculator import MotorFormula


class MotorAdjustButton(Button):
    key = StringProperty()
    amount = NumericProperty()
    screen = ObjectProperty()

    def on_press(self):
        return
        
        # read and sanitize input
        raw = self.screen.ids[f"{self.key}_input"].text
        try:
            value = float(raw)
        except ValueError:
            value = 0
            self.screen.ids[f"{self.key}_input"].text = "0"

        new_value = value + self.amount

        # SAFETY 1: nothing below zero
        if new_value < 0:
            return

        # SAFETY 2: bore/rod cannot be zero
        if self.key in ("bore", "rod") and new_value == 0:
            return

        # SAFETY 3: rod cannot reach/exceed bore
        if self.key == "rod":
            try:
                bore = float(self.screen.ids["bore_input"].text or 0)
            except ValueError:
                bore = 0
                self.screen.ids["bore_input"].text = "0"

            if new_value >= bore:
                return

        # SAFETY 4: bore cannot go below rod
        if self.key == "bore":
            try:
                rod = float(self.screen.ids["rod_input"].text or 0)
            except ValueError:
                rod = 0
                self.screen.ids["rod_input"].text = "0"

            if new_value <= rod:
                return
        
        # formatting rules
        if self.key == "pressure":
            self.screen.ids[f"{self.key}_input"].text = f"{new_value:.0f}"
        else:
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


            if pressure == 0:
                self.ids.output_label.text = (
                    "Motor torque: 0\n"
                    "Motor speed: 0"
                )
            
            calc = MotorFormula(
                displacement=displacement,
                flow=flow,
                pressure=pressure
            )

            torque = None
            motor_speed = None

            self.ids.output_label.text = (
                f"Motor torque: {torque:,.0f} ft-lbs.\n"
                f"Motor speed: {motor_speed:,.0f} rpm."
            )


        except ValueError:
            self.ids.output_label.text = (
                "Invalid input."
            )
    