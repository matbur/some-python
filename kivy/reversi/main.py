from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class Piece(Button):
    augmenter = 0

    def __init__(self, **kwargs):
        super(Piece, self).__init__(**kwargs)

        self.nr = self.augmenter
        Piece.augmenter += 1


class Empty(Piece):
    pass


class Disk(Piece):
    pass


class White(Disk):
    pass


class Black(Disk):
    pass


class Scores(BoxLayout):
    pass


class Whites(Scores):
    pass


class Blacks(Scores):
    pass


class Buttons(Button):
    pass


class NewGame(Buttons):
    pass


class RightButtons(BoxLayout):
    pass


class Undo(Buttons):
    pass


class Redo(Buttons):
    pass


class Game(GridLayout):
    players = (White, Black)

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)

        self.player = 1
        self.blacks = 0
        self.whites = 0
        self.moves = 0
        self.board = []

        self.new_game()

    def new_game(self):
        for i in xrange(100):
            if i in (0, 9, 90):
                wid = ''
            elif 0 < i < 9 or 90 < i < 99:
                wid = Label(text='abcdefgh'[i % 10 - 1])
            elif i % 10 in (0, 9):
                wid = Label(text=str(9 - i / 10))
            else:
                wid = Empty(text='')  # str(i-i/10*2-9))
                wid.bind(on_press=self.move)
            self.board.append(wid)

        self.board[90] = NewGame()
        self.board[90].bind(on_press=self.new)

        self.board[99] = RightButtons()
        self.board[99].ids.undo.on_press = self.undo
        self.board[99].ids.redo.on_press = self.redo

        self.board[0] = Whites()
        self.board[9] = Blacks()

        self.board[44] = White()
        self.board[45] = Black()
        self.board[54] = Black()
        self.board[55] = White()

        self.apply_changes()

    def apply_changes(self):
        self.clear_widgets()

        self.whites = len(filter(lambda x: isinstance(x, White), self.board))
        self.blacks = len(filter(lambda x: isinstance(x, Black), self.board))

        self.board[0].ids.white.text = str(self.whites)
        self.board[9].ids.black.text = str(self.blacks)

        for i in self.board:
            self.add_widget(i)

    def move(self, instance):
        nr = instance.nr + instance.nr / 8 * 2 + 11
        board = self.board
        player = self.player
        players = self.players
        to_change = []
        directions = (-11, -10, -9, -1, 1, 9, 10, 11)
        for (j, k) in enumerate(directions):
            to_change.append([])
            for i in xrange(1, 8):
                n = nr + i * k
                if i == 7 or not isinstance(board[n], Disk):
                    del to_change[j][:]
                    break
                elif isinstance(board[n], players[not player]):
                    to_change[j].append(n)
                elif isinstance(board[n], players[player]):
                    if to_change[j]:
                        to_change[j].append(nr)
                    break

        for i in to_change:
            for j in i:
                board[j] = players[player]()
        if any(to_change):
            self.player = not player
        self.apply_changes()

    def new(self, instance):
        Piece.augmenter = 0
        self.__init__()

    def undo(self):
        print 'undo'

    def redo(self):
        print 'redo'


class Square(AnchorLayout):
    pass


class ReversiApp(App):
    def build(self):
        self.icon = 'icon.ico'
        self.title = 'Reversi / Othello'
        return Square()


if __name__ == '__main__':
    ReversiApp().run()