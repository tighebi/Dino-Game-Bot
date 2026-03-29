import pyautogui
import time
import mss
import numpy as np
 

pyautogui.time.sleep(3)

frame = 0
c = 10
last_time = time.time()

with mss.mss() as sct:
    while "Dino running":
        frame += 1
        x, y = pyautogui.position()

        monitor = {"top": y-c, "left": x-c, "width": 2*c, "height": 2*c}
        img = np.array(sct.grab(monitor))

        if (img[:,:,:3].mean(axis=2) < 128).any():
            pyautogui.hotkey("space")
        
        if frame == 500:
            print(f"fps: {frame/(time.time()-last_time)}")
            last_time = time.time()
            frame = 0            