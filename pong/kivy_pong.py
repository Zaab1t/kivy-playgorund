from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            speedup = bounced * 1.1
            ball.velocity = speedup.x, speedup.y + offset


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel):
        self.ball.center = self.center
        self.ball.velocity = vel

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y

    def update(self, dt):
        self.ball.move()

        # ball hits paddle
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # ball hits bottom or top
        if self.ball.y < self.y or self.ball.top > self.top:
            self.ball.velocity_y *= -1

        # ball hits side, score!
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball((4, 0))
        if self.ball.x > self.width:
            self.player1.score += 1
            self.serve_ball((-4, 0))


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball(Vector(4, 0).rotate(randint(0, 360)))
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
