import tkinter as tk


import adp
import AdaptiveLogic
from main import open_youtube_learning, open_canvas_learning


def create_main_window():
    root = tk.Tk()
    root.title("Learning Platform")
    root.geometry("600x400")

    tk.Label(root, text="Choose Learning Option", font=("Arial", 24, "bold")).pack(pady=20)

    tk.Button(root, text="YouTube Learning", command=open_youtube_learning, width=20).pack(pady=10)
    tk.Button(root, text="Canvas Learning", command=open_canvas_learning, width=20).pack(pady=10)

    root.mainloop()