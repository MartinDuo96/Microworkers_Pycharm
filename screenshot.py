import pyautogui
import tkinter as tk
import getId

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()


def takeScreenshot():
    im = pyautogui.screenshot(region=(0, 110, 1900, 930))
    im.save(r'C:\Users\marti\OneDrive\Desktop\Microworker\screenshot.png')


getId.scroll_down()
takeScreenshot()
