import pyautogui
from screeninfo import get_monitors

while True:
    x,y = pyautogui.position()
    for monitor in get_monitors():
        if monitor.x <= x < monitor.x + monitor.width and monitor.y <= y < monitor.y + monitor.height:
            x -= monitor.x
            y -= monitor.y
            print(f"Mouse is at ({x}, {y}) on monitor {monitor.name}")
            break
