import pyttsx3
import cv2
import mediapipe as mp
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def count_fingers(lst):
    cnt = 0

    thresh = (lst.landmark[0].y * 100 - lst.landmark[9].y * 100) / 2

    if (lst.landmark[5].y * 100 - lst.landmark[8].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[9].y * 100 - lst.landmark[12].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[13].y * 100 - lst.landmark[16].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[17].y * 100 - lst.landmark[20].y * 100) > thresh:
        cnt += 1

    if (lst.landmark[5].x * 100 - lst.landmark[4].x * 100) > 6:
        cnt += 1

    return cnt


cap = cv2.VideoCapture(0)

drawing = mp.solutions.drawing_utils
hands = mp.solutions.hands
hand_obj = hands.Hands(max_num_hands=2)

start_init = False

prev = -1

while True:
    end_time = time.time()
    _, frm = cap.read()
    frm = cv2.flip(frm, 1)

    res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))



    if res.multi_hand_landmarks:

        hand_keyPoints = res.multi_hand_landmarks[0]

        cnt = count_fingers(hand_keyPoints)

        if not (prev == cnt):
            if not (start_init):
                start_time = time.time()
                start_init = True

            elif (end_time - start_time) > 0.2:

                if (cnt == 2):
                    time.sleep(5)

                    # pyautogui.hotkey("ctrl", 'f2')
                    # pyautogui.press('enter')

                elif (cnt == 3):
                    speak('alart')
                    # speak('alart')
                    # speak('alart')
                    # speak('alart')

                    # (os.startfile("D:/jarvis/jarvis all/allinone/pyauto/ultrajarvis.mp4"))
                    # pyautogui.hotkey("ctrl", 'm')
                    # os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2023.1.3.lnk")

                elif (cnt  == 1):
                    speak('alart')
                    # speak('alart')
                    # speak('alart')
                    # speak('alart')


                    # os.startfile("D:/jarvis/jarvis all/allinone/pyauto/ultrajarvis.mp4")
                    # pyautogui.hotkey("ctrl", 'm')
                    # os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2023.1.3.lnk")

                elif (cnt == 4):
                    # speak('alart')
                    # speak('alart')
                    # speak('alart')
                    # speak('alart')
                    speak('alart')


                       # os.startfile("D:/jarvis/jarvis all/allinone/pyauto/ultrajarvis.mp4")
                       # pyautogui.hotkey("ctrl", 'm')
                       # os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2023.1.3.lnk")

                elif (cnt == 5):
                    # speak('alart')
                    # speak('alart')
                    # speak('alart')
                    # speak('alart')
                    speak('alart')


                    # os.startfile("D:\jarvis\jarvis all\dist\WhatsApp Audio 2023-06-07 at 20.55.27.mp3")
                    # pyautogui.hotkey("ctrl", 'm')
                    # os.startfile("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2023.1.3.lnk")

                prev = cnt

                tart_init = False

        drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

    cv2.imshow("window", frm)

    if cv2.waitKey(1) == 27:
        cv2.destroyAllWindows()
        cap.release()
        break