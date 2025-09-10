import kivy
from kivy.app import StringProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition, ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder

Builder.load_file('story.kv')
Window.size = (320, 600)

class WindowManager(ScreenManager):
    '''A Window manager to manage switching between screens.'''


class MessageScreen(Screen):
    '''A Screen that display the stories and all message histories.'''

class StoryWithImage(MDBoxLayout):
    '''A horizontal layout with the user dp and the username'''
    text = StringProperty() # To store the user's name
    source = StringProperty() # The path of the story

class MainApp(MDApp):
    def build(self):
        '''Initialize the application
        an return the root widget.'''

        # Setting theme properties.
        self.theme_cls.theme_style = 'Dark' # Dark theme
        self.theme_cls.primary_palette = 'Teal' #Main color
        self.theme_cls.accent_palette = 'Teal' #Secondary color palette with 400 hue value
        self.theme_cls.accent_hue = '400'
        self.title = 'Whatsapp Redesign'

        # Storing the screens in a list
        screens = [
            MessageScreen(name='message')
        ]

        # Adding all screen in screens to the window manager
        self.wm = WindowManager(transition=FadeTransition()) # creating an instance of window manager and setting the animation when switching between screens
        for screen in screens:
            self.wm.add_widget(screen)

        # return the windon manager

        return self.wm


if __name__ == '__main__':
    MainApp().run()
