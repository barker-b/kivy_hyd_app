import os
import sys
from kivy.resources import resource_add_path

# 1. Add PyInstaller support for your pathing
if hasattr(sys, '_MEIPASS'):
    resource_add_path(sys._MEIPASS)
    # Force the script to treat the temporary extraction folder as its home directory
    os.chdir(sys._MEIPASS)

from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '800')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from screens import HomeScreen, CylinderScreen, MotorScreen, PumpScreen
from screens import FormulaScreen, AngleScreen
from kivy.lang import Builder

KV_PATH = os.path.join(os.path.dirname(__file__), "ui", "home.kv")
Builder.load_file(KV_PATH)

KV_PATH = os.path.join(os.path.dirname(__file__), "ui", "cylinder.kv")
Builder.load_file(KV_PATH)

KV_PATH = os.path.join(os.path.dirname(__file__), "ui", "motor.kv")
Builder.load_file(KV_PATH)

KV_PATH = os.path.join(os.path.dirname(__file__), "ui", "pump.kv")
Builder.load_file(KV_PATH)

KV_PATH = os.path.join(os.path.dirname(__file__), "ui", "formula.kv")
Builder.load_file(KV_PATH)

KV_PATH = os.path.join(os.path.dirname(__file__), "ui", "angles.kv")
Builder.load_file(KV_PATH)



class Hydraulics(App):
    def build(self):


        sm = ScreenManager()

        sm.add_widget(HomeScreen(name="home"))
        sm.add_widget(CylinderScreen(name="cylinder"))
        sm.add_widget(MotorScreen(name="motor"))
        sm.add_widget(PumpScreen(name="pump"))
        sm.add_widget(FormulaScreen(name="formula"))
        sm.add_widget(AngleScreen(name="angles"))

        return sm

Hydraulics().run()
