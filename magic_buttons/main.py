from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.behaviors.magic_behavior import MagicBehavior
from kivymd.uix.button import MDRaisedButton


magicbutton = '''
MDFloatLayout:  
    MagicButton:
        text: "Grow Effect"
        pos_hint: {"center_x": .5, "center_y": .6}
        on_release: self.grow()
    MagicButton:
        text: "Twist Effect"
        pos_hint: {"center_x": .5, "center_y": .5}
        on_release: self.twist()
    MagicButton:
        text: "Wobble Effect"
        pos_hint: {"center_x": .5, "center_y": .4}
        on_release: self.wobble()
    MagicButton:
        text: "Shake Effect"
        pos_hint: {"center_x": .5, "center_y": .3}
        on_release: self.shake()
'''


class MagicButton(MagicBehavior, MDRaisedButton):
    pass


class TutorialApp(MDApp):
    def build(self):
        magic_button = Builder.load_string(magicbutton)
        return magic_button


if __name__ == "__main__":
    TutorialApp().run()
