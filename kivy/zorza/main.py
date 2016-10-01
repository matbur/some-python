from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.clock import Clock

from random import random as r

class Piece(Button):
    def __init__(self, **kwargs):
        super(Piece, self).__init__(**kwargs)

        self.id = kwargs['index']
        self.text = kwargs['index']

        self.set_color()

    def set_color(self):
        self.background_color = r(), r(), r(), 1



class Board(GridLayout):
    def __init__(self, **kwargs):
        super(Board, self).__init__(**kwargs)

        self.board = {}
        for y in xrange(6):
            for x in xrange(16):
                    self.board[cell(x,y)] = (Piece(index=cell(x,y)))
                    self.add_widget(self.board[cell(x, y)])

    def update(self, dt):
        for i in self.iterate():
            i.background_color = r(), r(), r(), 1


    def iterate(self):
        for i in self.children:
            yield i

    def get_cell(self, x, y):
        cell_id = cell(x, y)
        return self.board[cell_id]

def cell(x, y):
        return str(hex(x))[2:]+str(y)


class ZorzaApp(App):
    def build(self):
        b = Board()

        Clock.schedule_interval(b.update, .5)
        return b


if __name__ == '__main__':
    ZorzaApp().run()