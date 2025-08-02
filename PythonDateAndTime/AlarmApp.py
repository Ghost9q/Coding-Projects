import threading
# to update the time every second we
import time
# to use string specifier for date and time we
import datetime
# the easiest way to use sound effects is to use pygame
import pygame
# Alarm App
# the program has some bugs like if you enter option 4 (setting the timer to 10 secs) it will actually count 11 seconds
# or if the alarm music was over which is 30 seconds the program won't stop, you still have to enter 's' to close it.
# couldn't find a solution for these bugs but you can always upload the file to Chat GPT :)
def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
def con():
    con = input('Enter s to stop the alarm: ').lower()
    if con == 's':
        pygame.mixer.music.stop()
def set_alarm(alarm_time):
    print(f'Alarm set for: {alarm_time}')
    alarm_sound = 'clockAlarm.mp3'
    running = True
    while running:
        current_time = datetime.datetime.now().strftime('%H:%M:%S')
        print(current_time)
        time.sleep(1)
        if alarm_time == current_time:
            print('WAKE UPPP 😫')
            running = False
            process1 = threading.Thread(target=play_music, args=(alarm_sound,))
            process2 = threading.Thread(target=con)
            process1.start()
            process2.start()
def main():
    print('''
Welcome to the Alarm app:
1. one hour from now.
2. 30 minutes from now.
3. 5 minutes from now.
4. 10 seconds from now.
5. enter 5 to enter the time manually.
''')
    chosen = input('Enter on of the numbers above: ')
    if chosen == '4':
        c_sec = datetime.datetime.now().strftime('%S')
        c_min = datetime.datetime.now().strftime('%M')
        c_hou = datetime.datetime.now().strftime('%H')
        if int(c_sec) not in [i for i in range(0, 60)]:
            time.sleep(1)
        target_time = datetime.time(int(c_hou),int(c_min),int(c_sec) + 10)
        set_alarm(str(target_time))
    elif chosen == '5':
        target_time = input('enter a time for the alarm to trigger (HH:MM:SS): ')
        set_alarm(str(target_time))
    elif chosen == '1':
        c_sec = datetime.datetime.now().strftime('%S')
        c_min = datetime.datetime.now().strftime('%M')
        c_hou = datetime.datetime.now().strftime('%H')
        if int(c_sec) not in [i for i in range(1, 59)]:
            time.sleep(1)
        target_time = datetime.time(int(c_hou) + 1,int(c_min),int(c_sec))
        set_alarm(str(target_time))
    elif chosen == '2':
        c_sec = datetime.datetime.now().strftime('%S')
        c_min = datetime.datetime.now().strftime('%M')
        c_hou = datetime.datetime.now().strftime('%H')
        if int(c_sec) not in [i for i in range(1, 59)]:
            time.sleep(1)
        target_time = datetime.time(int(c_hou),int(c_min) + 30,int(c_sec))
        set_alarm(str(target_time))
    elif chosen == '3':
        c_sec = datetime.datetime.now().strftime('%S')
        c_min = datetime.datetime.now().strftime('%M')
        c_hou = datetime.datetime.now().strftime('%H')
        if int(c_sec) not in [i for i in range(1, 59)]:
            time.sleep(1)
        target_time = datetime.time(int(c_hou),int(c_min) + 5,int(c_sec))
        set_alarm(str(target_time))

if __name__ == '__main__':
    main()