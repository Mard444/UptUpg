import subprocess
import time
import schedule
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock

Window.size = (300, 100)
Window.clearcolor = (39 / 255, 35 / 255, 252 / 255, 1 / 255)


class Update(App):
    def build(self):
        box = BoxLayout()

        btn1 = Button(text="yes")
        btn1.bind(on_release=self.btn1_released)
        box.add_widget(btn1)

        btn2 = Button(text="no")
        btn2.bind(on_release=self.btn2_released)
        box.add_widget(btn2)

        return box

    def btn1_released(self, instance):
        subprocess.run(["sudo", "apt", "update"])
        subprocess.run(["sudo", "apt", "upgrade"])
        App.get_running_app().stop()

    def btn2_released(self, instance):
        self.root_window.hide() 
        delay = 5  
        Clock.schedule_once(self.show_window, delay)

    def show_window(self, dt):
        self.root_window.show()  



if __name__ == "__main__":
    Update().run()

