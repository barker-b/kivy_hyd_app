from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout


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

        mot_button = Button(text='Motor')
        mot_button.bind(on_press=self.go_to_mot_page)
        choice_layout.add_widget(mot_button)

        build_layout.add_widget(Label(text='Build'))


        root.add_widget(choice_layout)
        root.add_widget(build_layout)

        self.add_widget(root)

    def go_to_cyl_page(self, instance):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "cylinder"

    def go_to_mot_page(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "motor"