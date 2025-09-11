from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.lang import Builder
Window.size = (305, 400)

carrosa = '''
Carousel:
    MDFloatLayout:
        MDCard:
            size_hint: .9, .58
            pos_hint: {"center_x": .5, "center_y": .58}
            Image:
                source: "images/1.jpg"
        MDIconButton:
            icon: "facebook"
            user_font_size: "40sp"
            pos_hint: {"center_x": .3, "center_y": .2}
        MDIconButton:
            icon: "instagram"
            user_font_size: "40sp"
            pos_hint: {"center_x": .5, "center_y": .2}
        MDIconButton:
            icon: "youtube"
            user_font_size: "40sp"
            pos_hint: {"center_x": .7, "center_y": .2}
    MDFloatLayout:
        MDCard:
            size_hint: .9, .58
            pos_hint: {"center_x": .5, "center_y": .58}
            Image:
                source: "images/2.jpg"
        MDIconButton:
            icon: "facebook"
            user_font_size: "40sp"
            pos_hint: {"center_x": .3, "center_y": .2}
        MDIconButton:
            icon: "instagram"
            user_font_size: "40sp"
            pos_hint: {"center_x": .5, "center_y": .2}
        MDIconButton:
            icon: "youtube"
            user_font_size: "40sp"
            pos_hint: {"center_x": .7, "center_y": .2}
    MDFloatLayout:
        MDCard:
            size_hint: .9, .58
            pos_hint: {"center_x": .5, "center_y": .58}
            Image:
                source: "images/3.jpg"
        MDIconButton:
            icon: "facebook"
            user_font_size: "40sp"
            pos_hint: {"center_x": .3, "center_y": .2}
        MDIconButton:
            icon: "instagram"
            user_font_size: "40sp"
            pos_hint: {"center_x": .5, "center_y": .2}
        MDIconButton:
            icon: "youtube"
            user_font_size: "40sp"
            pos_hint: {"center_x": .7, "center_y": .2}
'''

class Project1App(MDApp):

    def build(self):
        return Builder.load_string(carrosa)


if __name__ == "__main__":
    app = Project1App()
    app.run()
