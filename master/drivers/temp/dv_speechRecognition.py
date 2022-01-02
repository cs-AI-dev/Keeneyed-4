import os
os.system("py -m pip install SpeechRecognition -q")
os.system("py -m pip install pocketsphinx -q")
import speech_recognition as recog

class SpeechRecognitionModule:
    def __init__(srm):
        srm.masterRecognizer = recog.Recognizer()

    def getMicrophoneRecognition(srm):
        audio = None

        with srm.masterRecognizer.Microphone() as audioSource:
            print("[ke4_speech_recognition_module] taking input ...", end="")
            audio = srm.masterRecognizer.listen(audioSource)

        try:
            recognizedSpeech = str(srm.masterRecognizer.recognize_sphinx(audio))
            print("complete, returned value: " + recognizedSpeech)
        except recog.UnknownValueError:
            print("no speech detected.")
            return None
        except recog.RequestError as e:
            print("error: could not request results: " + str(e))
            return e
