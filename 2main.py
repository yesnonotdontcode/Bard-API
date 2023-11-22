import requests
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.clock import Clock
from threading import Thread

url = 'https://cautious-zebra-wr76wjg67p57297gj-5555.app.github.dev/'
m = {'message': ''}
session = requests.Session()

class MyApp(App):
    def build(self):
        self.text_input = TextInput(multiline=False, hint_text='Введите сообщение')
        self.text_name = TextInput(multiline=False, hint_text='Введите ваше имя')

        self.label = Label(text='PlAneGram', top=0.9, size_hint=(1, 0.1))
        self.output_label = TextInput(text="Тут появится текст", readonly=True, size_hint_y=10, height=400)

        scroll_view = ScrollView()
        scroll_view.add_widget(self.output_label)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        layout.add_widget(scroll_view)
        layout.add_widget(self.text_input)
        layout.add_widget(self.text_name)

        self.text_input.bind(on_text_validate=self.on_text_validate)

        Clock.schedule_interval(self.receive_message, 1)

        return layout

    def on_button_click(self, instance):
        entered_text = self.text_input.text
        name = self.text_name.text

        def post_message():
            response = session.post(url, json={'all_messages': f'{name}: {entered_text}'})
            self.text_input.text = ''

        thread = Thread(target=post_message)
        thread.start()

    def on_text_validate(self, instance):
        self.on_button_click(None)

    def receive_message(self, dt):
        def get_message():
            r_message = session.get(url + 'json')
            if r_message.text != m['message']:
                self.output_label.text = r_message.text
                m['message'] = r_message.text
            else:
                self.output_label.text = m['message']

        thread = Thread(target=get_message)
        thread.start()

if __name__ == '__main__':
    app = MyApp()
    app.run()
