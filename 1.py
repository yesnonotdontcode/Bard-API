import re
from requests import post, get
from time import sleep
import threading

url = 'https://cautious-zebra-wr76wjg67p57297gj-5555.app.github.dev/'

user = input('Enter your username: ')

m = {
  'message': ''
}

def check_messages():
  while True:
    r_message = get(url + 'json')
    if r_message.text.replace('[', '').replace('"', '').replace(']','') == m['message']:
        pass
    else:
        print(r_message.text.replace('[', '').replace('"', '').replace(']',''))
        m['message'] = r_message.text.replace('[', '').replace('"', '').replace(']','')

def send_message():
  while True:
    user_message = input()#'Enter your message: ')
    response = post(url, json={'all_messages': f'{user}: {user_message}'})
    #print(re.sub(r'[\[\]" ,]', '', response.text))

# Создаем и запускаем потоки
send_message_thread = threading.Thread(target=send_message)
check_messages_thread = threading.Thread(target=check_messages)

check_messages_thread.start()
send_message_thread.start() 
