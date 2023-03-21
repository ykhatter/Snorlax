import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Speak Anything : ")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        
        print("You Said : {}".format(text))
    except:
        print("Sorry could not recognize your voice")