import datetime
import os
import wikipedia
import random
import winsound
import sounddevice as sd
import time
import turtle
import webbrowser
from tkinter import messagebox
import pywhatkit
import speech_recognition as sr
import tkinter as tk
import numpy as np
import pyjokes
import pyautogui
import pyjokes
import pyttsx3



root=tk.Tk()
root.geometry("50x50") 
root.title('SUPREME JARVIS')
root.after_cancel=False
root.attributes("-topmost", True)


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

hour = int(datetime.datetime.now().hour)
minute = int(datetime.datetime.now().minute)
day = int(datetime.datetime.now().day)
month = int(datetime.datetime.now().month)


def date():
    speak(f'Today is {day} {month}th month')
    speak(f'{hour} hour{minute}minute')


def create_bubble():
    x = random.randint(20, 380) 
    y = 380 
    size = random.randint(10, 30) 

    bubble = canvas.create_oval(x, y, x + size, y + size, outline="blue", fill="lightblue")

    animate_bubble(bubble)

def animate_bubble(bubble):
    x1, y1, x2, y2 = canvas.coords(bubble)
    if y1 > 0:  
        canvas.move(bubble, 0, -5) and canvas.move(bubble, 0, 5)
        canvas.after(50, lambda: animate_bubble(bubble))


def another_win():
    global another_window
    another_window=tk.Tk()
    another_window.geometry('500x300')
    another_window.title('Welcome')
    global player
    player = tk.Entry(another_window,width=40,highlightthickness=1,highlightbackground='blue',highlightcolor='black')
    player.place(x=30, y=10)
    button = tk.Button(another_window, text="Youtube",command=song_)
    button.place(x=50, y=100)

    button2 = tk.Button(another_window, text="Google search",command=google_search)
    button2.place(x=150, y=100)
    button3 = tk.Button(another_window, text="Spotify",command=spotify)
    button3.place(x=300, y=100)
    button4 = tk.Button(another_window, text="Calculator",command=calculator_TK)
    button4.place(x=450, y=100) 
    another_window.mainloop()

def button_clicked():
    jarvis_.config(bg="#FFA500", relief=tk.SUNKEN)

def button_released():
    jarvis_.config(bg="#FFD700", relief=tk.RAISED)

def factorial(factorial_num):
    if factorial_num == 1:
        return 1
    else:
        return factorial_num *  factorial(factorial_num-1)
    
def wishMe():  
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning! ", )

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
def get(self):
        """Return the text."""
        return self.tk.call(self._w, 'get')

def song_():
    pywhatkit.playonyt(f"https://www.youtube.com/watch?v={player.get()}")
def google_search():
    webbrowser.open(f"https://www.google.com/search?q={player.get()}")
def spotify():
    webbrowser.open(f"https://open.spotify.com/search/{player.get()}")
def calculator_TK():
    speak(int(eval(player.get())))

def play_notification_beep():
    frequency = 1000  
    duration = 1000  
    winsound.Beep(frequency, duration)


def sleep():
    time.sleep(60)
def shut_down():
    os.system("shutdown /s /t 1")
    play_notification_beep()

def restart():
    os.system("shutdown /r /t 1")
    play_notification_beep()
def instagrm():
    webbrowser.open("https://www.instagram.com/pathak_jii2407/")
def exit_loop():
    speak('Good bye world')
    play_notification_beep()
    exit()

def youtubeplay(que):
    web= "https://www.youtube.com/watch?v=" + que  
    webbrowser.open(web) 
    pywhatkit.playonyt(que)
    speak("Done sir")


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
        label=tk.Label(root,text=f'you said: {query}\n')
        label.pack(side='right')

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query




date()

