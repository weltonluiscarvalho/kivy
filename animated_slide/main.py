from kivy.animation import Animation
from kivy.app import StringProperty
from kivy.clock import Clock
from kivy.core.text import LabelBase
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import StringProperty
from kivymd.uix.label import MDIcon
Window.size = (350, 600)


kv = '''
<SlideToActionButton>
    canvas.before:
        Color:
            rgba: 127/255, 0, 1, 0.3
        RoundedRectangle:
            size: self.size
            pos: self.pos
            radius: [10]
    size_hint: None, None
    height: lbl_ic.height + dp(16)
    width: lbl_txt.texture_size[0] + lbl_ic.width * 3.5
    MDLabel:
        id: lbl_txt
        text: root.text
        font_name: "Poppins"
        font_size: "15sp"
        pos_hint: {"center_x": .5, "center_y": .5}
        haling: "center"
        adaptive_size: True
        color: 1, 1, 1, 1
    Slider:
        id: slider
        size_hint_x: None
        width: root.width - dp(16)
        max: 203
        cursor_width: 0
        background_width: 0
        on_touch_move:
            lbl_txt.opacity = 1 - (self.value/self.max)
        on_touch_up:
            root.change_slider_pos(self)
    MDBoxLayout:
        id: box
        size_hint_x: None
        width: root.width - dp(16)
        MDIcon:
            id: lbl_ic
            icon: root.icon
            size_hint: None, None
            size: self.texture_size
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1
            pos_hint: {"center_y": .5}
            pos: (box.pos[0] + slider.value, box.pos[1] + dp(8))
            padding_x: "10dp"
            padding_y: "10dp"
            font_size: "22sp"
            canvas.before:
                Color:
                    rgb: 127/255, 0, 1
                RoundedRectangle:
                    size: self.size
                    pos: self.pos
                    radius: [5]
MDFloatLayout:
    md_bg_color: 127/255, 0, 1, .1
    SlideToActionButton:
        text: "Slide To Action"
        icon: "arrow-right"
        pos_hint: {"center_x": .5, "center_y": .12}
'''

class SlideToActionButton(AnchorLayout):
    text = StringProperty()
    icon = StringProperty()

    def change_slider_pos(self, slider):
        if round((slider.value/slider.max) * 100) < 60:
            anim_icon = Animation(pos=(self.ids.box.pos[0], self.ids.box.pos[1] + 8), duration=0.3)
            anim_icon.start(self.ids.lbl_ic)
            anim_lbl = Animation(opacity=1, duration=0.3)
            anim_lbl.start(self.ids.lbl_txt)
        else:
            anim_icon = Animation(pos=(self.ids.box.pos[0] + 202, self.ids.box.pos[1] + 8), duration=0.3)
            anim_icon.start(self.ids.lbl_ic)
            anim_lbl = Animation(opacity=0, duration=0.3)
            anim_lbl.start(self.ids.lbl_txt)
            Clock.schedule_once(self.remove_icon, .5)
            anim_back = Animation(duration=.5)
            anim_back += Animation(width=self.height, duration=.3)
            anim_back.start(self)
            check_icon = MDIcon(icon="check", 
                                halign="center", 
                                theme_text_color="Custom", 
                                text_color=(127/255, 0, 1), 
                                opacity=0)
            self.add_widget(check_icon)
            anim_check = Animation(duration=1)
            anim_check += Animation(opacity=1, duration=.3)
            anim_check.start(check_icon)


    def remove_icon(self, *args):
        self.remove_widget(self.ids.box)
        self.remove_widget(self.ids.slider)
        self.remove_widget(self.ids.lbl_txt)

class MainApp(MDApp):

    def build(self):
        return Builder.load_string(kv)


if __name__ == '__main__':
    LabelBase.register(name='Poppins', fn_regular='fonts/Poppins-Regular.otf')
    MainApp().run()
