from kivy.app import App
import math
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from screens import HomeScreen, CylinderScreen
from kivy.lang import Builder

Builder.load_file("ui/cylinder.kv")

class Hydraulics(App):
    def build(self):

        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(CylinderScreen(name="cylinder"))

        return sm

Hydraulics().run()
