from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from calculator import Formula

class CylinderScreen(Screen):

    def reset(self, instance=None):
        self.ids.bore_input.text = '' 
        self.ids.rod_input.text = ''
        self.ids.pressure_input.text = ''
        self.ids.output_label.text = ''

    def go_back(self, instance=None):
        self.manager.current = "home"

    def calculate(self, instance=None):
        try:
            bore = float(self.ids.bore_input.text)
            rod = float(self.ids.rod_input.text)
            pressure = float(self.ids.pressure_input.text)

            if rod >= bore:
                self.ids.output_label.text = (
                    "Invalid, rod cannot be\n"
                    "The same or larger than bore"
                )  
                return
            
            calc = Formula(
                bore=bore,
                rod=rod,
                pressure=pressure
            )

            push = calc.cyl_ext_force()
            pull = calc.cyl_ret_force()

            self.ids.output_label.text = (
                f"Push force: {push:.0f}\n"
                f"Pull force: {pull:.0f}"
            )


        except ValueError:
            self.ids.output_label.text = (
                "Invalid input."
            )