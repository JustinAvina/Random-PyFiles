import pyautogui as spam
import time
import requests as req

class Spammer:

limit = input("Enter number of messages >")
msg = input("Message you want to send >")

i = 0

time.sleep(10)

while i<int(limit):

    spam.typewrite(msg)
    spam.press('Enter')

    i += 1
