from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button

class AngleScreen(Screen):

    def go_back(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "cylinder"

