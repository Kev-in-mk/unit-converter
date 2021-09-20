from kivymd.app import MDApp

from kivy.core.window import Window
import math
from kivy.config import Config

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup

from kivy.uix.scrollview import ScrollView
from kivy.lang.builder import Builder
from kivy.properties import NumericProperty


Builder.load_file('kivy_lang.kv')

class ConverterWidget(GridLayout):

    int_button_width = 120
    int_button_height = 100
    int_button_font_size = 40

    button_width = NumericProperty(int_button_width)
    button_height = NumericProperty(int_button_height)
    button_font_size = NumericProperty(int_button_font_size)

    Window.size = (int_button_width * 4, int_button_height * 6)

    def euler(self, *args):
        self.ids.calc_input.text = self.ids.calc_input.text + str(math.e)

    def clear(self):
        self.ids.calc_input.text = ''

    def calc_error(self):
        # self.ids.calc_input.text = 'Its a popup'
        content = BoxLayout(orientation='vertical')
        scrollview = ScrollView()

        close_popup = Button(text='Close this popup')
        error_message = Label(text='This is Pi constant\n' + str(math.pi))

        scrollview.add_widget(error_message)
        content.add_widget(scrollview)
        content.add_widget(close_popup)

        popup = Popup(title='An error occurred', content=content, size_hint=(.8, .8))

        close_popup.bind(on_release=popup.dismiss)

        popup.open()

    def c_to_f(self):
        try:
            self.ids.calc_input.text = str(float(self.ids.calc_input.text) * (9 / 5) + 32)
        except:
            if self.ids.calc_input.text == '':
                self.ids.calc_input.text = 'No Input'

    def f_to_c(self):
        try:
            self.ids.calc_input.text = str((float(self.ids.calc_input.text) - 32) * (5 / 9))
        except:
            if self.ids.calc_input.text == '':
                self.ids.calc_input.text = 'No Input'
    def foot_to_cm(self):
        try:
            self.ids.calc_input.text = str(float(self.ids.calc_input.text) * 30.48)
        except:
            if self.ids.calc_input.text == '':
                self.ids.calc_input.text = 'No Input'
    def in_to_cm(self):
        try:
            self.ids.calc_input.text = str(float(self.ids.calc_input.text) * 2.54)
        except:
            if self.ids.calc_input.text == '':
                self.ids.calc_input.text = 'No Input'
    def mph_to_kmh(self):
        try:
            self.ids.calc_input.text = str(float(self.ids.calc_input.text) * 1.60934)
        except:
            if self.ids.calc_input.text == '':
                self.ids.calc_input.text = 'No Input'

    def oz_to_gr(self):
        try:
            self.ids.calc_input.text = str(float(self.ids.calc_input.text) * 28.35)
        except:
            if self.ids.calc_input.text == '':
                self.ids.calc_input.text = 'No Input'
    def gal_to_lit(self):
        try:
            self.ids.calc_input.text = str(float(self.ids.calc_input.text) * 3.785)
        except:
            if self.ids.calc_input.text == '':
                self.ids.calc_input.text = 'No Input'

class ConverterApp(MDApp):
    def build(self):
        self.title = 'Unit converter'
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'LightBlue'
        Config.set('graphics', 'resizable', '0')
        Config.write()
        return ConverterWidget()


if __name__ == '__main__':
    ConverterApp().run()