import importlib
import inspect
import numbers
import sys
import tkinter as tk
import tkinter.ttk as ttk
from inspect import signature
from pathlib import Path

import matplotlib.pyplot as plt
from logzero import logger
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

sys.path.append("./demos")


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

        reloadButton = ttk.Button(self.master, text="Reload", command=self.reload)
        reloadButton.pack(side=tk.LEFT, padx=5, pady=5)

        self.labelAuthor = ttk.Label(self.master, text="")
        self.labelAuthor.pack(side=tk.LEFT, padx=5, pady=5)

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
            self.labelAuthor["text"] = demo.comment
        else:
            self._demo = None

    def update(self):
        args = [control.val for control in self._demo.controls]
        self.demo_obj.interact(*args)
        self.fig.canvas.draw_idle()

    def reload(self):
        self.dtree.reload()

    def resize(self, event):
        self.fig.tight_layout(rect=[0, 0.03, 1, 0.95])
        self.fig.canvas.draw_idle()


class DemoWrap:
    def __init__(self, name, app: TeachApp) -> None:
        self.app = app
        self.name = name
        self.runable = False
        self.load()

    def load(self):
        try:
            self.code = importlib.import_module(self.name)
            importlib.reload(self.code)
        except Exception as e:
            logger.error(f"Error while trying to import {self.name}.py")
            logger.error(e)
            self.title = f"{self.name} (ERROR)"
            self.runable = False
            self.comment = ""
        else:
            self.title = self.code.title
            self.nparam = len(signature(self.code.Demo.interact).parameters) - 1
            if hasattr(self.code, "authors"):
                if hasattr(self.code, "email"):
                    self.comment = f"{self.code.authors} - {self.code.email}"
                else:
                    self.comment = f"{self.code.authors}"
            elif hasattr(self.code, "email"):
                self.comment = f"{self.code.email}"
            else:
                self.comment = ""

            if hasattr(self.code, "dontload") and self.code.dontload:
                self.runable = False
            else:
                self.runable = True

    def add_control(self, app: TeachApp):
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

            if isinstance(annot, tuple) and len(annot) == 2:
                if all(isinstance(a, int) for a in annot):
                    control = IntScale(
                        app, start=annot[0], stop=annot[1], name=name, default=default,
                    )
                elif all(isinstance(a, numbers.Real) for a in annot):
                    control = FloatScale(
                        app, start=annot[0], stop=annot[1], name=name, default=default,
                    )
                else:
                    logger.warning(f"{annot} annotations control type unsuported")
                    control = None
            elif isinstance(annot, tuple) and len(annot) == 3:
                if all(isinstance(a, numbers.Real) for a in annot):
                    control = FloatScale(
                        app,
                        start=annot[0],
                        stop=annot[1],
                        num=annot[2],
                        name=name,
                        default=default,
                    )
            elif isinstance(annot, tuple):
                control = Dropdown(app, values=annot)
            elif isinstance(annot, str):
                control = Button(app, annot)
            elif isinstance(annot, bool):
                control = CheckBox(app, name, annot)
            elif isinstance(annot, range):
                control = Slider(app, len(annot))
            else:
                logger.warning(
                    f"{annot} annotations control type unsuported and will be given as fixed default value"
                )
                control = Fixed(annot)

            if control is not None:
                self.controls.append(control)


class IntScale:
    def __init__(
        self, app: TeachApp, start: int, stop: int, name: str = "", default: int = None,
    ) -> None:
        self.app = app

        w = tk.Scale(
            app.control_frame,
            from_=start,
            to=stop,
            orient=tk.HORIZONTAL,
            command=self.update,
            label=name,
            length=150,
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


class FloatScale:
    def __init__(
        self,
        app: TeachApp,
        start: float,
        stop: float,
        num: int = 10,
        name: str = "",
        default: float = None,
    ) -> None:
        self.app = app

        w = tk.Scale(
            app.control_frame,
            from_=start,
            to=stop,
            resolution=(stop - start) / num,
            orient=tk.HORIZONTAL,
            command=self.update,
            label=name,
            length=150,
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
    def __init__(self, app: TeachApp, text: str,) -> None:
        self.app = app
        self.val = None

        w = ttk.Button(app.control_frame, text=text, command=self.update,)
        w.pack(side=tk.LEFT, padx=5, pady=5)

    def update(self):
        self.val = True
        self.app.update()
        self.val = None


class Slider:
    def __init__(self, app: TeachApp, num: int,) -> None:
        self.app = app
        self.num = num
        self.val = 0

        self.label = ttk.Label(app.control_frame, text=f"0 / {num-1}")
        self.label.pack(side=tk.LEFT, padx=5, pady=5)
        w = ttk.Button(app.control_frame, text="←", command=self.previous,)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w = ttk.Button(app.control_frame, text="→", command=self.next,)
        w.pack(side=tk.LEFT, padx=5, pady=5)

    def previous(self):
        self.val = max(self.val - 1, 0)
        self.label["text"] = f"{self.val} / {self.num-1}"
        self.app.update()

    def next(self):
        self.val = min(self.val + 1, self.num - 1)
        self.label["text"] = f"{self.val} / {self.num-1}"
        self.app.update()


class CheckBox:
    def __init__(self, app, text, value):
        self.app = app
        self.val = value
        self.text = text
        self.val = value
        self.var = tk.IntVar()

        if self.val:
            self.var.set(1)
        else:
            self.var.set(0)

        w = ttk.Checkbutton(
            app.control_frame, text=text, command=self.update, variable=self.var,
        )
        w.pack(side=tk.LEFT, padx=5, pady=5)

    def update(self):
        if self.var.get():
            self.val = True
        else:
            self.val = False
        self.app.update()


class Dropdown:
    def __init__(self, app, values):
        self.app = app
        self.values = values
        self._idx = 0
        self.val = values[self._idx]

        w = ttk.Combobox(app, values=[str(item) for item in values])
        w.current(self._idx + 1)
        w.pack(side=tk.LEFT, padx=5, pady=5)
        w.bind("<<ComboboxSelected>>", self.update)

    def update(self, event):
        pass


class Fixed:
    def __init__(self, val):
        self.val = val


class DemosTree:
    def __init__(self, app: TeachApp, path=".") -> None:
        self.app = app
        demo_names = (p.stem for p in Path("./demos").rglob("*.py"))
        self.demos = []
        for name in sorted(demo_names):
            self.demos.append(DemoWrap(name, app))

        self.tree = ttk.Treeview(app.master)
        self.tree.heading("#0", text="Demos", anchor=tk.W)
        self.tree.column("#0", width=250)
        for demo in self.demos:
            self.tree.insert("", tk.END, demo.name, text=demo.title)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH)

        self.tree.bind("<<TreeviewSelect>>", self.on_select)

    def on_select(self, event):
        self.selected = event.widget.selection()[0]
        for demo in self.demos:
            if demo.name == self.selected and demo.runable:
                break
        else:
            demo = None
        self.app.demo = demo

    def reload(self):
        for demo in self.demos:
            if demo.name == self.selected:
                demo.load()
                if demo.runable:
                    self.tree.item(demo.name, text=demo.title)
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
