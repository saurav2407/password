import time
import pyautogui as pg


msg=input('Enter message:')
# num=input('Enter number:')
n=input('Enter number of message:')
# pg.hotkey('win','s')
# time.sleep(1)
# pg.typewrite('whatsapp')
# time.sleep(1)
# pg.press('enter')
# time.sleep(2)
# pg.typewrite(num)
# time.sleep(2)
# pg.press('down')
# time.sleep(1)
# pg.press('enter')
time.sleep(5)
for x in range (int(n)):
    pg.typewrite(msg)
    pg.press('enter')















