# Creating a program that converts text to speech

# FOR WINDOWS USERS

# This module provides a simple interface for text-to-speech (TTS) conversion in Python on Windows
import pyttsx3

# Initializing text-to-speech engine
engine = pyttsx3.init()

print()
print("\t\t\t\t\t\t*** WELCOME TO THE VOICE CONVERTER PROGRAM ***")
print()

while True:
    
    # Taking input from user 
    text = input("Enter what you want to say (or 'qn' to quit): ")

    if text.lower() == 'qn':
        engine.say("See ya' around mate")
        engine.runAndWait()
        print()
        break

    # Using the engine to speak the text entered by user
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()


# # FOR MAC USERS
# import os
# text = input("Enter what you want to say: ")
# voice = f"say {text}"
# os.system(voice)