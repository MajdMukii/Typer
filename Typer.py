import tkinter as tk
from tkinter import *
# from tkinter import messagebox
import pyautogui as pag

root = tk.Tk()
root.title("Typer")
root.resizable(True,True)
root.geometry("200x200")
Entry1 = tk.Entry(root)
Entry1.pack(expand=1,)

def start():
    write = Entry1.get()
    x, y = pag.position()
    pag.PAUSE = 2
    pag.moveTo(x, y)
    pag.write(str(write))


button = tk.Button(root, text="Start Writing", command=start)

button.pack(fill="x")
root.mainloop()
