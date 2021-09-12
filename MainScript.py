from tkinter.constants import CENTER
from vidstream import *
import tkinter as tk
import tkinter.ttk as ttk
import socket
import threading
from config import local_ip_address,public_ip_address


server = StreamingServer(local_ip_address,9999)
receiver = AudioReceiver(local_ip_address,8888)
socket.getaddrinfo('localhost', 8080)

def start_listening():
  t1 = threading.Thread(server.start_server).start()
  t2 = threading.Thread(receiver.start_server).start()

def start_camera_stream():
  camera_client = CameraClient(text_target_ip.get(1.0,'end-1c'),7777)
  t3 = threading.Thread(target=camera_client.start_stream).start()

def start_screen_sharing():
  screen_client = ScreenShareClient(text_target_ip.get(1.0,'end-1c'),7777)
  t4 = threading.Thread(target=screen_client.start_stream).start()

def start_audio_stream():
  audio_client = AudioSender(text_target_ip.get(1.0,'end-1c'),6666)
  t5 = threading.Thread(target=audio_client.start_stream).start()


# GUI
window = tk.Tk()
window.title('Private Network v0.0.1 Alpha')
window.geometry('300x200')


label_target_ip = tk.Label(window, text = 'Target IP Address')
label_target_ip.pack()

text_target_ip = tk.Text(window, height = 1)
text_target_ip.pack()

btn_listen = tk.Button(window, text = 'Start Listening',command=start_listening)
btn_listen.pack(anchor=CENTER, expand=True)

btn_camera = tk.Button(window, text = 'Start Camera Stream',command=start_camera_stream)
btn_camera.pack(anchor=CENTER, expand=True)

btn_screen = tk.Button(window, text = 'Start Screen Sharing',command=start_screen_sharing)
btn_screen.pack(anchor=CENTER, expand=True)

btn_audio = tk.Button(window, text = 'Start Audio Stream',command=start_audio_stream)
btn_audio.pack(anchor=CENTER, expand=True)

window.mainloop()
