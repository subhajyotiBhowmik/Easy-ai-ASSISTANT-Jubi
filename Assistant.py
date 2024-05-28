import subprocess
import webbrowser
import winsound

import cv2
import pyautogui
import pyttsx3
import datetime
from playsound import playsound


import requests
import self as self
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import psutil
import pyjokes
import smtplib

from bs4 import BeautifulSoup

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

voicespeed = 190
engine.setProperty('rate',voicespeed)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("Now the time is")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak("Today's Date is")
    speak(date)
    speak(month)
    speak(year)




def wishme():
    speak("Welcome back Sir!!!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <= 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    elif hour >= 18 and hour <= 24:
        speak("Good night sir")

    speak("I am  at your service. Please tell me how can i help you?")
    speak("Checking Microphone Instances and Clearing Extra noises...")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 2
        audio = r.listen(source)

    try:
        print("Recognizning...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:-{query}")

    except Exception as e:
        print("Repeat once sir.too much noise")
        speak("Sorry sir can you please repeat?")

        return "none"
    return query

def run(self):
    speak("please say wakeup to continue")
    while True:
        self.query = self.takecommand()
        if "wake up " in self.query or "are you there" in self.query or "hello" in self.query:
            self.TaskExecution()
def TaskExecution(self):
    wishme()
    while True:
        self.query = self.takecommand()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 535)
    server.ehlo()
    server.starttls()
    server.login('swarupsubho@gmail.com', 'Swarup@1973')
    server.sendmail('swarupsubho@gmail.com', to, content)
    server.close()


def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\subha\\OneDrive\\Pictures\\Screenshots\\ss.png")





def cpu():
    usage = str(psutil.cpu_percent())
    speak("cpu is at"+usage)
    battery = psutil.sensors_battery()
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_jokes())


def get(param):
    pass


if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)

        elif 'send email' in query:
            try:
                speak("what will you send?")
                content = takeCommand()
                to = 'subhajyoti010102@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("unable to send email")


        elif "open chrome" in query:
            webbrowser.open("www.google.com")
            speak(" your Chrome browser is opened.")

        elif "open google" in query:
            speak("Sir what should I search on google?")
            cm = takeCommand().lower()
            webbrowser.open(f"{cm}")

        elif "thank you" in query:
            speak("You are most welcome")



        elif "who made you" in query:
            speak("My developer name is Jubi . For him today I am here ....... Thank you Jubi ")

        elif "hello" in query:
            speak("Hi, it's really good to hear from you Sir!")




        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            speak("opening in 2 second!!")

        elif "send message" in query:
            speak("what should i send?")
            msz= takeCommand()

            from twilio.rest import  Client

            account_sid=['AC95436f57a2496fb0aad925f79a5e3c2e']
            auth_token = ['c564a73162f92ecad7d0b9cdaa2d080c']

            client=Client(account_sid,auth_token)
            message=client.messages \
                .create(
                    body=msz,
                    from_='+18624659594',
                    to= '+918101074980'
            )
            print(message.sid)

        elif "alarm" in query:
            speak("sir please tell me the time to set alarm. For example set alarm to at 9:30 am")
            tt = takeCommand()
            tt=tt.replace("set alarm to","")
            tt=tt.replace(".","")
            tt = tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)

        elif 'volume up' in query:
            pyautogui.press("volumeup")
            speak("Your voulume level is increasing")

        elif 'volume down' in query:
            pyautogui.press("volumedown")
            speak("Your voulume level is decreasing")

        elif 'volume mute' in query or 'mute' in query:
            pyautogui.press("Muted")
            speak("Muting your voulume")
            pyautogui.alert("Volume Muted")



        elif "ip address" in query:
            ip = get("https://www.opentracker.net/feature/ip-tracker/")
            speak(f"your IP address is{ip}")



        elif "temperature" in query:
            search = ""
            url = f"https://www.google.com/search?q={search}"
            r=requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            speak(f"current{search}is{temp}")

        elif"open drive" in query:
            webbrowser.open("https://drive.google.com/drive/u/0/my-drive")
            speak("Your google drive is opened")





        elif "open udemy" in query:
            webbrowser.open("www.udemy.com")
            speak("Opening Google to search your result")

        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            speak("Your socialmedia account is opened ")

        elif "photo" in query:
            webbrowser.open("https://photos.google.com/?tab=rq&pageId=none")
            speak("Here is your gallery")


        elif "open camera" in query:
            vid = cv2.VideoCapture(0)

            while (True):

                # Capture the video frame
                # by frame
                ret, frame = vid.read()


                cv2.imshow('frame', frame)


                if cv2.waitKey(1) & 0xFF == ord('q'
                                                ):
                    break

            vid.release()
            # Destroy all the windows
            cv2.destroyAllWindows()

        elif "weather today" in query:
            webbrowser.open("https://www.accuweather.com/en/in/india-weather")

        elif "open gaana" in query:
            webbrowser.open("https://gaana.com/")
            speak("Opening ganna")


        elif "logout" in query:
            os.system("shutdown -1")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play music" in query:
            songs_dir = 'D:\\Music'
            speak("PLAYing sir  ")
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))



        elif "remember that" in query:
            speak("what should i remember sir?")
            data = takeCommand()
            speak("you said me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()



        elif 'do you know anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())


        elif 'screenshot' in query:
            screenshot()
            speak("Done screen shot and saved to your screenshot folder!")
        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            jokes()

        elif 'offline' in query:
            speak("Bye sir . HAVE A GREAT DAY")
            quit()

        elif 'good night' in query:
            speak("Good Night sir. Sweet Dreams")
            quit()
        elif 'good morning' in query:
            speak("Good morning sir, Have a graet day")