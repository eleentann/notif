from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window

from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton
import json
import requests

#Window.size = (310,500)

class Slope(MDApp):
    def build(self):
        self.screen_manager = ScreenManager()
        self.screen_manager.add_widget(Builder.load_file("main.kv"))
        return self.screen_manager

if __name__ == "__main__":
    Slope().run()