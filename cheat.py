from time import sleep
import time
import pyautogui
import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("auto walk sim")

textlabel = tk.Label(root, text="auto walk sim v1", font=('Arial', 40))
textlabel.pack()

root.mainloop()

time.sleep(10)

while True:
    pyautogui.keyDown('w')

root.mainloop()
input()
