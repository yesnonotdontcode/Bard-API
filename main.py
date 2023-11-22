import random
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.camera import Camera
import os
from android.permissions import request_permissions, Permission

# Запрашиваем разрешения на доступ к хранилищу файлов
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA])


class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Добавляем виджет камеры
        self.camera = Camera(play=False, index=1)  # Используйте index=1 для фронтальной камеры
        layout.add_widget(self.camera)

        # Добавляем кнопку для съемки фото
        btn_capture = Button(text='Сделать фото')
        btn_capture.bind(on_press=self.capture)
        layout.add_widget(btn_capture)

        return layout

    def capture(self, *args):

        photo_path = f'/storage/emulated/0/Pictures/{random.randint(0, 1000)}.png'
        self.camera.export_to_png(photo_path)
        print(f"Фото сохранено в {photo_path}")

if __name__ == '__main__':
    # Создаем и запускаем приложение
    CameraApp().run()