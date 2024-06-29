from gtts import gTTS
import os
import time
from pygame import mixer

tts = gTTS('ya',lang='id')
tts.save('testing_tts_mark.mp3')

mixer.init()
mixer.music.load("testing_tts_mark.mp3")
mixer.music.play()
while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)