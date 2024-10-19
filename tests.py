import tkinter as tk
from turtle import width
from PIL import ImageGrab
import pyautogui
import threading
import time
from screeninfo import get_monitors

root = tk.Tk()
root.title("FDTD")
root.geometry("600x300")
root.configure(bg="#d4d4d4")
btn = tk.Button(root, text="Gerar CPF")
btn.pack(pady=20)
label = tk.Label(root,text="",width=10,height=4,border=2,borderwidth=3,relief="groove")
label.pack(pady=20)
def monitorar_cor_mouse():
    while True:
        x, y = pyautogui.position()
        screenshot = ImageGrab.grab()
        cor = screenshot.getpixel((x, y))
        cor_hex = '#%02x%02x%02x' % cor
        time.sleep(0.05)

def get_mouse_color():
    """Retorna a cor RGB do pixel sob o mouse, considerando múltiplos monitores."""
    while True:
        x,y = pyautogui.position()
        for monitor in get_monitors():
            if monitor.x <= x < monitor.x + monitor.width and monitor.y <= y < monitor.y + monitor.height:
                x -= monitor.x
                y -= monitor.y
                break
        screenshot = ImageGrab.grab(bbox=(monitor.x, monitor.y, monitor.x + monitor.width, monitor.y + monitor.height),all_screens=True)
        cor = screenshot.getpixel((x, y))
        cor_hex = '#%02x%02x%02x' % cor
        label.config(bg=cor_hex)

thread = threading.Thread(target=get_mouse_color)
thread.daemon = True
thread.start()
root.mainloop()
