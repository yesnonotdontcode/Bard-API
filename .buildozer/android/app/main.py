import random
import cv2
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.clock import Clock
import os
from android.permissions import request_permissions, Permission

# Запрашиваем разрешения на доступ к хранилищу файлов
request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE, Permission.CAMERA])


class CameraApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        # Создаем виджет для предварительного просмотра камеры (не видимого)
        self.capture = cv2.VideoCapture(1)  # Используйте 1 для фронтальной камеры
        _, frame = self.capture.read()

        # Создаем кнопку для съемки фото
        btn_capture = Button(text='Сделать фото')
        btn_capture.bind(on_press=self.capture_and_save)
        layout.add_widget(btn_capture)

        return layout

    def capture_and_save(self, *args):
        # Снимаем фото
        _, frame = self.capture.read()

        # Создаем уникальное имя файла с помощью временной метки
        timestamp = Clock.get_time()
        photo_path = f'/storage/emulated/0/Pictures/{random.randint(0, 1000)}.png'

        # Сохраняем фото
        cv2.imwrite(photo_path, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        print(f"Фото сохранено в {photo_path}")

if __name__ == '__main__':
    # Запускаем приложение
    CameraApp().run()

