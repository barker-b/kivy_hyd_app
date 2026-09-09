from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button

class SectionButton(Button):
    pass


class HomeScreen(Screen):


    def go_to_cyl_page(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "cylinder"

    def go_to_mot_page(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "motor"

    def go_to_pump_page(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "pump"

    def go_to_formula_page(self):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "formula"