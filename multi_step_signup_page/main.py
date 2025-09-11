from kivymd.app import MDApp
from kivy.lang import Builder


KV = '''
MDFloatLayout:
    MDCard:
        size_hint: .45, .8
        pos_hint: {"center_x": .5, "center_y": .5}
        Carousel:
            MDFloatLayout:
                MDTextField:
                    hint_text: "First Name"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .48}
                MDTextField:
                    hint_text: "Last Name"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .36}
                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .2}
            MDFloatLayout:
                MDTextField:
                    hint_text: "Email address"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .48}
                MDTextField:
                    hint_text: "Phone Number"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .36}
                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x: .39
                    pos_hint: {"center_x": .3, "center_y": .2}
                MDRaisedButton:
                    text: "NEXT"
                    size_hint_x: .39
                    pos_hint: {"center_x": .7, "center_y": .2}
            MDFloatLayout:
                MDTextField:
                    hint_text: "Password"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .48}
                    password: True
                MDTextField:
                    hint_text: "Confirm Password"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .36}
                    password: True
                MDRaisedButton:
                    text: "PREVIOUS"
                    size_hint_x: .8
                    pos_hint: {"center_x": .5, "center_y": .2}
    MDLabel:
        text: "SignUp Form"
        bold: True
        pos_hint: {"center_x": .88, "center_y": .8}
        font_style: "H4"
    MDLabel:
        text: "Name"
        pos_hint: {"center_x": .808, "center_y": .7}
        font_style: "H6"
    MDIconButton:
        icon: "numeric-1-circle"
        pos_hint: {"center_x": .34, "center_y": .65}
        user_font_size: "35sp"
    MDProgressBar:
        size_hint_x: .1
        size_hint_y: None
        pos_hint: {"center_x": .42, "center_y": .65}
'''


class ProjectApp(MDApp):

    def build(self):
        kv = Builder.load_string(KV)
        return kv


if __name__ == '__main__':
    ProjectApp().run()
