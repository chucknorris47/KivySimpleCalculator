from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from functools import partial
from tools.tools import Tools

MYNONE = ""
to = Tools()


class CalculatorWindow(GridLayout):

    def __init__(self, **kwargs):
        super(CalculatorWindow, self).__init__(**kwargs)
        self.cols = 6
        self.rows = 6

        """
            ERSTE ZEILE
        """
        self.add_widget(Label(text=MYNONE))
        self.add_widget(Label(text="Result"))

        self.result_tf = TextInput(password=False, multiline=False)

        # result textfield
        self.add_widget(self.result_tf)
        self.add_widget(Label(text=MYNONE))
        self.add_widget(Label(text=MYNONE))
        self.add_widget(Label(text=MYNONE))

        """
            ZWEITE ZEILE
        """
        self.ac_btn = Button(text='AC', font_size=28)
        self.ac_btn.bind(on_press=self.ac_btn_clicked)
        self.add_widget(self.ac_btn)

        self.one_btn = Button(text='1', font_size=28)
        self.one_btn.bind(on_press=partial(self.btn_clicked, input=self.one_btn.text))
        self.add_widget(self.one_btn)

        self.two_btn = Button(text='2', font_size=28)
        self.two_btn.bind(on_press=partial(self.btn_clicked, input=self.two_btn.text))
        self.add_widget(self.two_btn)

        self.three_btn = Button(text='3', font_size=28)
        self.three_btn.bind(on_press=partial(self.btn_clicked, input=self.three_btn.text))
        self.add_widget(self.three_btn)

        self.plus_btn = Button(text='+', font_size=28)
        self.plus_btn.bind(on_press=partial(self.btn_clicked, input=self.plus_btn.text))
        self.add_widget(self.plus_btn)

        self.enter_btn = Button(text='=', font_size=28)
        self.enter_btn.bind(on_press=self.result_btn_clicked)
        self.add_widget(self.enter_btn)

        """

            DRITTE ZEILE
        """

        self.add_widget(Label(text=MYNONE))
        # one button
        self.four_btn = Button(text='4', font_size=28)
        self.four_btn.bind(on_press=partial(self.btn_clicked, input=self.four_btn.text))
        self.add_widget(self.four_btn)

        self.five_btn = Button(text='5', font_size=28)
        self.five_btn.bind(on_press=partial(self.btn_clicked, input=self.five_btn.text))
        self.add_widget(self.five_btn)

        self.six_btn = Button(text='6', font_size=28)
        self.six_btn.bind(on_press=partial(self.btn_clicked, input=self.six_btn.text))
        self.add_widget(self.six_btn)

        self.minus_btn = Button(text='-', font_size=28)
        self.minus_btn.bind(on_press=partial(self.btn_clicked, input=self.minus_btn.text))
        self.add_widget(self.minus_btn)

        self.add_widget(Label(text=MYNONE))

        """
            VIERTE ZEILE
        """

        self.add_widget(Label(text=MYNONE))
        # one button
        self.seven_btn = Button(text='7', font_size=28)
        self.seven_btn.bind(on_press=partial(self.btn_clicked, input=self.seven_btn.text))
        self.add_widget(self.seven_btn)

        self.eight_btn = Button(text='8', font_size=28)
        self.eight_btn.bind(on_press=partial(self.btn_clicked, input=self.eight_btn.text))
        self.add_widget(self.eight_btn)

        self.nine_btn = Button(text='9', font_size=28)
        self.nine_btn.bind(on_press=partial(self.btn_clicked, input=self.nine_btn.text))
        self.add_widget(self.nine_btn)

        self.multi_btn = Button(text='*', font_size=28)
        self.multi_btn.bind(on_press=partial(self.btn_clicked, input=self.multi_btn.text))
        self.add_widget(self.multi_btn)

        self.add_widget(Label(text=MYNONE))

        """
        FUENFTE ZEILE
        """

        self.add_widget(Label(text=MYNONE))
        self.add_widget(Label(text=MYNONE))
        self.add_widget(Label(text=MYNONE))
        self.add_widget(Label(text=MYNONE))

        self.divi_btn = Button(text='/', font_size=28)
        self.divi_btn.bind(on_press=partial(self.btn_clicked, input=self.divi_btn.text))
        self.add_widget(self.divi_btn)

    def btn_clicked(self, instance, input):
        self.result_tf.text += input

    def ac_btn_clicked(self, instance):
        self.result_tf.text = MYNONE

    def result_btn_clicked(self, instance):
        current_input = self.result_tf.text.encode('ascii', 'ignore')
        expression_valid = to.is_expression_valid(current_input)
        if expression_valid is True:
            result = to.evaluate_complete_expression(current_input)
            self.result_tf.text = str(result[0])


class MyApp(App):

    def build(self):
        return CalculatorWindow()


if __name__ == '__main__':
    MyApp().run()
