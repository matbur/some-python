from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window
from random import randint


class Helicopter(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    score = NumericProperty(0)

    def __init__(self, **kwargs):
        super(Helicopter, self).__init__(**kwargs)
        self.size = 50, 50

        self.img = Image(source='helicopter-128.png')
        self.img.size = self.size
        self.add_widget(self.img)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        self.update_image()

    def update_image(self):
        self.img.pos = self.pos


class Block(Widget):
    i = 0

    def __init__(self, **kwargs):
        super(Block, self).__init__(**kwargs)
        self.i = Block.i
        Block.i += 1

    def move(self, helicopter):
        self.pos[0] -= 1
        return self.collide_widget(helicopter)

    def __repr__(self):
        return '{}: ({}, {})'.format(self.i, self.x, self.y)


class MainGame(Widget):
    blocks = []
    w = Window.width
    h = Window.height
    helicopter = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(MainGame, self).__init__(**kwargs)
        self.size = self.w, self.h
        for _ in xrange(10):
            blocks = (Block(), Block())
            self.add_widget(blocks[0])
            self.add_widget(blocks[1])
            self.blocks.append(blocks)

    def start(self):
        self.helicopter.center = 100, self.height - 100
        self.helicopter.velocity = Vector(0, -3)
        self.helicopter.score = 0

        for blocks in self.blocks:
            blocks[0].x = 0

        for blocks in self.blocks:
            self.new_blocks(blocks)

    def update(self, dt):
        self.helicopter.move()

        if self.helicopter.top > self.height or self.helicopter.y < 0:
            self.start()

        for blocks in self.blocks:
            up, down = blocks
            if up.move(self.helicopter) or down.move(self.helicopter):
                self.start()
            if down.right < 0:
                self.helicopter.score += 1
                self.new_blocks(blocks)

    def new_blocks(self, blocks):
        offset = randint(250, 300)

        height = randint(100, self.height - 200)
        blocks[0].height = height
        blocks[1].height = self.height - height - randint(150, 300)

        max_ = self.get_max_x()
        blocks[0].x = max_ + offset
        blocks[1].x = max_ + offset
        blocks[1].top = self.height

    def get_max_x(self):
        return max([i[0].x for i in self.blocks] + [self.width - 300])

    def on_touch_down(self, touch):
        self.helicopter.velocity[1] *= -1

    def on_touch_up(self, touch):
        self.helicopter.velocity[1] *= -1


class MainApp(App):
    def build(self):
        game = MainGame()
        game.start()
        Clock.schedule_interval(game.update, 1 / 60.)
        return game


if __name__ == '__main__':
    MainApp().run()
