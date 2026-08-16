from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '800')
 
from kivy.app import App
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
