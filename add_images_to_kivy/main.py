from kivymd.app import MDApp
from kivy.lang import Builder


image = '''
Image:
    source: "images/4.jpg"
    pos_hint: {"center_x": .5, "center_y": .5}
    size_hint: 1.9, 1.9
'''

class TutorialApp(MDApp):
    def build(self):
        images = Builder.load_string(image)
        return images


if __name__ == "__main__":
    TutorialApp().run()
