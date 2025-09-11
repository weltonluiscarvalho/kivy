from kivymd.app import MDApp
from kivy.lang import Builder


textfield = '''
MDTextField:
    hint_text: "Enter Your Name"
    pos_hint: {"center_x": .5, "center_y": .5}
    size_hint_x: .5
    mode: "fill"
'''

class TutorialApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Red"
        text_field = Builder.load_string(textfield)
        return text_field


if __name__ == "__main__":
    TutorialApp().run()
