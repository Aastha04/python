
import gtts
from gtts import gTTS
import os
text= "hello,everyone.My name is Aastha Sharma and I am 19 years old"
myText=gTTS(text,lang='en',slow=True)
myText.save("myText.mp3")
os.system("myText.mp3")