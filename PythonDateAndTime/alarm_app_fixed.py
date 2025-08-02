import threading
import time
import datetime
import pygame

# Utility functions

def play_music(file_path: str):
    """Play *and keep looping* the given music file until stop() is called."""
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(loops=-1)


def wait_for_stop():
    """Block until the user presses "s", then stop the music."""
    while True:
        user_inp = input("Enter 's' to stop the alarm: ").strip().lower()
        if user_inp == "s":
            pygame.mixer.music.stop()
            break


# Core alarm logic

def set_alarm(alarm_time: str, alarm_sound: str = "clockAlarm.mp3"):
    """Continuously check the time and trigger the alarm when it matches."""
    print(f"Alarm set for: {alarm_time}")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        if current_time == alarm_time:
            print("WAKE UPPP 😫")
            # Spawn two threads: one to play music in a loop, one to wait for user input
            threading.Thread(target=play_music, args=(alarm_sound,), daemon=True).start()
            wait_for_stop()  # runs on main thread; returns after user stops music
            break  # exit the alarm loop once music is stopped


# Helper to compute future times cleanly using timedelta


def time_after(seconds: int = 0, minutes: int = 0, hours: int = 0) -> str:
    target = datetime.datetime.now() + datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return target.strftime("%H:%M:%S")


# Main menu


def main():
    menu = (
        "\nWelcome to the Alarm app:\n"
        "1. One hour from now.\n"
        "2. 30 minutes from now.\n"
        "3. 5 minutes from now.\n"
        "4. 10 seconds from now.\n"
        "5. Enter time manually (HH:MM:SS).\n"
    )
    print(menu)
    choice = input("Choose an option: ").strip()

    if choice == "1":
        set_alarm(time_after(hours=1))
    elif choice == "2":
        set_alarm(time_after(minutes=30))
    elif choice == "3":
        set_alarm(time_after(minutes=5))
    elif choice == "4":
        set_alarm(time_after(seconds=10))
    elif choice == "5":
        target = input("Enter alarm time (HH:MM:SS): ").strip()
        set_alarm(target)
    else:
        print("Invalid choice. Exiting…")


if __name__ == "__main__":
    main()
