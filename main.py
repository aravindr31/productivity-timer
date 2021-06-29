from datetime import datetime
import time
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 160)


def speak_time():
    now = datetime.today().strftime("%I %M %p")s
    engine.say("time is " + now)
    engine.runAndWait()
    engine.stop()
    return


def time_calibrator():
    second = datetime.now().strftime("%S")
    if second != "00":
        print("Calibrating...")
        time.sleep(1)
        time_calibrator()
    else:
        print("Calibrated !!")
        time_loop()


def time_loop():
    time_min = datetime.now().strftime("%M")
    if time_min == "00" or time_min == "30":
        speak_time()
        time.sleep(60)
        time_calibrator()
    elif time_min == "15" or time_min == "45":
        speak_time()
        time.sleep(60)
        time_loop()
    else:
        time.sleep(60)
        time_loop()


time_calibrator()
