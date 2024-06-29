from gtts import gTTS
import os
import time
from pygame import mixer
import pygame._sdl2.audio as sdl2_audio

def get_devices(capture_devices: bool = False) -> tuple[str, ...]:
    init_by_me = not mixer.get_init()
    if init_by_me:
        mixer.init()
    devices = tuple(sdl2_audio.get_audio_device_names(capture_devices))
    if init_by_me:
        mixer.quit()
    return devices

print(get_devices())

# set output to 'CABLE Input (VB-Audio Virtual Cable)'
mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')

kalimat_tersimpan = []

while True:
  kalimat_baru = input("Masukkan kalimat: ")
  kalimat_tersimpan.append(kalimat_baru)
  if kalimat_baru == "":
    break
  # kalimat masukan ke dalam variabel

  # sekarang masukan kalimat kedalam mp3
  tts = gTTS(kalimat_baru,lang='id')
  tts.save('testing_tts_mark.mp3')
  time.sleep(1)
  mixer.init()
  mixer.music.load("testing_tts_mark.mp3")
  mixer.music.play()
  while mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(0.1)
  mixer.music.unload()
  mixer.stop()
  
