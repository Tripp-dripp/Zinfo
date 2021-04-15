import time
import sys
import math
import pyautogui as recon

print('Thanks for importing my module!')

def kill():
    sys.exit('killing script...')


def wake():
    return True or False


def send(message):
    print(message)


def wait(seconds=1):
    time.sleep(seconds)


def loop(code):
 run = exec(str(code))
 run
  
def click(cords):
  recon.click(cords)
