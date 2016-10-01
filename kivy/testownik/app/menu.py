from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen


class LoadDialog(BoxLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Menu(Screen):
    def __init__(self, **kw):
        super(Menu, self).__init__(**kw)

        self.popup = Popup(title='Wybierz baze pytan:',
                           size_hint=(0.9, 0.9),
                           content=LoadDialog(load=self.load,
                                              cancel=self.dismiss_popup))

    def dismiss_popup(self):
        self.popup.dismiss()

    def open_popup(self):
        self.popup.open()

    def load(self, selection):
        if not selection:
            return

        self.manager.get_screen('quiz').set_base(selection[0])
        self.dismiss_popup()
