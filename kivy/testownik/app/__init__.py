from kivy.app import App
from kivy.factory import Factory
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from menu import Menu
from quiz import Quiz

Builder.load_file('app/app.kv')

Factory.register('Quiz', cls=Quiz)
Factory.register('Menu', cls=Menu)


class SM(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return SM()
