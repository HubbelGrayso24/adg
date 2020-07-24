import numpy as np
from grabscreen import grab_screen
import cv2
import time
import os
import pyautogui as kp
import random as r

starting_value = 1
typekey = "i"
x = 1

while True:
    file_name = 'training_data-{}.npy'.format(starting_value)

    if os.path.isfile(file_name):
        print('File exists, moving along',starting_value)
        starting_value += 1
    else:
        print('File does not exist, starting fresh!',starting_value)

        break

def key(typekey):
    kp.press(typekey)
    time.sleep(1)

def gnkey():
    kp.keyDown("num9")
    time.sleep(1)
    kp.keyUp("num9")

def activate():
    key('i')
    key('num9')
    time.sleep(5)
    key('num5')
    key('num2')
    key('num2')
    key('num5')
    key('num2')
    key('num5')
    key('num0')
    for i in range(3):
        key('num2')
    key('num5')
    key('num8')
    key('num5')
    for i in range(4):
        key('num2')
    time.sleep(1)
    key('num9')

def texit():
    for i in range(3):
        key('num0')

def treturn():
    key('num9')
    time.sleep(1)
    for i in range(2):
        key('num5')

def teleport():
    key('num5')
    for i in range(r.randint(1, 25)):
        key('num2')
    key('num5')

def main(file_name, starting_value):
    file_name = file_name
    starting_value = starting_value
    training_data = []
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)
    activate()
    last_time = time.time()
    paused = False
    print('STARTING')
    while(True):

        for i in range(100):
            teleport()
            texit()
            screen = grab_screen(region=(0,40,1280,747))
            last_time = time.time()
            #screen = cv2.resize(screen, (480,270))
            #screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB)

            training_data.append([screen])
            time.sleep(1)
            treturn()
            last_time = time.time()

            if len(training_data) % 5 == 0:
                print(len(training_data))

                if len(training_data) == 25:
                    np.save(file_name,training_data)
                    print('SAVED')
                    training_data = []
                    starting_value += 1
                    file_name = 'C:/Users/hubbe/Documents/GitHub/adg/ADG Files/training_data-{}.jpg'.format(starting_value)

main(file_name, starting_value)
