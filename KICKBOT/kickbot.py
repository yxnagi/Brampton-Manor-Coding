import pyautogui as pag
import time
import sys
import random
import win32api, win32con

def staggered_speak(string):
    for character_index in string:
        sys.stdout.write(character_index)
        sys.stdout.flush()
        time.sleep(0.05)

def kick(name):
    while True:
        confidence_variable = 0.6
        if name == "RIDWAN":
            confidence_variable = 0.67
        if (pag.locateOnScreen(f"{name}.png") is not None):
            find = pag.locateCenterOnScreen(f"{name}.png", confidence = confidence_variable)
            pag.moveTo(find)
            time.sleep(0.05)
            pag.click(button='right')
            find = pag.locateCenterOnScreen("DISCONNECT.png", confidence = confidence_variable)
            pag.moveTo(find)
            pag.click()
        elif (pag.locateOnScreen(f"{name}2.png") is not None):
            find = pag.locateCenterOnScreen(f"{name}2.png", confidence = confidence_variable)
            pag.moveTo(find)
            time.sleep(0.05)
            pag.click(button='right')
            find = pag.locateCenterOnScreen("DISCONNECT.png", confidence = confidence_variable)
            pag.moveTo(find)
            pag.click()

name = input(f"INPUT VICTIM (RAYAN SOLEBUM OR RIDWAN ) ")
string = f"initiating program, kicking user {name}"
if name == "SOLEBUM":
    staggered_speak(string)
    kick(name)
elif name == "RIDWAN":
    staggered_speak(string)
    kick(name)
elif name == "RAYAN":
    staggered_speak(string)
    kick(name)

