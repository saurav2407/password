import pyautogui as pg
import time
import os
d=time.strftime('%D')


print("welcome to APPLICATION writer")
print("FILL THE GIVEN BOX")
print("   ")

print('↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')
print("   ")
for i in range(1):
    a=input("Enter your name:")
    g=input('class:')
    b=input("Enter your college/school name:")
    f=input("subject for leave:")
    e=input("address:")
    h=input('days for leave:')
    l=h.replace('days','')
    c=input("Reason for leave:")
    notepad=r'C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2305.18.0_x64__8wekyb3d8bbwe\Notepad\Notepad.exe'
    os.startfile(notepad)
    time.sleep(2)
    pg.typewrite(f'To the Principal,\n{ b }, \n{e},\nDate:{d},\nSubject:An application for {f}\n')
    pg.typewrite("sir/ Ma’am,\n")
    pg.typewrite(f"I would like to bring to your notice that I,{a} of {g}\nwill not be able to attend school for the coming {l}days \nas I have {c}.\n")
    pg.typewrite(f'I would kindly request you grant me leave for {l}days.I will be highly obliged.\n')
    pg.typewrite(f'Your’s truly, \n{a}, \n{g}\nDate:{d}')


