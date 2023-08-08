import time
import os
import pyautogui
t = 5
while True:
    time.sleep(1)
    t = (int(t) - 1)
    print(t)
    if (t == 0):
        break
    else:
        continue
    
time.sleep(2)
pyautogui.hotkey('alt', 'f4')
os.system("shutdown /s /t 1")