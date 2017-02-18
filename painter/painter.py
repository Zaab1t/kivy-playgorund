from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
from random import random


class Painter(App, Widget):
    def build(self):
        return self

    def on_touch_down(self, touch):
        with self.canvas:
            Color(random(), random(), random())
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


if __name__ == '__main__':
    Painter().run()
