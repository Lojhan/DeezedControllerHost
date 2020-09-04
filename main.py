from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib
import keyboard
import wmi
import subprocess
from win32 import win32gui
import qrcode
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import time 
from keyboard import mouse
import socket
import ctypes
import webbrowser
# Text segmentation 
import cv2
import numpy as np
import pyscreenshot as ImageGrab

# grab fullscreen


image = cv2.imread(r'C:\Users\Vinic\Desktop\Capturar.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
sharpen_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen = cv2.filter2D(gray, -1, sharpen_kernel)
thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
result = 255 - close

cv2.imshow('sharpen', sharpen)
cv2.imshow('thresh', thresh)
cv2.imshow('close', close)
cv2.imshow('result', result)
cv2.waitKey()


user32 = ctypes.windll.user32
height = user32.GetSystemMetrics(1)
width = user32.GetSystemMetrics(0)
print(height)

firstWidth = 0
firstHeight = 0

secondWidth = 0
secondHeight = 0

if height == 720:
    firstWidth = 0.32
    firstHeight = 0.281
    secondWidth = 0.32
    secondHeight = 0.600
elif height == 1080:
    firstWidth = 0.236
    firstHeight = 0.187
    secondWidth = 0.236
    secondHeight = 0.40
elif height == 1440:
    firstWidth = 0.30
    firstHeight = 0.15
    secondWidth = 0.30
    secondHeight = 0.30


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

ip = get_ip_address()
print(ip)

img = qrcode.make(ip)
img.show()

DeezerWindow = 0

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    
    for i in top_windows:
        if "Deezer" in i[1]:
            DeezerWindow = i[0]
            print(i)
            # win32gui.SetForegroundWindow(DeezerWindow)

HOST_ADDRESS = ""
HOST_PORT = 8000

class RequestHandler(BaseHTTPRequestHandler):
    
    def send_response(self, code, message=None):
        # self.log_request(code)
        self.send_response_only(code)
        self.send_header('Server','python3 http.server Development Server')     
        self.send_header('Date', self.date_time_string())
        self.end_headers()  
    
    def open_deezer():
        win32gui.ShowWindow(DeezerWindow,3)
        win32gui.SetForegroundWindow(DeezerWindow)
        mouse.move(100, 100)
        mouse.click()
    
    def do_GET(self):
        self.send_response(200, message='OK')
        
        if self.path == '/control':
            
            self.send_response(200, message='OK')
            control = self.headers._headers[0][1]

            if control == 'resume':
                keyboard.send('play/pause media')  
            elif control == 'volup':       
                keyboard.send('volume up') 
            elif control == 'bfrtrack':
                keyboard.send('previous track') 
            elif control == 'voltar':   
                RequestHandler.open_deezer()
                keyboard.send('ctrl+left') 
            elif control == 'avancar':     
                RequestHandler.open_deezer()
                keyboard.send('ctrl+right') 
            elif control == 'nxttrack':
                keyboard.send('next track') 
            elif control == 'voldown':
                keyboard.send('volume down') 
            elif control == 'mute':
                keyboard.send('volume mute')
            elif control == 'repeat':
                RequestHandler.open_deezer()
                keyboard.send('r')
            elif control == 'like':
                RequestHandler.open_deezer()
                keyboard.send('l')
            elif control == 'open':
                RequestHandler.open_deezer()
            elif control == '0.0':
                RequestHandler.open_deezer()
                keyboard.send('0')
            elif control == '1.0':
                RequestHandler.open_deezer()
                keyboard.send('1') 
            elif control == '2.0':
                RequestHandler.open_deezer()
                keyboard.send('2') 
            elif control == '3.0':
                RequestHandler.open_deezer()
                keyboard.send('3') 
            elif control == '4.0':
                RequestHandler.open_deezer()
                keyboard.send('4') 
            elif control == '5.0':
                RequestHandler.open_deezer()
                keyboard.send('5') 
            elif control == '6.0':
                RequestHandler.open_deezer()
                keyboard.send('6') 
            elif control == '7.0':
                RequestHandler.open_deezer()
                keyboard.send('7') 
            elif control == '8.0':
                RequestHandler.open_deezer()
                keyboard.send('8')
            elif control == '9.0':
                RequestHandler.open_deezer()
                keyboard.send('9')
            elif control == 'openweb':       
                webbrowser.open('http://deezer.com')  

        if self.path == '/search':
            
            self.send_response(200, message='OK')
            print('open')
            control = self.headers._headers[0][1]
            RequestHandler.open_deezer()
            keyboard.send('S') 
            keyboard.send('ctrl+a') 
            keyboard.send('backspace') 
            keyboard.write(control)
            keyboard.send('enter') 
            time.sleep(2)
            mouse.move(width*firstWidth, height*firstHeight)
            mouse.click()
            mouse.move(width*secondWidth, height*secondHeight)
            mouse.click()

            
        self.send_response(200, message='OK')
 
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = (HOST_ADDRESS, HOST_PORT)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

if __name__ == '__main__':
    run(handler_class=RequestHandler)


