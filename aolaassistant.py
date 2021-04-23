import speech_recognition as sr
from datetime import datetime
import time
import os
from gtts import gTTS
import random
from playsound import playsound
from os import path
from pydub import AudioSegment

def listen():
    r = sr.Recognizer()
    with sr.Microphone(device_index = 0) as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, phrase_time_limit=4)
    data = ""
    try:
        data = r.recognize_google(audio)
        print(data)
        #if 'Paola' not in data.lower().split():
        #    return data
        #else:
            print(data)
    except sr.UnknownValueError:
        print("Google Speech Recognition did not understand audio")
    except sr.RequestError as e:
        print(f"Request Failed; {e}")
    return data


def respond(audioString):
    try:
        gTTS(text=audioString, lang='en').save("speech.mp3")
        AudioSegment.from_mp3('speech.mp3').export('speech.wav', format="wav")
        if audioString == "Hello! I am Ayola, a virtual assistant.":
            print("Hello! I am Aola, a virtual assistant")
        elif audioString == "Yo! Im Ayola, the coolest virtual assistant there is!":
            print("Yo! Im Aola, the coolest virtual assistant there is!")
        else:
            print(audioString)
        playsound("speech.wav")
        os.remove("speech.mp3")
        os.remove("speech.wav")
    except:
        print('No internet connection! Please try again later.')
        playsound('aolanointernet.wav')
    

def digital_assistant(data):
    if "hello" in data or "hi" in data or "yo" in data or 'high' in data:
        listening = True
        choice = random.randint(0, 2)
        if choice == 0:
            respond("Hello! I am Ayola, a virtual assistant.")
        if choice == 1:
            respond("Hello user!")
        if choice == 2:
            respond("Yo! Im Ayola, the coolest virtual assistant there is!")

    elif "how" in data and "are" in data and "you" in data or "how" in data and "are" in data and "you?" in data:
        listening = True
        respond("I am good")

    elif "what" in data and "time" in data and "is" in data and "it" in data:
        listening = True
        respond(f"It is {datetime.now().strftime('%I:%M %p')}")

    elif "what" in data and "day" in data and "is" in data and "it" in data or "what" in data and "day" in data and "is" in data and "it?" in data:
        listening = True
        respond(f"It is {datetime.now().strftime('%A')}")

    elif "what" in data and "year" in data and "is" in data and "it" in data or "what" in data and "year" in data and "is" in data and "it?" in data:
        listening = True
        respond(f"The year is {datetime.now().strftime('%Y')}")

    elif "repeat" in data or "say" in data:
        listening = True
        count = 0
        wordstring = ''
        for word in data:
            if count != 0:
                wordstring = f'{wordstring} {word}'
            count = count + 1
        respond(wordstring)

    #elif "login" in data or "log" in data and "in" in data:


    else:
        listening = True
        print("I didn't quite catch that.")
        playsound('aolaerror.wav')
    return listening


time.sleep(2)
print('Hello!')
playsound('aolahello.wav')
listening = True
wakeword = 'paola'
timer = 4
while listening == True:
	data = input().lower().split(' ')
	#data = listen().lower().split(' ')
	listening = digital_assistant(data)
	#if wakeword in listen().lower().split():
		#data = listen().lower().split(' ')
		#listening = digital_assistant(data)
