import time
import requests
import threading
import kivy
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label

url = 'https://cautious-zebra-wr76wjg67p57297gj-5555.app.github.dev/'
m = {'message': ''}

class MyApp(App):
    def build(self):
        self.text_input = TextInput(multiline=False, hint_text='Enter The Message')
        self.text_name = TextInput(multiline=False, hint_text='Enter Your Name')

        self.label = Label(text='PlAneGram', top=0.9, size_hint=(1, 0.1))
        self.output_label = TextInput(text="Тут появится текст", readonly=True, size_hint_y=100, height=400)

        # Создаем ScrollView и добавляем output_label внутрь
        scroll_view = ScrollView()
        scroll_view.add_widget(self.output_label)

        # Добавляем ScrollView в ваш макет вместо output_label
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.label)
        layout.add_widget(scroll_view)
        layout.add_widget(self.text_input)
        layout.add_widget(self.text_name)

        # Добавим обработчик для события нажатия клавиши Enter на клавиатуре
        self.text_input.bind(on_text_validate=self.on_text_validate)

        return layout
    
    def on_button_click(self, instance):
        entered_text = self.text_input.text
        name = self.text_name.text
        response = requests.post(url, json={'all_messages': f'{name}: {entered_text}'})
        self.text_input.text = ''
    
    def on_text_validate(self, instance):
        self.on_button_click(None)

    def receive_message(self):
        while True:
            r_message = requests.get(url + 'json')
            if r_message.text == m['message']:
                pass
            else:
                self.output_label.text = r_message.text
                m['message'] = r_message.text
            time.sleep(1)

if __name__ == '__main__':
    app = MyApp()
    threading.Thread(target=app.receive_message, daemon=True).start()
    app.run()