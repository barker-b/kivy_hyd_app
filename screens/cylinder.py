from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from calculator import Formula

class CylinderScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation='vertical')

        self.bore_input = TextInput(
            hint_text="Bore size",

        )

        self.rod_input = TextInput(
            hint_text="Rod size",

        )

        self.pressure_input = TextInput(
            hint_text="Pressure (psi)",

        )

        self.output_label = Label(
            text=""
        )
        root.add_widget(self.bore_input)
        root.add_widget(self.rod_input)
        root.add_widget(self.pressure_input)
        root.add_widget(self.output_label)
        calculate = Button(text='Calculate')
        calculate.bind(on_press=self.button_click)
        back_button = Button(text='back')
        back_button.bind(on_press=self.go_back)
        root.add_widget(calculate)
        root.add_widget(back_button)
        

        self.add_widget(root)

    def go_back(self, instance):
        self.manager.current = "home"

    def button_click(self, instance):
        try:
            bore = float(self.bore_input.text)
            rod = float(self.rod_input.text)
            pressure = float(self.pressure_input.text)

            if rod >= bore:
                self.output_label.text = (
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

            self.output_label.text = (
                f"Push force: {push:.0f}\n"
                f"Pull force: {pull:.0f}"
            )


        except ValueError:
            self.output_label.text = (
                "Invalid input."
            )