try:
    def arvis():
            speak("Yes Boss")
            while True:
                query = takeCommand().lower()

                if 'Jarvis' in query:
                    speak("I Woke up")
                    speak("yes boss!!")


                elif 'give your intro' in query:
                    speak('I am Artificial Intelligence')
                    speak("invented by saurav pathak ")
                

                elif 'on wikipedia' in query:
                    speak("searching wikipedia")
                    query = query.replace("wikipedia", "")
                    results = wikipedia.summary(query, sentences=2) + query
                    speak("According to wikipedia")
                    answer_label = tk.Label(root,text=f"answer:{results}\n")
                    answer_label.pack(side='right')
                    print(results)
                    speak(results)
                    
                elif 'close wikipedia' in query:
                    speak("closing")
                    os.system("TASKKILL /F /IM wikipedia.")



                elif 'open command prompt' in query:
                    speak("opening")
                    os.system("start cmd")

                elif 'open WhatsApp' in query:
                    path = 'https://web.whatsapp.com/'
                    webbrowser.open_new(path)

                elif 'on google' in query:
                    speak("searching on google...")
                    query.replace("on google",'')
                    webb="https://www.google.com/search?q=microphone+" + query
                    webbrowser.open(webb)
                    speak("i found this")
                elif 'open google' in query:
                    speak("opening google...")
                    webb="https://www.google.com"
                    webbrowser.open(webb)
                    speak("i found this")


                elif 'open code' in query:
                    webbrowser.open("https://replit.com/@SauravPathak1/CALCULATORGOOGLE")

                elif 'open instagram' in query:
                    speak("opening...")
                    webbrowser.open("https://www.instagram.com/pathak_jii2407/")

                elif 'wish me' in query:
                    wishMe()

                elif 'tell me a joke' in query:
                    speak(pyjokes.get_jokes())
                    print(pyjokes.get_jokes())

                elif 'shutdown' in query:
                    speak('shut down in five seconds')
                    t = 5
                    speak(t)
                    while True:
                        t = (int(t) - 1)
                        speak(t)
                        if (t == 0):
                            break
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
                        pyautogui.hotkey('alt', 'f4')
                        os.system("shutdown /r /t 1")

                elif "shut down" in query:
                    speak("going to sleep in 5 seconds")
                    t = 5
                    speak(t)
                    while True:

                        # time.sleep(1)
                        t = (int(t) - 1)
                        speak(t)
                        if (t == 0):
                            break
                        pyautogui.hotkey('alt', 'w')
                        os.system("shutdown /l")

                elif 'close' in query:
                    speak("closing the running app")
                    pyautogui.hotkey('alt', 'f4')
                elif 'exit' in query:
                    speak("closing the running app")
                    pyautogui.hotkey('alt', 'f4')
                    
                elif 'close all' in query:
                    speak("closing all tab")
                    pyautogui.hotkey('ctrl', 'shift', 'w')
                    
                elif 'calculate' in query:
                    
                    quer=query.replace('calculate','')
                    que=quer.replace('x','*')
                    qu=que.replace('into','*')
                    calci_=f"the answer is: {eval(qu)}"
                    speak(calci_)
                    answer_label = tk.Label(root,text=f"answer:{calci_}\n")
                    answer_label.pack(side='right')
                    answer_label.destroy()

                elif 'the time' in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:%S")
                    speak(f"Sir, the time is {strTime}")


                elif 'remember that' in query:
                    rememberMsg = query.replace("remember that", "")
                    rememberMsg = rememberMsg.replace("Jarvis", "")
                    speak("you tell me to Remind me That :" + rememberMsg)
                    remember = open('data.txt', 'w')
                    remember.write(rememberMsg)
                    remember.close()
                


                elif 'what do you remember' in query:
                    remember = open('data.txt', 'r')
                    speak("you tell me that " + remember.read())
                elif 'factorial of' in query:
                    
                    factorial_num=query.replace('factorial of','')
                    speak(f"The factorial of {factorial_num} is {factorial(int(factorial_num))}")

                elif 'start countdown of' in query:
                    que=query.replace('start countdown of','') #start countdown of 5 seconds
                    qu=que.replace('seconds','')
                    speak(qu)
                    for x in range(int(qu)):
                            time.sleep(1)
                    play_notification_beep()
                elif 'YouTube'in query:                        
                    speak("playing...")
                    que=query.replace('on YouTube','')
                    youtubeplay(que)
                    
                elif 'destroy' in  query:
                    speak('Good Bye Sir')
                    speak('take care you bloody')
                    play_notification_beep()
                    exit()

except Exception as e:
    play_notification_beep()
    messagebox.showerror('Error',e)

try:
    jarvis_ = tk.Button(root, text="<JARVIS>",bg='white',font='bold',border=3,borderwidth=3,highlightbackground='black',highlightthickness=5,highlightcolor='red',command=arvis)
    jarvis_.bind("<Button-1>", lambda event: button_clicked())
    jarvis_.pack()
    jarvis_.bind("<ButtonRelease-1>", lambda event: button_released())

    button1 = tk.Button(root, text="Wake-UP",command=arvis,bg='green',borderwidth=2,highlightbackground='black',highlightthickness=1,highlightcolor='black')
    button1.place(x=50, y=50)

    button5 = tk.Button(root, text="Exit",command=exit_loop,bg='gold',borderwidth=2,highlightbackground='black',highlightthickness=1,highlightcolor='black')
    button5.place(x=150, y=50)

    button2 = tk.Button(root, text="Sleep",command=sleep,bg='silver')
    button2.place(x=200, y=50)

    button3 = tk.Button(root, text="Shut-Down",command=shut_down,bg='orange',borderwidth=2,highlightbackground='black',highlightthickness=1,highlightcolor='black')
    button3.place(x=50, y=50)

    button4 = tk.Button(root, text="Re-Start",command=restart,bg='sky blue')
    button4.place(x=350, y=50)



    button6 = tk.Button(root, text="Instagram",command=instagrm,bg='red')
    button6.place(x=450, y=50)

    button8 = tk.Button(root, text="Date",command=date)
    button8.place(x=280, y=50) 

    button9 = tk.Button(root, text="search",command=another_win,bg='pink',borderwidth=2,highlightbackground='black',highlightthickness=1,highlightcolor='black')
    button9.place(x=650, y=50)

    button10 = tk.Button(root, text="Bubble",command=create_bubble,bg='skyblue',borderwidth=2,highlightbackground='black',highlightthickness=1,highlightcolor='black')
    button10.place(x=550, y=50)
    canvas = tk.Canvas()
    canvas.pack()


except Exception as e:
    messagebox.showerror("Error",e)

tk.mainloop()




