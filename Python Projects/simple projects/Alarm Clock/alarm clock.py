import datetime
import time
import pygame

def set_alarm(alarm_time):
    is_alarm = True
    audio_path = 'one-piece-ost-overtaken.mp3'

    while is_alarm:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("Wake Up!")

            pygame.mixer.init()
            pygame.mixer.music.load(audio_path)
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                time.sleep(1)

            is_alarm = False
        time.sleep(1)

if __name__ == '__main__':
    alarm_time = input("Set the alarm time (HH:MM:SS) : ")
    set_alarm(alarm_time)
