from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '800')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens import HomeScreen, CylinderScreen, MotorScreen
import os
from kivy.lang import Builder

KV_PATH = os.path.join(os.path.dirname(__file__), "ui", "home.kv")
Builder.load_file(KV_PATH)

KV_PATH = os.path.join(os.path.dirname(__file__), "ui", "cylinder.kv")
Builder.load_file(KV_PATH)

KV_PATH = os.path.join(os.path.dirname(__file__), "ui", "motor.kv")
Builder.load_file(KV_PATH)




class Hydraulics(App):
    def build(self):


        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(CylinderScreen(name="cylinder"))
        sm.add_widget(MotorScreen(name="motor"))

        return sm

Hydraulics().run()
