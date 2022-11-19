# importing needed packages
import speech_recognition as speech_recog

def main():
    # initialize the recognizer
    recognizer = speech_recog.Recognizer()
    # source of audio - microphone
    with speech_recog.Microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something...")