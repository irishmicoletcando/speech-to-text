# importing needed packages
import speech_recognition as speech_recog


def main():
    # initialize the recognizer
    recognizer = speech_recog.Recognizer()
    # source of audio - microphone
    with speech_recog.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Say something...")

        # listening to the source
        audio = recognizer.listen(source)
        print("Recognizing the speech now...")

        # converting the audio to text file using Google
        try:
            print("You said: \n " + recognizer.recognize_google(audio))
            print("Audio recorded successfully!")
        except Exception as error:
            print("Error.")


if __name__ == '__main__':
    main()