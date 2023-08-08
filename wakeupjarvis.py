import os
import pyautogui as pg
pg.hotkey("win",'m')
import speech_recognition as sr
import time 

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
                    

__path__=r'D:\jarvis\jarvis all\allinone\jarvis24.py'
# sourcery skip: merge-duplicate-blocks, remove-redundant-continue, remove-redundant-if
while True:
    wake_up = takeCommand()
    if 'wake up' in wake_up:
        os.startfile(__path__)
        time.sleep(3)
        exit()
    elif 'woke up' in wake_up:
        os.startfile(__path__)
        time.sleep(3)
        exit()
    elif 'breakup' in wake_up:
        os.startfile(__path__)
        time.sleep(3)
        exit()
    elif 'makeup' in wake_up:
        os.startfile(__path__)
        time.sleep(3)
        exit()
        
    else:
        print("nothing.....")
        continue
        
