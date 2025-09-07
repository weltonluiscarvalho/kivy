from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import NumericProperty, ObjectProperty, ReferenceListProperty, Widget
from kivy.vector import Vector

class PongPaddle(Widget):

    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset

class PongBall(Widget):

    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as 
    # a shorthand, just like e.g. w.pos for w.x and w.y 
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    # will be called in equal intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    button_pause = ObjectProperty(None)
    label_wins = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.button_pause.bind(on_press=self.on_press_pause_button)
        self.is_running = True

    def on_end_game(self, player):
        self.label_wins.text = f"player{player} wins the game"
        self.label_wins.opacity = 1.0
        self.ball.center = self.center
        self.is_running = False
        self.disable_childs()
        self.button_pause.text = "Start New Game"
        self.player2.score = 0
        self.player1.score = 0

    def disable_childs(self):
        self.ball_velocity = self.ball.velocity_x, self.ball.velocity_y
        self.ball.velocity = 0, 0
        self.button_pause.text = "Restart"

    def enable_childs(self):
        self.label_wins.opacity = 0.0
        self.ball.velocity = self.ball_velocity
        self.button_pause.text = "Pause"

    def on_press_pause_button(self, event):
        if self.is_running:
            self.is_running = False
            self.disable_childs()
        else:
            self.is_running = True
            self.enable_childs()

    def on_touch_move(self, touch):
        if touch.x < self.width/3:
            self.player1.center_y = touch.y 
        if touch.x > self.width - self.width/3:
            self.player2.center_y = touch.y 

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce off paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        # bounce off top and bottom
        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        # bounce off left and right
        # if (self.ball.x < 0) or (self.ball.right > self.width):
        #     self.ball.velocity_x *= -1

        # went off to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            if self.player2.score >= 3:
                self.on_end_game(2)
            else:
                self.serve_ball(vel=(4, 0))
        if self.ball.right > self.width:
            self.player1.score += 1
            if self.player1.score >= 3:
                self.on_end_game(1)
            else:
                self.serve_ball(vel=(-4, 0))

class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0/60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
