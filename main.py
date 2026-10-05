from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


class CalculatorApp(App):

    def build(self):
        main = BoxLayout(orientation="vertical")

        self.screen = TextInput(
            font_size=40,
            readonly=True,
            halign="right",
            multiline=False
        )

        main.add_widget(self.screen)

        buttons = GridLayout(cols=4)

        for text in [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]:
            button = Button(
                text=text,
                font_size=30
            )

            button.bind(
                on_press=self.button_pressed
            )

            buttons.add_widget(button)

        main.add_widget(buttons)

        return main

    def button_pressed(self, button):
        value = button.text

        if value == "=":
            try:
                result = eval(self.screen.text)
                self.screen.text = str(result)
            except:
                self.screen.text = "Error"

        else:
            self.screen.text += value


CalculatorApp().run()