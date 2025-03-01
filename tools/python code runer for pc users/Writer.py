import tkinter as tk
from tkinter import messagebox as msg
import os

# Выполняет код python конвертирует в exe и выполняет на другом компьютере

filename = "testWriter.py"
programName = "python code reading to for exe user pc"

def save():
    msg.showinfo("python code reading to for exe user pc", "Фаил успешно сахранен конвертирован в exe")

def runCode():
    msg.showinfo("python code reading to for exe user pc", f"Код успешно запушен и успешно сохранен в файле {filename}!")
    # os.system(f"python {filename}")
    
windows = tk.Tk()
windows.geometry("650x450")
windows.title("python code reading to for exe user pc")
windows.resizable(False, False)

txt = tk.Text(windows)
txt.place(x=0, y=30)

button_save = tk.Button(windows, text='Save file', font=('copper', 10), command=save)
button_start = tk.Button(windows, text="Run", font=('cooper', 10), command=runCode) 
filename = tk.Label(windows, text=f"{filename}", bg=None)

filename.place(x=0, y=8)
button_save.place(x=580, y=0)
button_start.place(x=540, y=0)
windows.mainloop()