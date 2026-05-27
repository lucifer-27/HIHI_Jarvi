#This Code is for SpeechRecognition

# for speech_recognition we have to use pip install SpeechRecognition
import speech_recognition as sr        
import os
import threading

# for translate we have to use pip install mtranslate
from mtranslate import translate 

#pip install colorma
from colorama import Fore,Style,init

init(autoreset=True)

def print_loop():
    while True:
        print(Fore.CYAN + "I am Listening Master ",end="",flush=True)
        print(Style.RESET_ALL,end="",flush=True)

def Translate_hindi_to_english(text):
    english_text = translate(text,"en-us")

def Speech_to_text():
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = False