from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.button import Button

class FormulaScreen(Screen):

    def go_back(self, instance=None):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = "home"
