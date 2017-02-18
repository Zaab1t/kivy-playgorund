from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginScreen(App, GridLayout):
    def build(self):
        return self

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1

        username_row = BoxLayout(orientation='horizontal')
        username_row.add_widget(Label(text='Username'))
        username_row.add_widget(TextInput(multiline=False))

        password_row = BoxLayout(orientation='horizontal')
        password_row.add_widget(Label(text='Password'))
        password_row.add_widget(TextInput(password=True, multiline=False))

        self.add_widget(username_row)
        self.add_widget(password_row)
        self.add_widget(Button(text='Sign in!'))


if __name__ == '__main__':
    LoginScreen().run()
