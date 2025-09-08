from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.properties import NumericProperty

class Manager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Game(Screen):
    def on_enter(self, *args):
        Clock.schedule_interval(self.update, 1/30)

    def on_pre_enter(self, *args):
        self.ids.player.y = self.height / 2
        self.ids.player.speed = 0

    def update(self, *args):
        self.ids.player.speed += -self.height * 1/30
        self.ids.player.y += self.ids.player.speed * 1/30
        if self.ids.player.y > self.height or self.ids.player.y < 0:
            self.game_over()

    def on_touch_down(self, *args):
        self.ids.player.speed = self.height*0.7

    def game_over(self):
        Clock.unschedule(self.update, 1/30)
        App.get_running_app().root.current = 'game_over'

class Player(Image):
    speed = NumericProperty(0)

class GameOver(Screen):
    pass

class ArcBird(App):
    pass

ArcBird().run()
