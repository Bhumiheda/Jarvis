import pyttsx3 as p  
import speech_recognition as sr  
import cv2  
from web import *
from yt1 import *
from news import *
import randfacts
from joke import *
import threading

def play_video_in_loop():
    cap = cv2.VideoCapture("C:\\sem 3\\general purpose programming-python\\nova\\video.mp4")

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return  

    while True: 
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  
        while cap.isOpened():
            ret, frame = cap.read()
            if ret:
                cv2.imshow('Video', frame)
                if cv2.waitKey(25) & 0xFF == ord('q'):  
                    cap.release()
                    cv2.destroyAllWindows()
                    return  
            else:
                
                print("Replaying...")
                break

    cap.release()
    cv2.destroyAllWindows()
t1= threading.Thread(target=play_video_in_loop)
t1.start()

engine=p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',180)  
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

speak("Hello. I am your voice assistant Jarvis. how are you")
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print("Listening...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
if "what" and "about" and "you" in text:
    speak("I am having a good day.")
    speak("what can i do for you")

    with sr.Microphone() as source:
     r.adjust_for_ambient_noise(source, duration=1) 
     print("Listening...")
     audio = r.listen(source)
     try:
         text2 = r.recognize_google(audio)
         print(text)
     except sr.UnknownValueError:
         print("Sorry, I didn't understand that")
     except sr.RequestError as e:
         print("Could not request results from Google Speech Recognition service; {0}".format(e))

if "information" in text2:
    speak("you need information related to which topic")

    with sr.Microphone() as source:
     r.adjust_for_ambient_noise(source, duration=1)
     print("Listening...")
     audio = r.listen(source)
     infor = r.recognize_google(audio)
    speak("searching {} in wikipedia".format(infor))
    assist = InfoFetcher()
    assist.get_info(infor)

elif "play"  and "video" in text2:
    speak ("you want me to play which video??")
    with sr.Microphone() as source:
     r.adjust_for_ambient_noise(source, duration=1) 
     print("Listening...")
     audio = r.listen(source)
     vid = r.recognize_google(audio)
    speak("playing {} in youtube".format(vid))
    assist = Music()
    assist.get_info(vid)

elif "news" in text2:
    speak("sure")
    arr=news()
    for i in range(len(arr)):
       speak(arr[i])
       print(arr[i])

elif "fact" or "facts" in text2:
    x=randfacts.getFact()
    print(x)
    speak("sure")
    speak("Did you know that "+x)

elif "joke" or "jokes" in text2:
    arr=joke()
    print(arr[0])
    speak(arr[0])
    print(arr[1])
    speak(arr[1])

