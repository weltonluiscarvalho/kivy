import kivy
from kivy.properties import StringProperty, DictProperty, OptionProperty
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import FadeTransition, ScreenManager, Screen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from kivy.lang.builder import Builder
from demo.demo import profiles

Builder.load_file('story.kv')
Builder.load_file('chat_list_item.kv')
Window.size = (320, 600)

class WindowManager(ScreenManager):
    '''A Window manager to manage switching between screens.'''


class MessageScreen(Screen):
    '''A Screen that display the stories and all message histories.'''

class StoryWithImage(MDBoxLayout):
    '''A horizontal layout with the user dp and the username'''
    text = StringProperty() # To store the user's name
    source = StringProperty() # The path of the story
    
class ChatListItem(MDCard):
    '''A clickable chat item for the chat timeline'''
    mssg = StringProperty() # To store the user's mssg
    friend_avatar = StringProperty() # The path to the user's picture
    timestamp = StringProperty() #The time the message was sent
    profile = DictProperty() #A user demo.profile
    isRead = OptionProperty(None, options=['delivered', 'read', 'new', 'waiting']) #Message read status
    friend_name = StringProperty()

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

        self.story_builder()
        self.chat_list_builder()
        # return the windon manager

        return self.wm


    def story_builder(self):
        '''Create a story for each user and add it to the story layout'''
        for profile in profiles:
            self.story = StoryWithImage()
            self.story.text = profile['name']
            self.story.source = profile['image']
            self.wm.screens[0].ids['story_layout'].add_widget(self.story)

    def chat_list_builder(self):
        '''Create a chat list item for each user and add it to message list'''
        for profile in profiles:
            for message in profile['msg']:
                self.chatitem = ChatListItem()
                self.chatitem.profile = profile
                self.chatitem.friend_name = profile['name']
                self.chatitem.friend_avatar = profile['image']

                # Splitting the message content
                lastMessage, time, isRead, sender = message.split(';')
                self.chatitem.mssg = lastMessage
                self.chatitem.timestamp = time
                self.chatitem.isRead = isRead

            self.wm.screens[0].ids['chatTimeLine'].add_widget(self.chatitem)

if __name__ == '__main__':
    MainApp().run()
