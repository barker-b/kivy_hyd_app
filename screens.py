from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from calculator import Formula

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        root = BoxLayout(orientation='vertical')

        choice_layout = GridLayout(
            cols=2,
            padding=10,
            spacing=10
        )
        build_layout = GridLayout(
            cols=1,
            padding=10,
            spacing=10,

        )


        choice_layout.add_widget(Button(text='Pump'))
        choice_layout.add_widget(Button(text='Valve'))
        cyl_button = Button(text='Cylinder')
        cyl_button.bind(on_press=self.go_to_cyl_page)
        choice_layout.add_widget(cyl_button)
        choice_layout.add_widget(Button(text='Motor'))
        
        build_layout.add_widget(Label(text='Build'))

        widgets = [choice_layout, build_layout]

        for widget in widgets:
            root.add_widget(widget)

        self.add_widget(root)

    def go_to_cyl_page(self, instance):
        self.manager.current = "cylinder"



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
        root.add_widget(self.bore_input)
        root.add_widget(self.rod_input)
        root.add_widget(self.pressure_input)
        back_button = Button(text='back')
        back_button.bind(on_press=self.go_back)
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