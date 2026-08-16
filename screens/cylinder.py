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

        window = BoxLayout(orientation = 'horizontal')


       
        left_side = BoxLayout(orientation='vertical')

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
        calculate = Button(text='Calculate')
        calculate.bind(on_press=self.calculate)

        back_button = Button(text='back')
        back_button.bind(on_press=self.go_back)

        reset_button = Button(text='reset')
        reset_button.bind(on_press=self.reset)



        left_side.add_widget(self.bore_input)
        left_side.add_widget(self.rod_input)
        left_side.add_widget(self.pressure_input)
        left_side.add_widget(self.output_label)
        left_side.add_widget(calculate)
        left_side.add_widget(reset_button)
        left_side.add_widget(back_button)
                

        buttons = BoxLayout(orientation='vertical')

        bore_up_button = Button(text='up')
        bore_down_button = Button()
        rod_up_button = Button()
        rod_down_button = Button()
        pressure_up_button = Button()
        pressure_down_button = Button()





        buttons.add_widget(bore_up_button)
        buttons.add_widget(bore_down_button)
        buttons.add_widget(rod_up_button)
        buttons.add_widget(rod_down_button)
        buttons.add_widget(pressure_up_button)
        buttons.add_widget(pressure_down_button)

        window.add_widget(left_side)
        window.add_widget(buttons)

        self.add_widget(window)

    def reset(self, instance):
        self.bore_input.text = '' 
        self.rod_input.text = ''
        self.pressure_input.text = ''
        self.output_label.text = ''

    def go_back(self, instance):
        self.manager.current = "home"

    def calculate(self, instance):
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