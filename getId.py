from pynput.mouse import Button
import pynput.mouse
from pynput.keyboard import Key
import pynput.keyboard
import pyperclip
import time

# variables
search = '/userinfo.php?Id='
clipboard = ''
employer_id = ''

# open inspect
mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

# Read pointer position
print('The current pointer position is {0}', format(mouse.position))

def mouse_left(x, y):
    mouse.position = (x, y)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(1)

def mouse_right(x, y):
    mouse.position = (x, y)
    mouse.press(Button.right)
    mouse.release(Button.right)
    time.sleep(1)

def keyboard_enter():
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(1)

def keyboard_ctrl_f():
    keyboard.press(Key.ctrl)
    keyboard.press('f')
    keyboard.release(Key.ctrl)
    keyboard.release('f')
    time.sleep(1)

def save_clipboard(string):
    pyperclip.copy(string)
    time.sleep(1)

def keyboard_ctrl_c():
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    keyboard.release('c')
    time.sleep(1)

def keyboard_ctrl_v():
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release(Key.ctrl)
    keyboard.release('v')
    time.sleep(1)

def update_clipboard():
    global clipboard
    clipboard = pyperclip.paste()
    print('This is clipboard', clipboard)
    time.sleep(1)

def get_employer_id():
    lst = clipboard.split('_')
    lst = lst[1].split('<')
    id = lst[0]
    print(type(id))
    global employer_id
    employer_id = 'Member_' +  str(id)
    print(employer_id)
    time.sleep(1)
