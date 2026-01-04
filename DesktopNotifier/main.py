import csv
import time
import datetime
from plyer import notification
import simpleaudio as sa
import numpy as np
import pygame
import schedule


filename="file.csv" 
columns=[]
rows=[]
soundtrack="scream.mp3"

pygame.mixer.init()
pygame.mixer.music.load(soundtrack)
pygame.mixer.music.set_volume(1.0)

while pygame.mixer.music.get_busy() == True:
	pass

def playfilesound():
    waveobj=sa.WaveObject.from_wave_file(soundtrack)
    playobj=waveobj.play()
    playobj.wait_done()

def beep_simpleaudio():
    frequency = 440  # Hz (A4 note)
    duration = 0.4  # seconds
    
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    audio = np.sin(frequency * t * 2 * np.pi)
    
    
    audio *= 32767 / np.max(np.abs(audio))
    audio = audio.astype(np.int16)
    
    for i in range(10):
        play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
        play_obj.wait_done()
        if i < 9:
            time.sleep(0.3)

def triggerNotif(message):
    if __name__ == __name__:
        notification.notify(
            title="ALERT",
            message=message,
            app_icon="/home/unred/codin/projects/python-bot-path/DesktopNotifier/timer_hourglass.ico",
            timeout=5,
        )
        #beep_simpleaudio()
        pygame.mixer.music.play()
   
        time.sleep(7) 
        
def  setalarm():
   name="sssss"
   
#schedule.every().day.at("09:20").do(triggerNotif,"hello every very")

with open(filename,'r') as csvfile:
    reader=csv.reader(csvfile)
    print("headers",next(reader))
    for line in reader:
        #print((line[1])[11:19]);
        schedule.every().day.at((line[1])[11:19]).do(triggerNotif,line[2])


#playfilesound()
#beep_simpleaudio()
pro_time=datetime.datetime.now()
print("time clock is about:",pro_time)
#triggerNotif("صبح شده پا شو بلامیسر")
setalarm()

while True:
    schedule.run_pending()
    time.sleep(1)