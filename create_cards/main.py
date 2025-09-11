from kivymd.app import MDApp
from kivy.lang import Builder

Card = '''
MDFloatLayout:
    MDCard:
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: .5, .5
        md_bg_color: 0, 0, 0, 1
        MDLabel:
            text: "Welcome To"
            halign: "center"
            pos_hint: {"center_y": .7}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            font_style: "H4"
    MDLabel:
        text: "Arcturus"
        halign: "center"
        pos_hint: {"center_y": .52}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H5"
    MDIconButton:
        icon: "facebook"
        pos_hint: {"center_x": .5, "center_y": .4}
        user_font_size: "40sp"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
    MDIconButton:
        icon: "instagram"
        pos_hint: {"center_x": .4, "center_y": .4}
        user_font_size: "40sp"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
    MDIconButton:
        icon: "twitter"
        pos_hint: {"center_x": .6, "center_y": .4}
        user_font_size: "40sp"
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
'''

class TutorialApp(MDApp):
    def build(self):
        card = Builder.load_string(Card)
        return card


if __name__ == "__main__":
    TutorialApp().run()
