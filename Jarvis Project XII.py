import webbrowser
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import requests
from bs4 import BeautifulSoup
import cv2
import psutil
import speedtest
import pyautogui
from Whatsapp import WhatsAppMsg
from Whatsapp import WhatsAppCall
from Whatsapp import WhatsAppVdCall
from os import startfile
from pyautogui import click
from time import sleep
from keyboard import write
from keyboard import press
import screen_brightness_control as sbc
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import asyncio
from pywizlight import wizlight, PilotBuilder, discovery, PilotParser
import random
import array
from enum import IntEnum
import folium
Key = "dc61cc311ec545859fc06cc9a2545715"


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 16:
        speak("Good afternoon")

    else:
        speak("Good Evening!")

    speak("Jarvis at your service. How may I help you ?")


def takeCommand():            #taking microphone input from the user and returning it as a string function

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Pardon, I couldn't get you. Please try again...")
        speak("pardon, I couldn't get you. please try again...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()                # lowercase helps python to easily match command with the written code.

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia .....")                      #need to check what's wrong with this
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open classroom' in query:
            webbrowser.open("https://www.classroom.google.com/u/1/c/ODE3NzUwOTQ0NjFa.com")

        elif 'open amazon' in query:
            webbrowser.open("https://www.amazon.in")

        elif 'open netflix' in query:
            webbrowser.open("https://www.netflix.com")

        elif 'prime video' in query:
            webbrowser.open("https://www.primevideo.com")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com")

        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com")

        elif'open meet' in query:
            webbrowser.open("https://meet.google.com/")

        elif 'covid status' in query:
            webbrowser.open("https://covid19.who.int/")

        elif 'show me my location' in query:
            webbrowser.open("https://www.google.com/maps/place/my+location/")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com/mail/u/1/#inbox")

        elif 'google calendar' in query:
            speak("What task shall i add to the google calendar ?")
            task_for_google_calendar = takeCommand()
            webbrowser.open("https://calendar.google.com/calendar/u/1/r?tab=wc&pli=1")
            sleep(2)
            click(x=200, y=373)
            click(x=200, y=373)     # not clicking the right button
            sleep(1)
            click(x=199, y=569)
            sleep(1)
            write(task_for_google_calendar)
            sleep(2)
            press('enter')
            speak("Task has been added to your google calendar")
            print("Task has been added to your google calendar")

        elif 'wind conditions' in query:
            webbrowser.open("https://www.windy.com")

        elif 'start an instant google meeting' in query:
            webbrowser.open('https://meet.google.com/')
            sleep(5)
            click(x=431, y=1364)
            sleep(1)
            click(x=362, y=1461)
            sleep(3)
            print('Instant new meeting has now started on google meet')
            speak('Instant new meeting has now started on google meet')

        elif 'open adobe reader' in query:
            startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Adobe Acrobat DC.lnk")

        elif 'open chrome' in query:
            startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'open powerpoint presentation' in query:
            speak("Opening powerpoint presentation")
            print("Opening  powerpoint presentation")
            click(x=67, y=2092)
            sleep(0.5)
            write('powerpoint')
            sleep(2)
            click(x=490, y=836)
            sleep(5)
            speak("Your new powerpoint presentation window has been opened")
            print("Your new powerpoint presentation window has been opened")

        elif 'set alarm' in query:
            print("At which hour do you want the alarm to ring ?")
            speak("At which hour do you want the alarm to ring ?")
            hour_alarm = int(takeCommand())
            sleep(1)
            print(f"How many minutes past {hour_alarm} ?")
            speak(f"How many minutes past {hour_alarm} ?")
            minute_alarm = int(takeCommand())
            sleep(1)
            click(x=67, y=2091)
            sleep(0.5)
            write('alarm')
            sleep(2)
            click(x=490, y=836)
            sleep(2)
            click(x=224, y=279)
            sleep(1)
            click(x=3730, y=1937)
            sleep(2)
            for i in range(hour_alarm-7):
                pyautogui.click(x=1776, y=541)
            sleep(1)
            for j in range(minute_alarm):
                pyautogui.click(x=2048, y=543)
            sleep(1)
            print("Do you want to give a special name to the alarm ?")
            speak("Do you want to give a special name to the alarm ?")
            response_to_query_for_alarm = takeCommand()
            if response_to_query_for_alarm == 'yes':
                print("What name do you want to give the alarm ?")
                speak("What name do you want to give the alarm ?")
                alarm_name = takeCommand()
                sleep(1)
                click(x=1915, y=933)
                sleep(0.5)
                write(alarm_name)
                sleep(1)
            elif response_to_query_for_alarm == 'no':
                print("Okay")
                speak("Okay")
                sleep(1)
            print("Do you want the alarm to repeat on certain days ?")
            speak("Do you want the alarm to repeat on certain days ?")
            response_to_repeat_days = takeCommand()
            if response_to_repeat_days == 'yes':
                click(x=1624, y=1052)
                sleep(1.5)
                print("On which days ?")
                speak("On which days ?")
            days_repeat = takeCommand()
            if days_repeat == 'everyday':
                click(x=1640, y=1157)
                sleep(1)
                click(x=1725, y=1150)
                sleep(1)
                click(x=1817, y=1153)
                sleep(1)
                click(x=1906, y=1154)
                sleep(1)
                click(x=1999, y=1151)
                sleep(1)
                click(x=2087, y=1154)
                sleep(1)
                click(x=2177, y=1153)
                sleep(1)
            elif days_repeat == 'monday':
                click(x=1640, y=1157)
                sleep(1)
            elif days_repeat == 'tuesday':
                click(x=1725, y=1150)
                sleep(1)
            elif days_repeat == 'wednesday':
                click(x=1817, y=1153)
                sleep(1)
            elif days_repeat == 'thursday':
                click(x=1906, y=1154)
                sleep(1)
            elif days_repeat == 'friday':
                click(x=1999, y=1151)
                sleep(1)
            elif days_repeat == 'saturday':
                click(x=2087, y=1154)
                sleep(1)
            elif days_repeat == 'sunday':
                click(x=2177, y=1153)
                sleep(1)
            click(x=1758, y=1581)
            sleep(1)
            print(f"Alarm set at {hour_alarm} {minute_alarm}")
            speak(f"Alarm set at {hour_alarm} {minute_alarm}")

        elif 'current screen brightness' in query:
            current_brightness = sbc.get_brightness()
            print(f"Current brightness level is at {current_brightness} %")
            speak(f"Current brightness level is at {current_brightness} %")
        elif 'change screen brightness' in query:
            print("What brightness level shall I set for the display ?")
            speak("What brightness level shall I set for the display ?")
            brightness_level_change = takeCommand()
            sbc.set_brightness(brightness_level_change)
            print(f"Brightness level of the display is now set to {brightness_level_change} %")
            speak(f"Brightness level of the display is now set to {brightness_level_change} %")
        elif 'set brightness to minimum' in query:
            sbc.set_brightness(0)
            print("Minimum brightness level set")
            speak("Minimum brightness level set")
        elif 'set brightness to maximum' in query:
            sbc.set_brightness(100)
            print("Maximum brightness level set")
            speak("Maximum brightness level set")

        elif 'play music' in query:
            music_dir = 'C:\\FavSongs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'show me a quick update' in query:
            click(x=508, y=2095)
            speak("Quick update is being displayed now")
            print("Quick update is being displayed now")

        elif 'translate' in query:
            print("From which language do you want me to translate? ")
            speak("From which language do you want me to translate? ")
            translate_from = takeCommand()
            print(f"To which language shall I convert {translate_from} ? ")
            speak(f"To which language shall I convert {translate_from} ? ")
            translate_to = takeCommand()
            print(f"Type in the extract that you want me to translate from {translate_from} to {translate_to}")
            speak(f"Type in the extract that you want me to translate from {translate_from} to {translate_to}")
            extract_to_be_translated = input(f"Type in the extract that you want me to translate from {translate_from} to {translate_to} here ==> ")
            webbrowser.open("https://www.google.com/search?rlz=1C1UEAD_enIN927IN927&q=google+translate&spel\
            l=1&sa=X&ved=2ahUKEwjil6D7k_fyAhVjILcAHY4_BsAQBSgAegQIARAx&biw=1552&bih=772")
            sleep(3)
            click(x=785, y=650)
            sleep(0.5)
            write(translate_from)
            sleep(1)
            click(x=747, y=706)
            sleep(1)
            click(x=538, y=813)
            click(x=538, y=813)
            write(extract_to_be_translated)
            sleep(3)
            click(x=1537, y=650)
            write(translate_to)
            sleep(1)
            click(x=747, y=706)
            sleep(2)
            print("Translation via Google translate complete")
            speak("Translation via Google translate complete")
            sleep(2)
            speak(f"The translated form of the given extract from {translate_from} to {translate_to} is: ")
            sleep(1)
            click(x=1460, y=985)

        elif 'book hotel room' in query:
            webbrowser.open("https://www.google.com/travel/hotels/Mumbai?tcfs=ChMKCC9tLzBjdnc5GgdLb2xrYXRhEiwKCC9tLzA0dm\
            1wEgZNdW1iYWkaGAoKMjAyMS0xMS0xNhIKMjAyMS0xMS0xNxgDIhgKCjIwMjEtMTEtMTYSCjIwMjEtMTEtMTdSAmAB&ts=CAESDgoCCAMKAg\
            gDCgIIAxAAGjQKFhISCggvbS8wNHZtcDoGTXVtYmFpGgASGhIUCgcI5Q8QCxgQEgcI5Q8QCxgRGAEyAggBKgsKBygBOgNJTlIaAA&ved=0CA\
            AQ5JsGahgKEwj4nuKAjYDyAhUAAAAAHQAAAAAQvAU&ictx=3&hl=en&gl=in&rp=OAE")
            sleep(1)
            speak("In which hotel do you want to make a reservation ?")
            print("In which hotel do you want to make a reservation ?")
            hotel_name = takeCommand()
            click()
            write(hotel_name)
            speak("When do you want to check-in ?")
            print("When do you want to check-in ?")
            check_in = takeCommand()
            click()

        elif 'book flight tickets' in query:
            webbrowser.open("https://www.google.com/flights?sxsrf=ALeKk03xk5jVA8W1csWbYmpDWwsqG6uXzg%3A1627280679677&source\
            =flun&uitype=cuA_&hl=en&gl=in&curr=INR&tfs=CAEQARoVEgoyMDIxLTA4LTExagcIARIDQk9NGhUSCjIwMjEtMDgtMTVyBwgBEgNCT016\
            ZENqUklNRTVEVmpRNVlqZE1ORFJCWVRWNFdHZENSeTB0TFMwdExTMHRMUzEwYkd0ek4wRkJRVUZCUjBRdFZsTmpUVE51UTBGQkVnRTJHZ29JOEI0\
            UUFCb0RTVTVTT0FOd3ZTaz0%3D&ved=2ahUKEwiblPL2jIDyAhXcDnIKHd98C-cQlhd6BAgGEAw")
            sleep(2)
            print("What will be the origin location for the travel ?")
            speak("What will be the origin location for the travel ?")
            origin_location_travel = takeCommand()
            print("What will be the destination ?")
            speak("What will be the destination ?")
            destination_of_travel = takeCommand()
            click(x=1118, y=1301)
            sleep(1)
            press('backspace')
            sleep(0.5)
            write(origin_location_travel)
            sleep(0.5)
            click(x=1308, y=1416)
            sleep(1)
            click(x=1738, y=1285)
            sleep(1)
            write(destination_of_travel)
            sleep(0.5)
            click(x=1900, y=1405)
            print("Set the required fields and you will be able to book the ticket")
            speak("Set the required fields and you will be able to book the ticket")
            sleep(60)
            click(x=2982, y=1926)
            print("Now you can choose the flights as you want to")
            speak("Now you can choose the flights as you want to")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Right now,the time is {strTime}")
            print(f"Right now,the time is {strTime}")

        elif 'weather today' in query:
            webbrowser.open("https://www.google.com/search?q=weather+today+&rlz=1C1UEAD_enIN927IN927&sxsrf=ALeKk02ybSRf\
            ACPWbqdZDvrNpDlq3n4p3w%3A1626373050360&ei=unvwYPjGFZHB9QOimZnIBA&oq=weather+today+&gs_lcp=Cgdnd3Mtd2l6EAMyBA\
            gjECcyCwgAELEDEIMBEJECMgsIABCxAxCDARCRAjIFCAAQkQIyBQgAEJECMgUIABCxAzIICAAQsQMQgwEyCAgAELEDEIMBMggIABCxAxCDATI\
            ICAAQsQMQgwE6BwgAEEcQsANKBAhBGABQ3yRY0C1gxjBoAXACeACAAeUBiAG0D5IBBTAuNi40mAEAoAEBqgEHZ3dzLXdpesgBCMABAQ&sclient\
            =gws-wiz&ved=0ahUKEwj4i8Hf1-XxAhWRYH0KHaJMBkkQ4dUDCA4&uact=5")

        elif 'track flights' in query:
            webbrowser.open('https://www.flightradar24.com')

        elif 'open weather app' in query:
            click(x=67, y=2093)
            sleep(1)
            write('Weather app')
            sleep(2)
            click(x=466, y=863)
            sleep(1)
            print('Weather app is now open')
            speak('Weather app is now open')

        elif 'microsoft news app' in query:
            click(x=64, y=2088)
            sleep(1)
            click(x=529, y=507)
            sleep(1)
            write('Microsoft news')
            sleep(1)
            click(x=516, y=872)
            sleep(1)
            print('Microsoft news app is now open')
            speak('Microsoft news app is now open')

        elif 'microsoft store' in query:
            click(x=64, y=2088)
            sleep(1)
            click(x=529, y=507)
            sleep(1)
            write('Microsoft store')
            sleep(1)
            click(x=516, y=872)
            sleep(1)
            print('Microsoft store app is now open')
            speak('Microsoft store app is now open')

        elif 'lightroom' in query:
            click(x=64, y=2088)
            sleep(1)
            click(x=529, y=507)
            sleep(1)
            write('Adobe Lightroom')
            sleep(1)
            click(x=516, y=872)
            sleep(1)
            print('Adobe Lightroom app is now open')
            speak('Adobe Lightroom app is now open')

        elif 'show my photos' in query:
            click(x=64, y=2088)
            sleep(1)
            click(x=529, y=507)
            sleep(1)
            write('Photos')
            sleep(1)
            click(x=516, y=872)
            sleep(1)
            print('You can now see your photos')
            speak('You can now see your photos')

        elif 'open settings' in query:
            click(x=64, y=2088)
            sleep(1)
            click(x=529, y=507)
            sleep(1)
            write('Settings')
            sleep(1)
            click(x=516, y=872)
            sleep(1)
            print('Settings now open')
            speak('Settings now open')

        elif 'close the window' in query:
            click(x=3780, y=26)
            sleep(1)
            print("Are you sure you want to exit Pycharm ?")
            speak("Are you sure you want to exit Pycharm ?")
            answer_close = takeCommand()
            if 'yes' in answer_close:
                click(x=2016, y=1119)
            if 'no' in answer_close:
                click(x=2202, y=1124)

        elif 'search google' in query:
            print("What shall I search on Google?")
            speak("What shall I search on Google?")
            query_google_search = takeCommand()
            webbrowser.open(f"https://www.google.com/search?q={query_google_search}")

        elif 'search youtube' in query:
            print("What shall I search on Youtube ?")
            speak("What shall I search on Youtube ?")
            query_youtube = takeCommand()
            webbrowser.open(f"https://www.youtube.com/results?search_query={query_youtube}")

        elif 'temperature' in query:
            search = "temperature in Mumbai"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current {search} is {temp}")
            print(f"current {search} is {temp}")

        elif 'weather map' in query:
            webbrowser.open("https://www.windy.com/-Temperature-temp?temp,19.075,72.886,5")

        elif 'news' in query:
            webbrowser.open("https://www.google.com/search?q=news+today&rlz=1C1UEAD_enIN927IN927&sxsrf=ALeKk00cBhYzvDPEV\
            0Xep3AjRc4oEGVFZQ%3A1626402659890&ei=Y-_wYLj4Neec4-EPh--JkAQ&oq=news+today&gs_lcp=Cgdnd3Mtd2l6EAMyBwgAELEDEE\
            MyBQgAELEDMgUIABCxAzIFCAAQsQMyAggAMgUIABCxAzIFCAAQsQMyBQgAELEDMgIIADIFCAAQsQM6BwgAEEcQsAM6CggAELADEMkDEEM6CAg\
            AEJIDELADOgQIABBDOgoIABCxAxCDARBDOgoIABCHAhCxAxAUSgQIQRgAUIGUC1iqnAtg2p4LaAFwAngAgAG-AogByAmSAQcwLjYuMC4xmAEA\
            oAEBqgEHZ3dzLXdpesgBCsABAQ&sclient=gws-wiz&ved=0ahUKEwj4tbeGxubxAhVnzjgGHYd3AkIQ4dUDCA4&uact=5")

        elif 'open camera' in query:
            captureDevice = cv2.VideoCapture(0)  # captureDevice = camera
            while True:
                ret, frame = captureDevice.read()
                frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if cv2.waitKey(10) & 0xFF == ord('q'):
                    break
                cv2.imshow('my frame', frame)

            captureDevice.release()
            cv2.destroyAllWindows()

        elif 'open the camera app' in query:
            speak("Opening camera app")
            print("Opening camera app")
            click(x=69, y=2093)
            sleep(1)
            write('camera')
            sleep(1)
            click(x=469, y=866)
            speak("Camera app is now opened")
            print("Camera app is now opened")

        elif 'click a photo' in query:
            speak("Just a moment")
            print("Just a moment")
            click(x=69, y=2093)
            write('camera')
            sleep(1)
            click(x=469, y=866)
            sleep(5)
            speak("3 .......2 ........1 ..Say cheeeeeeeese !!")
            print("3 .......2 ........1 ..Say cheeeeeeeese !!")
            click(x=3733, y=1053)
            speak("Click")

        elif 'shoot a video' in query:
            speak("Just a moment")
            print("Just a moment")
            click(x=69, y=2093)
            write('camera')
            sleep(1)
            click(x=469, y=866)
            sleep(3)
            click(x=3726, y=873)
            click(x=3726, y=873)
            sleep(5)
            speak("Lights ....... camera ........ annnnddddd action !!")
            print("Camera now rolling")
            click(x=3733, y=1053)

        elif 'order food' in query:
            speak("From which restaurant ?")
            print("From which restaurant ?")
            swiggy_order = takeCommand()
            webbrowser.open("https://www.swiggy.com/restaurants")
            sleep(5)
            click(x=2009, y=312)
            sleep(1)
            write(swiggy_order)
            press('enter')
            sleep(1)
            click(x=1029, y=748)
            sleep(2)
            click(x=1198, y=1183)
            sleep(2)
            speak(f"Now you can choose what you want to order from {swiggy_order}")

        elif 'amazon' in query:
            speak("What shall I search on amazon ?")
            product_item = takeCommand()
            webbrowser.open(f"https://www.amazon.in/s?k={product_item}")
            speak("item search on amazon is complete")
            print("item search on amazon is complete")
            speak("Do you want me to add the first item on this list to your cart ?")
            print("Do you want me to add the first item on this list to your cart ?")
            response_to_amazon_search = takeCommand()
            if response_to_amazon_search == 'yes':
                click(x=1028, y=1628)
                sleep(5)
                click(x=3124, y=1683)
                sleep(2)
                speak("Item has been added to your cart")
                print("Item has been added to your cart")
            elif response_to_amazon_search == 'no':
                speak("Do you want to buy this item right now instead of adding it to cart ?")
                print("Do you want to buy this item right now instead of adding it to cart ?")
                response_to_ques = takeCommand()
                if response_to_ques == 'yes':
                    click(x=1028, y=1628)
                    sleep(5)
                    click(x=3116, y=1783)
                    speak("You can now provide the necessary details and buy the product")
                    print("You can now provide the necessary details and buy the product")
                else:
                    speak("Enjoy your shopping")
                    print("Enjoy your shopping")

        elif 'flipkart' in query:
            speak("What shall I search on flipkart ?")
            product_item_flip = takeCommand()
            webbrowser.open(f"https://www.flipkart.com/search?q={product_item_flip}")
            speak("item search on flipkart is complete")
            print("item search on flipkart is complete")
            speak("Do you want me to add the first item on this list to your cart ?")
            print("Do you want me to add the first item on this list to your cart ?")
            response_to_flipkart_search = takeCommand()
            if response_to_flipkart_search == 'yes':
                click(x=928, y=957)
                sleep(5)
                click(x=801, y=1564)
                speak("item has been added to your cart")
                print("item has been added to your cart")
            elif response_to_flipkart_search == 'no':
                speak("Do you want to buy this item right now instead of adding it to cart?")
                print("Do you want to buy this item right now instead of adding it to cart?")
                response_to_ques = takeCommand()
                if response_to_ques == 'yes':
                    click(x=928, y=957)
                    sleep(5)
                    click(x=1316, y=1570)
                    speak("You can now provide the necessary details and buy the product ")
                    print("You can now provide the necessary details and buy the product ")
                else:
                    speak("Enjoy your shopping")
                    print("Enjoy your shopping")

        elif 'weather' in query:
            speak("Weather about which place do you want to know ?")
            weather_location = takeCommand()
            search = f"temperature in {weather_location}"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current {search} is {temp}")
            print(f"current {search} is {temp}")

        elif 'calculate' in query:
            print("Please tell me the numbers that you want to calculate")
            speak("Please tell me the numbers that you want to calculate")
            print("What is the first number ?")
            speak("What is the first number ?")
            num1 = int(takeCommand())
            print(num1)
            print("What is the second number ?")
            speak("What is the second number ?")
            num2 = int(takeCommand())
            print(num2)
            speak("what mathematical calculation do you want me to perform on these ")
            operation_on_numbers = takeCommand()
            if 'addition' in operation_on_numbers:
               sum = num1 + num2
               speak(f"The sum of the two numbers is: {sum}",)
               print("The sum of the two numbers is: ", sum)
            elif 'subtraction' in operation_on_numbers:
                difference = num1 - num2
                speak(f"The difference between the numbers is{difference}")
                print("The difference between the two numbers is: ", difference)

            elif 'multiplication' in operation_on_numbers:
                product = num1*num2
                speak(f"The product of the two numbers is{product}")
                print("The product of the two numbers is: ", product)

            elif 'division' in operation_on_numbers:
                quotient = num1/num2
                speak(f"The quotient obtained upon dividing the two numbers is{quotient}")
                print("The quotient obtained upon dividing the two numbers is: ", quotient)

            elif 'route' in operation_on_numbers:   #mathematically 'root' but for the system to understand pronunciation 'root' is replaced by 'route'
                nth_root = num1**(1/num2)
                speak(f"The required root is{nth_root}")
                print("The required root is", nth_root)

            elif 'power exponent' in operation_on_numbers:
                nth_power = num1**num2
                speak(f"The result is{nth_power}")
                print("The result is: ", nth_power)

        elif 'battery percentage' in query or 'how much power is remaining' in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"The laptop has {percentage} percent battery")
            print(f"The laptop has {percentage} percent battery")
            if percentage == 100:
                speak("Laptop is fully charged. You may remove the charging cable now")
                print("Laptop is fully charged. You may remove the charging cable now")
            if 75 <= percentage < 100:
                speak("We have enough juice to power through our work ")
                print("We have enough juice to power through our work ")
            elif 30 <= percentage <= 75:
                speak("We should probably connect the charger after a little while")
                print("We should probably connect the charger after a little while")
            elif 20 <= percentage <= 30:
                speak("Now would be a good time to connect the charger to the laptop")
                print("Now would be a good time to connect the charger to the laptop")
            elif 5 <= percentage <= 20:
                speak("Battery saver mode has been activated. Please connect the charger to the laptop now")
                print("Battery saver mode has been activated. Please connect the charger to the laptop now")
            elif 1 <= percentage <= 5:
                speak("BATTERY LEVEL CRITICAL. REPEAT, BATTERY LEVEL CRITICAL. CONNECT THE CHARGER RIGHT NOW IF YOU WISH TO CONTINUE YOUR WORK !!!")
                print("BATTERY LEVEL CRITICAL. REPEAT, BATTERY LEVEL CRITICAL. CONNECT THE CHARGER RIGHT NOW IF YOU WISH TO CONTINUE YOUR WORK !!!")

        elif 'internet speed' in query:
            spdst = speedtest.Speedtest()
            dwnld = spdst.download()
            uplnk = spdst.upload()
            dwnld_in_mbps = dwnld*0.000001                                                                                   # These two function return the value in mbps using 1 Mbps = 10**6 bits per second
            dwnld_in_mbps_conversion = str(dwnld_in_mbps)
            dwnld_in_mbps_round_off = (dwnld_in_mbps_conversion[0:7])
            uplnk_in_mbps = uplnk*0.000001                                                                                   # because by default the function returns value in bits per second and we need mbps
            uplnk_in_mbps_conversion = str(uplnk_in_mbps)
            uplnk_in_mbps_round_off = (uplnk_in_mbps_conversion[0:])
            speak(f"The downloading speed is {dwnld_in_mbps_round_off} Mbp s and the uploading speed is {uplnk_in_mbps_round_off} Mbp s")
            print(f"The downloading speed is {dwnld_in_mbps_round_off} Mbp s and the uploading speed is {uplnk_in_mbps_round_off} Mbp s")

        elif 'take a screenshot' in query:
            screenshot_img = pyautogui.screenshot()
            speak("Screenshot taken")
            speak("By what name shall I save the screenshot?")
            print("By what name shall I save the screenshot?")
            img_name = takeCommand()
            screenshot_img.save(f"C:\\Bhutu CLASS XII\\CS\\python_project_ss\\{img_name}.png")
            speak("The screenshot has been saved in the designated file")
            speak("Opening the screenshot in file")
            path = f"C:\\Bhutu CLASS XII\\CS\\python_project_ss\\{img_name}.png"
            os.startfile(path)

        elif 'open whatsapp' in query:
            startfile("C:\\Users\\Rajdeep Mukherjee\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            sleep(5)
            speak("WhatsApp is now open")

        elif 'whatsapp message' in query:
            speak("Whom do you want to send the text ?")
            name_of_recipient = takeCommand()
            speak(f"What shall I say in the text to {name_of_recipient} ?")
            message_to_be_sent = takeCommand()
            WhatsAppMsg(name_of_recipient, message_to_be_sent)
            speak(f"Message sent to {name_of_recipient} ")

        elif 'whatsapp call' in query:
            speak("Whom shall I call on WhatsApp ?")
            name_of_who_i_want_to_call = takeCommand()
            speak(f"Calling {name_of_who_i_want_to_call} on WhatsApp right away")
            WhatsAppCall(name_of_who_i_want_to_call)

        elif 'whatsapp video call' in query:
            speak("With whom shall I start a video call on WhatsApp ?")
            name_of_who_i_want_to_vdcall = takeCommand()
            speak(f"Video calling {name_of_who_i_want_to_vdcall} on WhatsApp right away")
            WhatsAppVdCall(name_of_who_i_want_to_vdcall)

        elif 'locate phone number' in query:
            speak("Please enter the number along with the country code")
            number = input("Please enter the number along with the country code ==> ")
            number_in_query = phonenumbers.parse(number)
            your_Location = geocoder.description_for_number(number_in_query, "en")
            print(f"Phone number located. It is in {your_Location}")
            speak(f"Phone number located. It is in {your_Location}")

            print("Do you want me to find out the I S P of the number ?")
            speak("Do you want me to find out the I S P of the number ?")
            response_number_isp = takeCommand()
            if 'yes' in response_number_isp:
                service_provider = phonenumbers.parse(number)
                name_of_isp = carrier.name_for_number(service_provider, "en")
                print(f"I S P of the phone number is: {name_of_isp}")
                speak(f"I S P of the phone number is {name_of_isp}")

            print("Do you also want to see the location on world map ?")
            speak("Do you also want to see the location on world map ?")
            response_to_location = takeCommand()
            if 'yes' in response_to_location:
                geocoder = OpenCageGeocode(Key)
                query1 = str(your_Location)
                results = geocoder.geocode(query1)
                # print(results)
                lat = results[0]['geometry']['lat']
                lng = results[0]['geometry']['lng']
                print(lat, lng)
                myMap = folium.Map(location=[lat, lng], zoom_start=5)
                folium.Marker([lat, lng], popup=your_Location).add_to(myMap)
                myMap.save("my_location.html")
                sleep(1)
                print("Location of the phone number on map coming up")
                speak("Location of the phone number on map coming up")
                startfile("C:\\Users\\Rajdeep Mukherjee\\PycharmProjects\\pythonProject1\\my_location.html")
                sleep(2)
                click(x=3385, y=304)
                click(x=3385, y=304)
                print("Now you can see the location of the phone on the world map")
                speak("Now you can see the location of the phone on the world map")

        elif 'restart laptop' in query:
            click(x=68, y=2094)
            sleep(2)
            click(x=1299, y=1934)
            sleep(0.5)
            click(x=1303, y=1843)
            click(x=1303, y=1843)

        elif 'shutdown laptop' in query:
            click(x=68, y=2094)
            sleep(2)
            click(x=1299, y=1934)
            sleep(0.5)
            click(x=1310, y=1771)
            click(x=1310, y=1771)

        elif 'put laptop on sleep mode' in query:
            click(x=68, y=2094)
            sleep(2)
            click(x=1299, y=1934)
            sleep(0.5)
            click(x=1292, y=1697)
            click(x=1292, y=1697)

        elif 'volume up' in query:
            pyautogui.press('volumeup')

        elif 'maximum volume' in query:
            pyautogui.press('volumeup', presses=50)
            print("Media volume set to maximum")
            speak("Media volume set to maximum")

        elif 'volume down' in query:
            pyautogui.press('volumedown')

        elif 'minimum volume' in query:
            pyautogui.press('volumedown', presses=50)
            print("Media volume set to minimum")
            speak("Media volume set to minimum")                # won't be able to hear this because media volume=0 then

        elif 'smart light control' in query:
            async def main():
                """Own code to work with bulbs."""
                # Discover all bulbs in the network via broadcast datagram (UDP)
                # function takes the discovery object and returns a list with wizlight objects.
                bulbs = await discovery.discover_lights(broadcast_space="192.168.0.106")
                # Print the IP address of the bulb on index 0
                print(f"Bulb IP address: {bulbs[0].ip}")

                # Iterate over all returned bulbs
                for bulb in bulbs:
                    print(bulb.__dict__)
                    # Turn off all available bulbs
                    # await bulb.turn_off()

                # Set up a standard light
                light = wizlight("192.168.0.106")
                # Set up the light with a custom port
                # light = wizlight("your bulb's IP address", port=12345)

                # The following calls need to be done inside an asyncio coroutine
                # to run them from normal synchronous code, you can wrap them with
                # asyncio.run(..).

                print('What do you want me to do with the smart lights ?')
                speak('What do you want me to do with the smart lights ?')
                response_to_query_for_lights = takeCommand()
                if 'switch on' in response_to_query_for_lights:
                    await light.turn_on(PilotBuilder())                # Turn on the light into "rhythm mode"
                    await light.turn_on(PilotBuilder(brightness=255))  # Set bulb brightness
                    timeout = 10
                    await asyncio.wait_for(light.turn_on(PilotBuilder(brightness=255)), timeout)         # Set bulb brightness (with async timeout)
                    print('Smart light has been switched on')
                    speak('Smart light has been switched on')

                if 'switch off' in response_to_query_for_lights:
                    await light.turn_off()          # Turns the light off
                    print('Smart light has been switched off')
                    speak('Smart light has been switched off')

                if 'maximum brightness' in response_to_query_for_lights:
                    await light.turn_on(PilotBuilder(brightness=255))
                if 'minimum brightness' in response_to_query_for_lights:
                    await light.turn_on(PilotBuilder(brightness=0))

                if 'custom brightness' in response_to_query_for_lights:
                    print("What brightness level between 0 and 255 should I set for the light?")
                    speak("What brightness level between 0 and 255 should I set for the light?")
                    brightness_level_value = int(takeCommand())
                    await light.turn_on(PilotBuilder(brightness=brightness_level_value))

                if 'set colour to warm white' in response_to_query_for_lights:
                    await light.turn_on(PilotBuilder(warm_white=255))   # Set bulb to warm white
                    print('Colour has been set to warm white')
                    speak('Colour has been set to warm white')

                if 'custom colour' in response_to_query_for_lights:
                    print('What shall I set for red?')
                    speak('What shall I set for red?')
                    red = int(takeCommand())
                    print('What shall I set for green?')
                    speak('What shall I set for green?')
                    green = int(takeCommand())
                    print('What shall I set for blue?')
                    speak('What shall I set for blue?')
                    blue = int(takeCommand())
                    await light.turn_on(PilotBuilder(rgb=(red, green, blue)))    # Set RGB values red to 0 = 0%, green to 128 = 50%, blue to 255 = 100%
                    print('Custom colour now available')
                    speak('Custom colour now available')

                if 'current colour temperature' in response_to_query_for_lights:
                    state = await light.updateState()          # Get the current color temperature, RGB values
                    print(state.get_colortemp())
                    speak(f"Colour temperature is {state.get_colortemp()}")
                    red, green, blue = state.get_rgb()
                    print(f"red {red}, green {green}, blue {blue}")
                    speak(f"red {red}, green {green}, blue {blue}")

                if 'start scene 4' in response_to_query_for_lights:
                    await light.turn_on(PilotBuilder(scene=4))  # party # Start a scene
                    print('Party scene has now been set')
                    speak('Party scene has now been set')

                if 'current mode selected' in response_to_query_for_lights:
                    state = await light.updateState() # Get the name of the current scene
                    print('Current scene set is: ', state.get_scene())
                    speak(f'Current scene set is: {state.get_scene()}')

                if 'bulb features' in response_to_query_for_lights:
                    bulb_type = await bulbs[0].get_bulbtype() # Get the features of the bulb
                    print('bulb brightness supported ==> ', bulb_type.features.brightness)  # returns true if brightness is supported
                    speak(f'bulb brightness supported ? {bulb_type.features.brightness}')
                    print('bulb colours supported ==> ', bulb_type.features.color)  # returns true if color is supported
                    speak(f'bulb colours supported ? {bulb_type.features.color}')
                    print('bulb colour temperature supported ==> ', bulb_type.features.color_tmp)  # returns true if color temperatures are supported
                    speak(f'bulb colour temperature supported ?{bulb_type.features.color_tmp}')
                    print('bulb effects supported ==> ', bulb_type.features.effect)  # returns true if effects are supported
                    speak(f'bulb effects supported ? {bulb_type.features.effect}')
                    print('bulb max temp supported ==> ', bulb_type.kelvin_range.max)  # returns max kelvin in in INT
                    speak(f'bulb max temp supported ? {bulb_type.kelvin_range.max}')
                    print('bulb min temp supported ==> ', bulb_type.kelvin_range.min)  # returns min kelvin in in INT
                    speak(f'bulb min temp supported ? {bulb_type.kelvin_range.min}')
                    print('bulb module name ==> ', bulb_type.name)  # returns the module name of the bulb
                    speak(f'bulb module name ? {bulb_type.name}')
                    print('bulb brightness ==> ', bulb_type.features.brightness)  # returns the brightness of the bulb
                    speak(f'bulb brightness ? {bulb_type.features.brightness}')

            loop = asyncio.get_event_loop()
            loop.run_until_complete(main())

        elif 'random password' in query:
            # maximum length of password needed
            # this can be changed to suit your password length
            MAX_LEN = 12

            # declare arrays of the character that we need in out password
            # Represented as chars to enable easy string concatenation
            DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                                 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                                 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                                 'z']

            UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                                 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                                 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                                 'Z']

            SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
                       '*', '(', ')', '<']

            # combines all the character arrays above to form one array
            COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

            # randomly select at least one character from each character set above
            rand_digit = random.choice(DIGITS)
            rand_upper = random.choice(UPCASE_CHARACTERS)
            rand_lower = random.choice(LOCASE_CHARACTERS)
            rand_symbol = random.choice(SYMBOLS)

            # combine the character randomly selected above
            # at this stage, the password contains only 4 characters but
            # we want a 12-character password
            temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

            # now that we are sure we have at least one character from each
            # set of characters, we fill the rest of
            # the password length by selecting randomly from the combined
            # list of character above.
            for x in range(MAX_LEN - 4):
                temp_pass = temp_pass + random.choice(COMBINED_LIST)

                # convert temporary password into array and shuffle to
                # prevent it from having a consistent pattern
                # where the beginning of the password is predictable
                temp_pass_list = array.array('u', temp_pass)
                random.shuffle(temp_pass_list)

            # traverse the temporary password array and append the chars
            # to form the password
            password = ""
            for x in temp_pass_list:
                password = password + x

            # print out password
            print(f'Random password generated as ==> {password}')
            speak('Random password generated')

        elif 'download youtube video' in query:
            speak("Please enter the url of the video that you want to download and save in your computer")
            youtube_url = input("Please enter the url of the video that you want to download and save in your computer ==> ")
            webbrowser.open(f"https://www.ss{youtube_url}")
            sleep(5)
            click(x=2489, y=745)
            sleep(5)
            click(x=1897, y=1335)
            sleep(10)
            print("The Youtube video has been downloaded")
            speak("The Youtube video has been downloaded")
            speak("Do you want me to play the video right now ?")
            video_query = takeCommand()
            if 'yes' in video_query:
                click(x=478, y=1999)
                sleep(3)
                click(x=547, y=1712)
                sleep(3)
                click(x=3696, y=0)
                print("The downloaded Youtube video is now playing")
                speak("The downloaded Youtube video is now playing")

        elif 'start scanner' in query:
            print("Accessing Camera to scan QR code")
            speak("Accessing Camera to scan QR code")
            cap = cv2.VideoCapture(0)
            # initialize the cv2 QRCode detector
            detector = cv2.QRCodeDetector()
            while True:
                _, img = cap.read()
                # detect and decode
                data, bbox, _ = detector.detectAndDecode(img)
                # check if there is a QRCode in the image
                if data:
                    a = data
                    break
                # display the result
                cv2.imshow("QRCODE scanner", img)
                if cv2.waitKey(1) == ord("q"):
                    break

            b = webbrowser.open(str(a))
            cap.release()
            cv2.destroyAllWindows()
            print("QR code scan complete")
            speak("QR code scan complete")

        elif 'price tracker' in query:

            headers = {
                "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
            }
            speak("Paste the amazon product's link")
            product_link = str(input("Paste the amazon product's link ==>"))
            response = requests.get(product_link, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            def check_price():
                title = soup.find(id="productTitle").get_text()
                price = soup.find(id="displayPrice").get_text().strip()
                print("Product name & specs: ", title.strip())
                speak(f"Product name & specs: {title.strip()}")
                print("Product cost: ", price)
                speak(f"Product cost: {price}")


            check_price()

        #elif 'play rock paper scissors with me' or "lets play rock paper scissors" in query:
            print("Okay, let's play!")
            speak("Okay, let's play!")

            class Action(IntEnum):
                Rock = 0
                Paper = 1
                Scissors = 2

            def get_user_selection():
                choices = [f"{action.name}[{action.value}]" for action in Action]
                choices_str = ", ".join(choices)
                print(f"Enter a choice ({choices_str}): ")
                speak(f"Enter a choice ({choices_str}): ")
                selection = int(takeCommand())
                action = Action(selection)
                return action

            def get_computer_selection():
                selection = random.randint(0, len(Action) - 1)
                action = Action(selection)
                return action

            def determine_winner(user_action, computer_action):
                if user_action == computer_action:
                    print(f"Both players selected {user_action.name}. It's a tie!")
                    speak(f"Both players selected {user_action.name}. It's a tie!")
                elif user_action == Action.Rock:
                    if computer_action == Action.Scissors:
                        print(f"I chose{computer_action}. Rock smashes scissors! You win!")
                        speak(f"I chose{computer_action}. Rock smashes scissors! You win!")
                    else:
                        print(f"I chose{computer_action}. Paper covers rock! You lose.")
                        speak(f"I chose{computer_action}. Paper covers rock! You lose.")
                elif user_action == Action.Paper:
                    if computer_action == Action.Rock:
                        print(f"I chose{computer_action}. Paper covers rock! You win!")
                        speak(f"I chose{computer_action}. Paper covers rock! You win!")
                    else:
                        print(f"I chose{computer_action}. Scissors cuts paper! You lose.")
                        speak(f"I chose{computer_action}. Scissors cuts paper! You lose.")
                elif user_action == Action.Scissors:
                    if computer_action == Action.Paper:
                        print(f"I chose{computer_action}. Scissors cuts paper! You win!")
                        speak(f"I chose{computer_action}. Scissors cuts paper! You win!")
                    else:
                        print(f"I chose{computer_action}. Rock smashes scissors! You lose.")
                        speak(f"I chose{computer_action}. Rock smashes scissors! You lose.")

            while True:
                try:
                    user_action = get_user_selection()
                except ValueError as e:
                    range_str = f"[0, {len(Action) - 1}]"
                    print(f"Invalid selection. Enter a value in range {range_str}")
                    continue
                computer_action = get_computer_selection()
                determine_winner(user_action, computer_action)

                print("Do you want to play again? (yes or no): ")
                speak("Do you want to play again? (yes or no): ")
                play_again = str(takeCommand())
                if play_again.lower() != "yes":
                    print("Game ended")
                    speak("Game ended")
                    break

            def determine_winner(user_action, computer_action):
                if user_action == computer_action:
                    print(f"Both players selected {user_action.name}. It's a tie!")
                    speak(f"Both players selected {user_action.name}. It's a tie!")
                elif user_action == Action.Rock:
                    if computer_action == Action.Scissors:
                        print("Rock smashes scissors! You win!")
                        speak("Rock smashes scissors! You win!")
                    else:
                        print("Paper covers rock! You lose.")
                        speak("Paper covers rock! You lose.")
                elif user_action == Action.Paper:
                    if computer_action == Action.Rock:
                        print("Paper covers rock! You win!")
                        speak("Paper covers rock! You win!")
                    else:
                        print("Scissors cuts paper! You lose.")
                        speak("Scissors cuts paper! You lose.")
                elif user_action == Action.Scissors:
                    if computer_action == Action.Paper:
                        print("Scissors cuts paper! You win!")
                        speak("Scissors cuts paper! You win!")
                    else:
                        print("Rock smashes scissors! You lose.")
                        speak("Rock smashes scissors! You lose.")

        elif 'colour detector' in query:

            import pandas as pd
            speak("Enter the name of the .jpg image file here")
            img_name = input("Enter the name of the .jpg image file here ==>")
            img_path = f'C:\\Bhutu CLASS XII\\CS\python_project_ss\\{img_name}.jpg'
            img = cv2.imread(img_path)

            # declaring global variables (are used later on)
            clicked = False
            r = g = b = x_pos = y_pos = 0

            # Reading csv file with pandas and giving names to each column
            index = ["color", "color_name", "hex", "R", "G", "B"]
            csv = pd.read_csv('colors.csv', names=index, header=None)


            # function to calculate minimum distance from all colors and get the most matching color
            def get_color_name(R, G, B):
                minimum = 10000
                for i in range(len(csv)):
                    d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
                    if d <= minimum:
                        minimum = d
                        cname = csv.loc[i, "color_name"]
                return cname


            # function to get x,y coordinates of mouse double click
            def draw_function(event, x, y, flags, param):
                if event == cv2.EVENT_LBUTTONDBLCLK:
                    global b, g, r, x_pos, y_pos, clicked
                    clicked = True
                    x_pos = x
                    y_pos = y
                    b, g, r = img[y, x]
                    b = int(b)
                    g = int(g)
                    r = int(r)


            cv2.namedWindow('image')
            cv2.setMouseCallback('image', draw_function)

            while True:

                cv2.imshow("image", img)
                if clicked:

                    # cv2.rectangle(image, start point, endpoint, color, thickness)-1 fills entire rectangle
                    cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

                    # Creating text string to display( Color name and RGB values )
                    text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

                    # cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
                    cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

                    # For very light colours we will display text in black colour
                    if r + g + b >= 600:
                        cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

                    clicked = False

                # Break the loop when user hits 'esc' key
                if cv2.waitKey(20) & 0xFF == 27:
                    break

            cv2.destroyAllWindows()

        elif 'currency conversion' in query:
            speak("Please enter the currency that you want to convert")
            crncy_to_convert = input("Enter the currency that you want to convert here ==> ")
            speak(f"To which currency do you want to convert {crncy_to_convert} ?")
            crncy_final = input(f"Enter the currency to which you want to convert {crncy_to_convert} to here ==> ")
            speak(f"Enter the amount to be converted from {crncy_to_convert} to {crncy_final} here")
            money_amount = input(f"Enter the amount to be converted from {crncy_to_convert} to {crncy_final} here ==> ")
            webbrowser.open("https://www.xe.com")
            sleep(3)
            click(x=1779, y=1263)
            sleep(1)
            write(f"{crncy_to_convert}")
            click(x=1841, y=1379)
            sleep(1)
            click(x=2680, y=1266)
            write(f"{crncy_final}")
            click(x=2763, y=1385)
            sleep(1)
            click(x=1052, y=1264)
            pyautogui.press("backspace", presses=20)
            write(f"{money_amount}")
            sleep(1)
            click(x=2971, y=1426)
            sleep(1)
            print(f"Currency conversion from {crncy_to_convert} to {crncy_final} complete")
            speak(f"Currency conversion from {crncy_to_convert} to {crncy_final} complete")






# ----------------------------------------------------------------------------------------------------------------------
# ______________________________________________________________________________________________________________________
# Special codes:
# add products in cart for amazon                                               [need to run code and check]
# search/add/buy products on flipkart                                           [done]
# all smart light controls                                                      [done]
# changing volume of media                                                      [done]
# changing brightness of screen                                                 [done]
# open camera                                                                   [done]
# flight tickets/hotel booking                                                  [done]
# location                                                                      [done]
# order food                                                                    [done]
# phone track                                                                   [done]
# add tasks to google calendar                                                  [done]
# set an alarm                                                                  [done]
# take a screenshot                                                             [done]
# text someone on whatsapp                                                      [done]
# call someone on whatsapp                                                      [done]
# take a photo and a video                                                      [done]
# google search                                                                 [done]
# youtube search                                                                [done]
# calculator                                                                    [done]
# internet speed                                                                [done]
# search and add item to cart or buy it on amazon/flipkart                      [done]
# shutdown restart and sleep the laptop                                         [done]
# phone track                                                                   [done]
# random password generator                                                     [done]
# YouTube video downloader                                                      [done]
# currency converter                                                            [done]
# rock paper scissor game                                                       [done]
# QR scanner                                                                    [done]
# Amazon price tracker                                                          [done]
# colour detector                                                               [done]
# google translator                                                             [done]


# This is an original source code inspired from the works of professional python programmers
# ----------------------------------------------------------------------------------------------------------------------
# NOTE: Once we get to know the coding basics, applying that for developing your
# digital personal assistant can give us infinite no. of possibilities of things to do.
# Since this is a project, less no. of applications are shown here.
# Copyrighted
# © All rights reserved to Rajdeep Mukherjee
# This is an original source code. Do not copy without proper consent ;))
