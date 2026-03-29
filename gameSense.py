import pyautogui
import time

pyautogui.time.sleep(3)

frame = 0

while "Dino running":
    frame += 1
    last_time = time.time()
    x, y = pyautogui.position()
    rgb = pyautogui.pixel(x,y)

    brightness = ( rgb.red + rgb.green + rgb.blue ) /3

    if brightness < 128:
        pyautogui.hotkey("space")
    
    if frame % 200 == 0:
        print(f"fps: {frame/(time.time()-last_time)}")