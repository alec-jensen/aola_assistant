import speech_recognition as sr
from datetime import datetime
import time 
import os
from gtts import gTTS
import requests, json
import random 
from playsound import playsound

def listen():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("I am listening...")
		audio = r.listen(source)
	data = ""
	try:
		data = r.recognize_google(audio)
		print("You said: " + data)
	except sr.UnknownValueError:
		print("Google Speech Recognition did not understand audio")
	except sr.RequestError as e:
		print("Request Failed; {0}".format(e))
	return data

def respond(audioString):
	if audioString == "Hello! I am Ayola, a virtual assistant.":
		print("Hello! I am Aola, a virtual assistant")
	elif audioString == "Yo! Im Ayola, the coolest virtual assistant there is!":
		print("Yo! Im Aola, the coolest virtual assistant there is!")
	else:
		print(audioString)
	tts = gTTS(text=audioString, lang='en')
	tts.save("speech.mp3")
	playsound("speech.mp3")
	os.remove("speech.mp3")

def digital_assistant(data):
	if "hello" in data or "hi" in data or "yo" in data:
		listening = True
		choice = random.randint(0, 2)
		if choice == 0:
			respond("Hello! I am Ayola, a virtual assistant.")
		if choice == 1:
			respond("Hello user!")
		if choice == 2:
			respond("Yo! Im Ayola, the coolest virtual assistant there is!")

	elif "how" in data and "are"in data and "you" in data or "how" in data and "are"in data and "you?" in data:
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

	elif "login" in data or "log" in data and "in" in data:
		

	else:
		listening = True
		respond("I didn't quite catch that")
	return listening

time.sleep(2)
respond('Hello!')
listening = True
while listening == True:
	#data = listen().lower().split(' ')
	data = input().lower().split(' ')
	listening = digital_assistant(data)
