from kivymd.app import MDApp
from kivy.lang import Builder

checkboxes = '''
MDFloatLayout:
    MDCheckbox:
        group: "group"
        pos_hint: {"center_x": .5, "center_y": .5}
        size_hint: .1, .1
        on_active: app.check(*args)
    MDCheckbox:
        group: "group"
        pos_hint: {"center_x": .6, "center_y": .5}
        size_hint: .1, .1
        on_active: app.check1(*args)
'''

class TutorialApp(MDApp):
    def build(self):
        checkbox = Builder.load_string(checkboxes)
        return checkbox

    def check(self, checkbox, active):
        if active:
            print("Hello")

    def check1(self, checkbox, active):
        if active:
            print("World")

if __name__ == "__main__":
    TutorialApp().run()
