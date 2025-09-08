from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty, ListProperty
from kivy.uix.widget import Widget
from kivy.animation import Animation
from random import random

class Manager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Game(Screen):

    obstacles = []

    def on_enter(self, *args):
        Clock.schedule_interval(self.update, 1/30)
        Clock.schedule_interval(self.put_obstacle, 1)

    def put_obstacle(self, *args):
        gap = self.height * 0.3
        position = (self.height - gap) * random()
        width = self.width * 0.05
        obstacle_low = Obstacle(x=self.width, height=position, width=width)
        obstacle_high = Obstacle(x=self.width, y=position + gap, height=self.height - position - gap, width=width)
        self.add_widget(obstacle_high,3)
        self.add_widget(obstacle_low,3)
        self.obstacles.append(obstacle_low)
        self.obstacles.append(obstacle_high)

    def on_pre_enter(self, *args):
        self.ids.player.y = self.height / 2
        self.ids.player.speed = 0

    def update(self, *args):
        self.ids.player.speed += -self.height * 2 * 1/30
        self.ids.player.y += self.ids.player.speed * 1/30
        if self.ids.player.y > self.height or self.ids.player.y < 0:
            self.game_over()
        elif self.player_collided():
            self.game_over()

    def on_touch_down(self, *args):
        self.ids.player.speed = self.height*0.7

    def game_over(self):
        Clock.unschedule(self.update, 1/30)
        Clock.unschedule(self.put_obstacle, 1)
        for ob in self.obstacles:
            ob.anim.cancel(ob)
            self.remove_widget(ob)
        self.obstacles = []
        App.get_running_app().root.current = 'game_over'

    def collided(self, widget1, widget2):
        if widget2.x <= widget1.x + widget1.width and \
            widget2.x + widget2.width >= widget1.x and \
            widget2.y <= widget1.y + widget1.height and \
            widget2.y + widget2.height >= widget1.y:
            return True
        return False

    def player_collided(self):
        collided = False
        for ob in self.obstacles:
            if self.collided(self.ids.player, ob):
                collided = True
                break

        return collided



class Player(Image):
    speed = NumericProperty(0)
    
class Obstacle(Widget):
    color = ListProperty([0.3, 0.2, 0.2, 1])

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anim = Animation(x=-self.width, duration=3)
        self.anim.bind(on_complete=self.vanish)
        self.anim.start(self)

    def vanish(self, *args):
        game_screen = App.get_running_app().root.get_screen('game')
        game_screen.remove_widget(self)
        game_screen.obstacles.remove(self)

class GameOver(Screen):
    pass

class ArcBird(App):
    pass

ArcBird().run()
