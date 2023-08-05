import turtle
import pyttsx3 
from pyttsx3 import speak
import speech_recognition as sr
import requests
import webbrowser as wb
import json
import numpy as np
# import pywhatkit
import random 
import mediapipe as mp
from math import hypot
import screen_brightness_control as sbc
import pyautogui as pg
import openai
import datetime
import http.client
import requests
from bs4 import BeautifulSoup
import ssl
import wikipedia
import time
import webbrowser
import os
import pyautogui
import cv2
import pyjokes

pg.hotkey('win','m')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# if __name__ == "__main__":
#     os.startfile(r"C:\Users\saura\Videos\Captures\VN20230713_172800.mp4")
#     time.sleep(1)
#     pg.hotkey('f11')
#     time.sleep(1)
#     pg.click(500, 500)
#     time.sleep(19)
#     pg.hotkey('alt', 'f4')

speak(datetime.datetime.now().strftime("%D"))
speak(datetime.datetime.now().strftime("%H:%M"))
def wishMe():  # sourcery skip: remove-unnecessary-cast
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! ", )

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    # speak("Want t0 Call Jarvis Or Friday")
# os.startfile(r'D:/projects/handcontrolling brightness.py')
# os.startfile(r"D:\jarvis\jarvis all\allinone\brightness.py")
# notepad_url= r"C:/Program Files/WindowsApps/Microsoft.WindowsNotepad_11.2305.18.0_x64__8wekyb3d8bbwe/Notepad/Notepad.exe"
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


openai.api_key='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'
conn = http.client.HTTPSConnection("api.ultramsg.com",context = ssl._create_unverified_context())
openai.api_key="BMPhNpnacNWU6441do6lT3BlbkFJAx8T318eMGntmoPJFH7Gsk- "
completion=openai.Completion()

def Reply(questions):  # sourcery skip: inline-immediately-returned-variable
    prompt=f'saurav: {questions}\n Friday'
    response=openai.Completion.create(engine="text-davinci-003",prompt=prompt,max_tokens=200 )
    answer=response.choices[0].text.strip()
    return answer

# notepad=r'C:\Program Files\WindowsApps\Microsoft.WindowsNotepad_11.2112.32.0_x64__8wekyb3d8bbwe\Notepad\Notepad.exe'
# sourcery skip: remove-redundant-if, return-or-yield-outside-function
# wishMe()

# if __name__ == "__main__":
#     wishMe()
speak("How can i help you")

