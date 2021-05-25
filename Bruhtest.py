import webbrowser
import tkinter as tk
root = tk.Tk()
root.withdraw()
from tkinter import messagebox, simpledialog
open1 = simpledialog.askstring('open', '')
webbrowser.open(open1)
