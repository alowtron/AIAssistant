import speech_recognition as sr


def record_mic():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        # Using PocketSphinx for offline recognition
        text = recognizer.recognize_sphinx(audio)
        return("You said: " + text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError:
        print("Sphinx Error")