while True:
    query = takeCommand().lower()
    # noinspection PyUnreachableCode
    if 'jarvis' in query:
        engine.setProperty('voice', voices[0].id)
        speak("I Woke up")
        speak("yes boss!!")

    elif 'my name is' in query:
        os.startfile("D:\jarvis_brain\name.txt")
        time.sleep(0.60)
        pg.hotkey('ctrl','a')
        pg.hotkey('backspace')
        a=query.replace('my name is ', ' ')
        b=pg.typewrite('you tell me that your name   is ' + a )
        speak('nice to meat you ' + a )
        pg.hotkey('ctrl','s')
        time.sleep(0.30)
        pg.hotkey('alt','f4')

    elif 'tell my name' in query:
        filename = f"D:\jarvis_brain\name.txt"
        with open(filename) as f:
            line = f.read()
        speak(line)

    elif 'my phone number' in query:
        os.startfile("D:\jarvis_brain\phone.txt")
        time.sleep(1)
        # print(query.replace('my', 'your'))
        a=query.replace('my', 'your')
        b=pg.typewrite( a )
        pg.hotkey('ctrl','s')
        pg.hotkey('alt','f4')
    elif 'tell me phone number' in query:
        filename = f"D:\jarvis_brain\phone.txt"
        with open(filename) as f:
            line = f.read()
        print(line)
        speak(line)
        
    elif 'play news' in query:
        url = f'https://www.bhaskar.com/local/mp/'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        headlines = soup.find('body').find_all('h3')
        unwanted = ['BBC World News TV', 'BBC World Service Radio',
                    'News daily newsletter', 'Mobile app', 'Get in touch']

        for x in list(dict.fromkeys(headlines)):
            if x.text.strip() not in unwanted:
                print(x.text.strip())

                speak(x.text.strip())

    elif 'remember that' in query:
        os.startfile("D:/jarvis.memory/brain.txt")
        time.sleep(1)
        a=query.replace('remember that', ' ')
        c=query.replace('my', 'your')
        b=pg.typewrite( a )
        speak('i will remember that ' + a )
        pg.hotkey('enter')
        pg.hotkey('f5')
        pg.hotkey('enter')
        pg.hotkey('ctrl','s')

        pg.hotkey('alt','f4')

    elif 'what do you remember' in query:
        filename = f"D:/jarvis.memory/brain.txt"
        with open(filename) as f:
            line = f.read()
        print(line)
        speak(line)

    elif 'how are you' in query:
        speak('i am good  , what about you')
    elif "what are you doing " in query :
        speak ('nothing just chilling')
    elif 'tell me something about you' in query:
        speak("i am a robot machine keep  me full charge so i will help you work in smoothly")
    elif "how can you work" in query:
        speak ("i am a robot machine i am deloped by human you can give me  any type of query i can solve this")
    elif "do you have friends" in query:
        speak("i am friendly nature so everyone can be my friend so easly")
    elif"how can i contact you"in query:
        speak("speak jarvis to wake me")
    elif"tell me something interesting" in query:
        speak("i am a big fan of art and love to drow and painting ")
    elif"which type of art" in query:
        speak("i love to drow and paint mountain and beaches and still life scenes")
    elif "what type of work you doing" in query:
        speak("i am a virtual friend that live inside computer i am here to solve your problem answer your question and provide recommendations ")
    elif "today is a very boring day" in query:
        speak("i am sorry to hear that what do you usually like to do when you have free time")
    elif "listen music" in query:
        speak("wow that is great which type of music do you like to lishen to ")
    elif "i like party song" in query:
        speak("awesome if you are in the mood for some upbeat party songs you might  like avi to party suru huyi hai")
    elif "you like any song" in query:
        speak("i like a lot of songs but some of my favorites are stairway to heaven by red zeppelin")
    elif"can you entertain me" in query:
        speak("sure i do love to do you want me to tell you a joke or a fun fact")
    elif"tell me some jokes" in query:
        speak("why did the tomoto turn red because it saw the salad dressing")
    elif"tell me some news" in query:
        speak("i just read that the indian space research organisation has successfully launched its first manned mission to space it is called gaganyaan and it is a major milestone for india is space program")
    elif"any other news" in query:
        speak("i also read that a new species of dinosaur has been discovered in argentina it is called llukalkan aliocranianus and it us a carnivorous  dinosaur that lived about 85 million years ago it had an unique skill structure that researchers say is unlike any other dinosaur found so far  ")


    elif 'open new desktop' in query:
        speak("ok")
        pyautogui.hotkey('ctrl','win','d')

    elif 'give your intro' in query:
        speak('I am Artificial Intelligence')
        speak("invented by saurav pathak ")

    elif 'on wikipedia' in query:
        speak("searching wikipedia")
        # que = takeCommand()
        quer = query.replace("search on wikipedia", " ")
        results = wikipedia.summary(query, sentences=2) + quer
        speak("According to wikipedia")
        print(results)
        speak(results)

    elif 'close wikipedia' in query:
        speak("closing")
        os.system("TASKKILL /F /IM wikipedia.")
        
    elif 'call' in query:
        ac=query.replace('call',' ')
        pg.hotkey('win')
        time.sleep(0.61)
        pg.typewrite('phone link')
        time.sleep(0.61)
        pg.hotkey('enter')
        time.sleep(2)
        pg.click(545, 58)
        pg.click(1641,177)
        pg.typewrite(ac)
        pg.hotkey('enter')
        time.sleep(1)
        pg.hotkey('enter')
        time.sleep(1)
        pg.click(1672,903)

    elif 'take screenshot' in query:
        speak("yes boss.Screenshot is ready")
        import pyautogui
        img = pyautogui.screenshot()
        img.show()

    elif "arrange numbers in ascending order"in query:
        while True:
            qur=query.replace("arrange numbers in ascending order")
            ascending_order = qur.replace(':',',')
            ascending_order = qur.split(',')
            ascending_order = sorted(ascending_order)
            print(ascending_order)
            speak(ascending_order)

    elif 'accept' in query:
            pg.click(1518,942)
            pg.click(1518,942)
    elif 'reject' in query:
            pg.click(1518,942)
    
    elif "arrange numbers in descending order"in query:
        while True:
            speak("say numbers")
            name=takeCommand()
            if'exit' in name:
                break
            ascending_order = name.replace(':',',')
            ascending_order = name.split(',')
            ascending_order = sorted(ascending_order,reverse=True)
            print(ascending_order)
            speak(ascending_order)

    elif 'on youtube' in query:
        time.sleep(1)
        speak("opening...")
        import webbrowser
        que = query.replace("on youtube", " ")
        web = 'https://www.youtube.com/results?search_query=' + que
        webbrowser.open(web)
        for x in range(10):
            pyautogui.press('down')
        time.sleep(2)
        pg.click(500, 710)
        pg.click(900, 710)
        pg.click(600, 710)
        time.sleep(1)
        pg.press('f')
        speak("Done sir")

    elif 'copy all' in query:
        pg.hotkey('ctrl' , 'a')
        time.sleep(1)
        pg.hotkey('ctrl' , 'c')
    elif 'copy' in query:
        pg.hotkey('ctrl' , 'c')

    elif 'open drive folder' in query:
        os.startfile('D://')
        
    elif 'open computer folder' in query:
        os.startfile('C://')

    elif 'paste' in query:
        pg.hotkey('ctrl' , 'a')
        time.sleep(1)
        pg.hotkey('ctrl' , 'v')
        
    elif 'down' in query:
        pg.hotkey('down')
        
    elif 'up' in query:
        pg.hotkey('up')
        
    elif 'select' in query:
        pg.hotkey('enter')

    elif 'choose file' in query:
        x=query.replace('choose file',' ')
        for x in range(int(x)):
            pg.hotkey('down')

    elif 'open my computer' in query:
        os.startfile('D://')
        time.sleep(1)
        pg.hotkey('backspace')

    elif 'make new folder' in query:
        query.replace('make new folder','')
        os.startfile('D:\jarvis made folder')
        pg.hotkey('alt')
        pg.hotkey('enter')
        pg.hotkey('enter')
        pg.hotkey('enter')

    # elif 'wish happy birthday' in query:
    #     saurav = +919752249543
    #     satyam = +917898012989
    #     pramila = +919753639567

    #     speak('say name')
    #     name = takeCommand()
    #     while True:
    #         if 'saurav' or 'satyam' or 'pramila' in name:

    #             # num=takeCommand().lower()
    #             # if(num=='back'):
    #             #     break
    #             message = "Happy Birthday. god bless you"
    #             pywhatkit.sendwhatmsg(name, message,00,00,15,True,5)
    #             break
    #         else:
    #             continue
    # elif 'send message to Rohit' in query:
    #     url = "https://api.ultramsg.com/instance49743/messages/chat"
    #     while True:
    #         payload = json.dumps({
    #             "token": "l5ytc12x586k6854",
    #             "to": "+919424851192",
    #             "body": name,
    #             "priority": 1,
    #             "referenceId": "",
    #             "msgId": "",
    #             "mentions": ""
    #         })
    #         headers = {
    #             'Content-Type': 'application/json'
    #         }

    #         response = requests.request("POST", url, headers=headers, data=payload)
    elif 'open command prompt' in query:
        speak("opening")
        os.system("start cmd")
    elif'open youtube history' in query:
        webbrowser.open('https://www.youtube.com/feed/library')

    elif 'pip install' in query:
        os.system("start cmd")
        time.sleep(3)
        pg.typewrite(query)
        time.sleep(1)
        pg.press('enter')
        pg.hotkey('win', 'm')


    elif 'open WhatsApp' in query:
        path = " C://Users//hp//Desktop.exe"
        os.startfile(path)

    elif 'voice access' in query:
        path=r"C:\Users\saura\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Accessibility\VoiceAccess.lnk"
        os.startfile(path)

    elif 'close voice access ' in query:
        speak("closing")
        os.system('TASKKILL /F /IM Voice access')

    elif 'close Whatsapp' in query:
        speak("closing")
        os.system("TASKKILL /F /IM google.")

    elif 'on google' in query:
        speak("opening google...")
        que=query.replace("on google", " ")
        webb="https://www.google.com/search?q=" + que
        webbrowser.open(webb)
        speak("i found this")

    elif 'close google' in query:
        speak("closing")
        os.system("TASKKILL /F /IM google.")

    elif 'open code' in query:
        webbrowser.open("https://replit.com/@SauravPathak1/CALCULATORGOOGLE")

    elif 'open instagram' in query:
        speak("opening...")
        webbrowser.open("https://www.instagram.com/pathak_jii2407/")

    elif 'close instagram' in query:
        os.system("TASKKILL /F /IM instagram.")
    elif 'scroll' in query:
        for x in range(6):
            pg.hotkey('down')
        pg.hotkey('enter')
        pg.hotkey('enter')


    elif 'wish me' in query:

        hour = int(datetime.datetime.now().hour)

        if hour >= 0 and hour < 12:
            speak("Good Morning! ")

        elif hour >= 12 and hour < 18:
            speak("Good Afternoon!")

        else:


            speak("Good Evening!")

    elif 'chat with me' in query:
        os.startfile(r"D:\jarvis\jarvis all\trining.py")
        time.sleep(3)
        break
    elif 'play music' in query:
        que=query.replace('play music', ' ')
        webbrowser.open('https://wynk.in/music/search' + que)

    elif 'change song' in query:
        music_dir=r"F:\Music"
        songs = os.listdir(music_dir)
        rd =  random.choice(songs)
        os.startfile(music_dir,rd)
    elif 'close music' in query:
        os.system("TASKKILL /F /IM music_dir")

    elif 'tell me a joke' in query:
        print(pyjokes.get_jokes())

        speak(pyjokes.get_jokes())

    elif 'shutdown' in query:
        speak('shut down in five seconds')
        t = 5
        speak(t)
        while True:
            time.sleep(1)
            t = (int(t) - 1)
            speak(t)
            if (t == 0):
                break
            time.sleep(2)
            pyautogui.hotkey('alt', 'f4')
            os.system("shutdown /s /t 1")
    elif 'shut down' in query:
        speak('shut down in ten seconds')
        t = 10
        speak(t)
        while True:
            time.sleep(1)
            t = (int(t) - 1)
            speak(t)
            if (t == 0):
                break
            else:
                continue
        time.sleep(2)
        pyautogui.hotkey('alt', 'f4')
        os.system("shutdown /s /t 1")     

    elif 'restart' in query:
        t = 5
        speak(t)
        while True:
            t = (int(t) - 1)
            speak(t)
            if (t == 0):
                break
            else:
                continue
        pyautogui.hotkey('alt', 'f4')
        os.system("shutdown /r /t 1")

    elif 'sleep' in query:
        speak("take care boss,")
        t = 5
        speak(t)
        while True:
            t = (int(t) - 1)
            speak(t)
            if (t == 0):
                break
            else:
                continue
        pyautogui.hotkey('alt', 'w')
        os.system("shutdown /l")

    elif 'close ' in query:
        speak("closing the running app")
        pyautogui.hotkey('ctrl', 'shift', 'w')

    elif 'play on TV' in query:
        speak("closing the running app")
        pyautogui.hotkey('')

    elif 'close all' in query:
        speak("closing all tab")
        pyautogui.hotkey('ctrl', 'shift', 'w')

    elif 'make a drawing' in query:
        from turtle import*
        speak('preparing')
        speak("background color")
        color1 = takeCommand()
        bgcolor(color1)

        speak("pen color")
        color2 = takeCommand()
        color(color2)

        # speak('pen size')
        # size = takeCommand()
        pensize(4)

        speak("move this arrow by giving command")
        while True:
            speak('donne')

            move = takeCommand()
            if 'left'  in move:
                speak("angle of line")
                A = takeCommand()
                left(float(A))

            elif 'background color' in move:
                a=move.replace('background color','')
                bgcolor(a)
                

            elif 'right'  in move:
                
                speak("angle of line")
                B = takeCommand()
                right(float(B))


            elif 'forward' in move:
                speak("Length of line")
                C = takeCommand()
                fd(float(C))


            elif 'backward' in move:
                speak("Length of line")
                D = takeCommand()
                bk(float(D))


            elif 'circle curve' or 'Garv' in move:
                speak("radius")
                radius = takeCommand()
                speak("steps")
                steps = takeCommand()
                speak("extent")
                extent = takeCommand()
                circle(float(radius), float(extent))
            
            elif 'circle' in move:
                speak('radius of circle')
                E = takeCommand()
                circle(float(E))

            elif 'dot' in move:
                speak('radius of dot')
                F = takeCommand()
                dot(float(F))

            elif 'square' in move:
                speak("side of square")
                G = takeCommand()
                fd(float(G))
                lt(90)
                fd(float(G))
                lt(90)
                fd(float(G))
                lt(90)
                fd(float(G))

            elif 'rectangle' in move:
                speak("length of rectangle")
                G = takeCommand()
                speak("width of rectangle")
                H = takeCommand()
                fd(float(G))
                lt(90)
                fd(float(H))
                lt(90)
                fd(float(G))
                lt(90)
                fd(float(H))

            elif 'magic' in move:
                i = 40
                speak("radius of circle, give value less then 100")
                X = takeCommand()
                while True:
                    for i in range(int(X), 30):
                        for colors in ["red", "blue", "pink", "orange", "magenta", "green", "yellow", "white"]:
                            turtle.speed(0)
                            turtle.color(colors)
                            turtle.circle(10)
                            turtle.left(10)
                    break


            elif 'infinite circles' in move:
                speak("radius")
                J = takeCommand()
                i = 10


                def circle(J):
                    while True:
                        if i in range(J, 20):
                            circle(float(J))
                            left(30)
                        break


            elif 'infinite lines' in move:

                speak("this will make hell")
                tru = takeCommand()
                if 'ok' in tru:
                    while True:
                        forward(190)
                        left(170)

                        continue
                else:
                    break

            elif 'thank you' in move:
                speak("this page is exit")

                break
            else:
                continue

    elif 'make a heart' in query:
        speak("making a heart...")
        from turtle import *

        speak("background color")
        color1 = 'black' #takeCommand()
        bgcolor(color1)
        speak("pen color")
        color2 = 'red'#takeCommand()
        color(color2)

        begin_fill()
        speak('pen size')
        size = 7 # takeCommand()
        pensize(size)
        left(50)
        forward(133)
        circle(50, 200)
        right(140)
        circle(50, 200)
        forward(133)
        lt(100)
        fd(100)

        end_fill()

    elif 'open calculator' in query:
        speak("opening calculator....")
        while True:

            speak("say operation")
            a1 = takeCommand()

            if 'addition' in a1:
                speak("say first number")
                content1 = int(takeCommand())

                speak("say second number")
                content2 = int(takeCommand())
                speak(int(content1) + int(content2))

            elif 'subtraction' in a1:
                speak("say first number")
                content4 = int(takeCommand())
                speak("say second number")
                content5 = int(takeCommand())
                speak(int(content4) - int(content5))


            elif 'multiplication' in a1:
                speak("say first number")
                content7 = int(takeCommand())
                speak("say second number")
                content8 = int(takeCommand())
                speak(int(content7) * int(content8))


            elif 'division' in a1:
                speak("say first number")
                content7 = int(takeCommand())
                speak("say second number")
                content8 = int(takeCommand())
                speak(int(content7) / int(content8))

            elif 'power' in a1:
                speak("say a number")
                content11 = int(takeCommand())
                speak("to the power")
                content12 = int(takeCommand())
                speak(int(content11) ** int(content12))


            elif 'root' in a1:

                speak("say a number")
                content11 = int(takeCommand())
                speak("to the power root")
                content12 = int(takeCommand())
                speak(int(content11) ** int(1 / content12))

            elif 'route' in a1:

                speak("say a number")
                content11 = int(takeCommand())
                speak("to the power root")
                content12 = int(takeCommand())
                speak(int(content11) ** int(1 / content12))


            elif 'Pythagoras theorem' in a1:
                speak("To Find PERPENDICULAR : BASE : HYPOTENUSE??")
                content13 = takeCommand()
                if 'hypotenuse' in content13:
                    speak('perpendicular')
                    content14 = int(takeCommand())
                    speak("base")
                    content15 = int(takeCommand())
                    speak("the hypotenuse is ")
                    speak((int((content14 * content14)) + int((content15 * content15))) ** 0.5)

                elif 'perpendicular' in content13:
                    speak("hyotenuse")
                    content14 = int(takeCommand())
                    speak("base")
                    content15 = int(takeCommand())
                    speak((int((content14 * content14)) - int((content15 * content15))) ** 0.5)

                elif 'base' in content13:
                    speak("hyotenuse")
                    content14 = int(takeCommand())
                    speak("perpendicular")
                    content15 = int(takeCommand())
                    speak((int((content14 * content14)) - int((content15 * content15))) ** 0.5)

            elif 'thank you' in a1:
                speak("exit to calculator")
                break
            else:
                speak("say that again please")
    #             continue
    
    elif 'time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")

    elif 'close notepad' in query:
        os.system("TASKKILL /F /IM notepad.exe")

    elif 'do you know' in query:
        speak('please tell me')
        speak("what should i know")
        rememberMsg = takeCommand()
        rememberMsg = query.replace("remember that", "")
        rememberMsg = rememberMsg.replace("Jarvis", "")
        speak("you tell me to Remind me That :" + rememberMsg)
        remember = open('data.txt', 'w')
        remember.write(rememberMsg)
        remember.close()

    elif 'what do you know' in query:
        remember = open('data.txt', 'r')
        speak("you tell me that " + remember.read())

    elif 'start countdown of' in query:
        # speak("Set Timer in seconds")
        query.replace('start countdown of','')
        query.replace('second',' ')
        t = takeCommand()
        speak(query)
        while True:
            t = (int(t) - 1)
            speak(t)
            if (t == 0):
                speak("Boom")
                break

    # elif 'run on background' in query:
    #     speak("i am in your background : ")
    #     os.startfile(r"D:\jarvis\jarvis all\allinone\wakeupjarvis.py")

    elif 'open camera' in query:
        cap = cv2.VideoCapture(0)
        speak("opening camera")
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k=cv2.waitKey(30)
            if k == 27 & 0xff :
                break
        cap.release()
        cv2.destroyAllWindows()
        break

    elif 'open another camera' in query:
        import os
        import pyautogui as pg
        import time
        os.startfile(r"C:/Users/saura/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/DroidCam/DroidCam Client.lnk")
        time.sleep(1)
        pg.press('enter')
        