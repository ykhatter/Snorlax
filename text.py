import subprocess
from gtts import gTTS 

mytext = "Welcome to Thapar"

language = 'en'

myobj = gTTS(text = mytext, lang = language)

myobj.save("welcome.mp3")

subprocess.call(['mpg321','welcome.mp3','--play-and-exit'])
