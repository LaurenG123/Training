from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp


class RomanToIntegerApp(App):
    def build(self):
        self.title = 'Roman Numeral to Integer Converter'

        # Main layout
        layout = BoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))

        # Header label
        header_label = Label(
            text='Roman Numeral to Integer Converter',
            font_size=24,
            bold=True,
            color=(0, 0.5, 1, 1),  # Blue color
            size_hint_y=None,
            height=dp(50)
        )

        # Input field
        self.input_field = TextInput(
            hint_text='Enter Roman Numeral',
            font_size=50,
            size_hint_y=None,
            height=dp(100),
            multiline=False,
            write_tab=False
        )

        # Convert button
        convert_button = Button(
            text='Convert',
            font_size=50,
            size_hint_y=None,
            height=dp(100),
            background_color=(0, 0.7, 0, 1)  # Green color
        )
        convert_button.bind(on_release=self.convert_roman)

        # Result label
        self.result_label = Label(
            text='',
            font_size=200,
            bold=True,
            color=(1, 1, 1, 1),  # Black color
            size_hint_y=None,
            height=dp(50)
        )

        # Add widgets to the layout
        layout.add_widget(self.result_label)
        layout.add_widget(header_label)
        layout.add_widget(self.input_field)
        layout.add_widget(convert_button)


        return layout

    def convert_roman(self, instance):
        roman_numeral = self.input_field.text
        integer_value = self.roman_to_integer(roman_numeral)
        self.result_label.text = f'{integer_value}'

    def roman_to_integer(self, s):
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
        int_val = 0

        for i in range(len(s)):
            if i > 0 and roman_dict[s[i]] > roman_dict[s[i - 1]]:
                int_val += roman_dict[s[i]] - 2 * roman_dict[s[i - 1]]
            else:
                int_val += roman_dict[s[i]]

        return int_val


if __name__ == '__main__':
    RomanToIntegerApp().run()

