import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.camera import Camera
from kivy.uix.button import Button
from kivy.uix.label import Label

class CameraApp(App):
    def build(self):
        # Create a BoxLayout to hold the camera and button
        layout = BoxLayout(orientation='vertical')

        # Create a Camera widget
        self.camera = Camera(resolution=(640, 480), play=True)
        self.text = Label(text='Photo will show there!')
        layout.add_widget(self.camera)
        layout.add_widget(self.text)

        # Create a button to capture the photo
        button = Button(text="Capture", size_hint=(None, None))
        button.bind(on_press=self.capture)
        layout.add_widget(button)

        return layout

    def capture(self, *args):
        # Capture the photo and save it to a file
        self.camera.export_to_png(f"storage/emulated/0/Pictures/{random.randint(1000)}.png")
        self.text = "Photo captured!"
        
CameraApp().run()