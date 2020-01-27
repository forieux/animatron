import importlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

import tkinter as tk

# from tkinter import Tk, RIGHT, BOTH, RAISED
import tkinter.ttk as ttk
from tkinter.ttk import Frame, Button, Style

demos = ["demosin"]


class DemoLister:
    def __init__(self, master, path="."):
        self.master = master
        self.listbox = tk.Listbox(master)
        self.demo_list = []
        for idx, demo in enumerate(demos):
            demo_modules.append(importlib.import_module(demo))
            demo_list.insert(idx + 1, demo_modules[idx].name)

        demo_list.pack(side=tk.LEFT, fill=tk.BOTH)

class TeachDemo:
    def __init__(self, master):
        super().__init__()

        self.master = master
        self.initUI()

    def update(self, val):
        self.demo.interact(float(val))
        self.fig.canvas.draw_idle()

    def initUI(self):
        self.master.title("Illustrations")
        self.style = Style()
        self.style.theme_use("clam")

        demo_list = tk.Listbox(self.master)
        demo_modules = []
        for idx, demo in enumerate(demos):
            demo_modules.append(importlib.import_module(demo))
            demo_list.insert(idx + 1, demo_modules[idx].name)

        demo_list.pack(side=tk.LEFT, fill=tk.BOTH)

        # frame = Frame(self, relief=RAISED, borderwidth=1)
        # frame.pack(fill=BOTH, expand=True)

        # self.pack(fill=BOTH, expand=True)

        # fig = Figure(figsize=(5, 4), dpi=100)
        self.fig = plt.figure()
        self.demo = demo_modules[0].Demo(self.fig)

        frame = ttk.Frame(self.master)
        frame.pack(side=tk.TOP, fill=tk.BOTH)
        w = ttk.Scale(
            frame,
            from_=1,
            to=10,
            orient=tk.HORIZONTAL,
            command=self.update,
        )
        w.pack(side=tk.LEFT, padx=5, pady=5)

        canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        closeButton = Button(self.master, text="Close", command=self.master.quit)
        closeButton.pack(side=tk.RIGHT, padx=5, pady=5)
        # okButton = Button(self.master, text="OK")
        # okButton.pack(side=tk.RIGHT)


def main():
    root = tk.Tk()
    app = TeachDemo(master=root)
    root.mainloop()


if __name__ == "__main__":
    main()
