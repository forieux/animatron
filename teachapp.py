import sys
import inspect
from inspect import signature
import importlib
import numbers
from pathlib import Path

import tkinter as tk
import tkinter.ttk as ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

from logzero import logger

sys.path.append('./demos')


class TeachApp:
    def __init__(self, master):
        self.master = master
        self.demo = None

        self.master.title("Illustrations")
        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.dtree = DemosTree(self)

        self.control_frame = ttk.Frame(self.master, relief="raised")
        self.control_frame.pack(side=tk.TOP, fill=tk.BOTH)

        self.fig = plt.figure()
        canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        closeButton = ttk.Button(self.master, text="Close", command=self.master.quit)
        closeButton.pack(side=tk.RIGHT, padx=5, pady=5)

        self.master.bind("<Configure>", self.resize)

    @property
    def demo(self):
        return self._demo

    @demo.setter
    def demo(self, demo):
        if demo is not None:
            self._demo = demo
            for child in self.control_frame.winfo_children():
                child.destroy()
            self._demo.add_control(self)
            self.demo_obj = self._demo.code.Demo(self.fig)
            self.update()
            self.fig.canvas.draw_idle()
            self.fig.tight_layout(rect=[0, 0.03, 1, 0.95])
        else:
            self._demo = None

    def update(self):
        args = [control.val for control in self._demo.controls]
        self.demo_obj.interact(*args)
        self.fig.canvas.draw_idle()

    def resize(self, event):
        self.fig.tight_layout(rect=[0, 0.03, 1, 0.95])


class DemoWrap:
    def __init__(self, name, app: TeachApp):
        self.app = app
        self.name = name
        self.code = importlib.import_module(name)
        self.title = self.code.title
        self.nparam = len(signature(self.code.Demo.interact).parameters) - 1

    def add_control(self, app: TeachApp):
        self.param_names = []
        self.controls = []
        # self.par_annots = []
        parameters = signature(self.code.Demo.interact).parameters
        for key in filter(lambda p: p != "self", parameters):
            annot = parameters[key].annotation
            name = parameters[key].name
            if parameters[key].default is inspect._empty:
                default = None
            else:
                default = parameters[key].default

            if isinstance(annot, tuple):
                if len(annot) == 1 and isinstance(annot[0], int):
                    control = None
                elif len(annot) == 1 and isinstance(annot[0], float):
                    control = None
                elif len(annot) == 2:
                    if all(isinstance(a, int) for a in annot):
                        logger.info("2 IntSlider")
                        control = IntSlider(
                            app,
                            start=annot[0],
                            stop=annot[1],
                            name=name,
                            default=default,
                        )
                    elif all(isinstance(a, numbers.Real) for a in annot):
                        logger.info("2 FloatSlider")
                        control = FloatSlider(
                            app,
                            start=annot[0],
                            stop=annot[1],
                            name=name,
                            default=default,
                        )
                    else:
                        logger.warning(f"{annot} annotations control type unsuported")
                        control = None
                elif len(annot) == 3:
                    if all(isinstance(a, numbers.Real) for a in annot):
                        logger.info("3 FloatSlider")
                        control = FloatSlider(
                            app,
                            start=annot[0],
                            stop=annot[1],
                            num=annot[2],
                            name=name,
                            default=default,
                        )
            elif isinstance(annot, numbers.Real):
                control = None
            else:
                logger.warning(f"{annot} annotations control type unsuported")
                control = None

            if control is not None:
                self.controls.append(control)


class IntSlider:
    def __init__(
        self, app: TeachApp, start: int, stop: int, name: str = "", default: int = None,
    ) -> None:
        logger.info("Init IntSlider")
        self.app = app

        w = tk.Scale(
            app.control_frame,
            from_=start,
            to=stop,
            orient=tk.HORIZONTAL,
            command=self.update,
            label=name,
        )
        w.pack(side=tk.LEFT, padx=5, pady=5)
        if default is None:
            w.set(start - stop // 2)
        else:
            w.set(default)

        self.val = int(float(w.get()))

    def update(self, w_val):
        self.val = int(float(w_val))
        self.app.update()


class FloatSlider:
    def __init__(
        self,
        app: TeachApp,
        start: float,
        stop: float,
        num: int = 10,
        name: str = "",
        default: float = None,
    ) -> None:
        logger.info("Init FloatSlider")
        self.app = app

        w = tk.Scale(
            app.control_frame,
            from_=start,
            to=stop,
            resolution=(stop - start) / num,
            orient=tk.HORIZONTAL,
            command=self.update,
            label=name,
        )
        w.pack(side=tk.LEFT, padx=5, pady=5)
        if default is None:
            w.set(start - stop / 2)
        else:
            w.set(default)

        self.val = float(w.get())

    def update(self, w_val):
        self.val = float(w_val)
        self.app.update()


class Button:
    pass


class ReloadButton:
    pass


class CheckBox:
    pass


class Dropdown:
    pass


class Text:
    pass


class DemosTree:
    def __init__(self, app: TeachApp, path="."):
        self.app = app
        demo_names = (p.stem for p in Path('./demos').glob('*.py'))
        self.demos = [DemoWrap(name, app) for name in demo_names]

        tree = ttk.Treeview(app.master)
        tree.heading("#0", text="Demos", anchor=tk.W)
        tree.column("#0", width=250)
        for demo in self.demos:
            tree.insert("", tk.END, demo.name, text=demo.title)

        tree.pack(side=tk.LEFT, fill=tk.BOTH)

        tree.bind("<<TreeviewSelect>>", self.on_select)

    def on_select(self, event):
        selected = event.widget.selection()[0]
        for demo in self.demos:
            if demo.name == selected:
                break
        else:
            demo = None
        self.app.demo = demo


def main():
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW", lambda: root.quit())
    TeachApp(master=root)
    root.mainloop()


if __name__ == "__main__":
    main()
