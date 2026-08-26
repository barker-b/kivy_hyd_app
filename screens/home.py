from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition



class HomeScreen(Screen):


    def go_to_cyl_page(self, instance):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "cylinder"

    def go_to_mot_page(self, instance):
        self.manager.transition = SlideTransition(direction='left')
        self.manager.current = "motor"

    def go_to_pump_page(self, instance):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = "pump"