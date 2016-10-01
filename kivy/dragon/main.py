from kivy.app import App
from kivy.lang import Builder
from kivy.vector import Vector
from kivy.graphics import Line
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window


kv = '''
<DragonCurve>:
    Button:
        id: button
        background_color: 0, 0, 0, 1
    Slider:
        id: slider
        orientation: 'vertical'
        size_hint: None, .5
        center_x: root.w - 50
        y: root.h / 2 - 30
        min: 0
        max: 15
        step: 1
'''
Builder.load_string(kv)


def get_points(points, n=5):
    for _ in xrange(n):
        for i in xrange(1, 2 * len(points) - 1, 2):
            point = points[i - 1]
            nextp = points[i]
            vec = (nextp - point) / 2
            pnew = point + vec + vec.rotate(90) * ((i + 1) % 4 - 1)

            points.insert(i, pnew)
    return points


class DragonCurve(FloatLayout):
    w = Window.width
    h = Window.height
    side = min([w / 3 * 2, h])
    side -= 30

    def __init__(self, **kwargs):
        super(DragonCurve, self).__init__(**kwargs)

        self.ids.slider.bind(value=self.on_slider)
        self.ids.button.bind(on_press=self.on_button)

        self.points = [Vector(self.side / 3 + 30, self.side / 3 + 30),
                       Vector(self.side / 3 * 4 + 30, self.side / 3 + 30)]
        self.points = get_points(self.points, 15)

        self.lines = []
        for i in xrange(16):
            points = [self.points[i] for i in range(0, len(self.points), int((len(self.points) - 1) / (2 ** i)))]
            points = [j for i in points for j in i]
            self.lines.append(Line(points=points, width=1))

        self.canvas.add(self.lines[0])

        self.keyboard = Window.request_keyboard('', self, '')
        self.keyboard.bind(on_key_down=self.on_key)

    with_previous = False

    def draw(self):
        for i in xrange(16):
            self.canvas.remove(self.lines[i])
        if self.with_previous:
            for i in xrange(int(self.ids.slider.value) + 1):
                self.canvas.add(self.lines[i])
        else:
            self.canvas.add(self.lines[int(self.ids.slider.value)])

    def on_slider(self, instance, value):
        self.draw()

    def on_button(self, instance):
        self.with_previous = False if self.with_previous else True
        self.draw()

    def on_key(self, *args):
        key = args[1][0]
        val = self.ids.slider.value

        if key in (275, 276):
            self.on_button(self)
        elif key == 273 and val < 15:
            val += 1
        elif key == 274 and val > 0:
            val -= 1
        self.ids.slider.value = val


class DragonApp(App):
    def build(self):
        self.icon = 'ja.ico'
        return DragonCurve()


if __name__ == '__main__':
    DragonApp().run()