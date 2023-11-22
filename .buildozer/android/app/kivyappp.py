import requests
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.label import MDLabel
from kivy.clock import Clock
from threading import Thread

url = 'https://cautious-zebra-wr76wjg67p57297gj-5555.app.github.dev/'
m = {'message': ''}
session = requests.Session()

class MyApp(MDApp):
    def build(self):
        self.text_input = MDTextField(hint_text='Enter message', size_hint_y=None, height="36dp")
        self.text_name = MDTextField(hint_text='Enter your name', size_hint_y=None, height="36dp")

        self.label = MDLabel(text='PlAneGram', top=0.9, size_hint=(1, 0.1))
        self.output_label = MDLabel(text="Тут появится текст", size_hint_y=10, height=400)

        self.scroll_view = ScrollView()
        self.scroll_view.add_widget(self.output_label)

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        layout.add_widget(self.scroll_view)
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


app = MyApp()
app.run()
