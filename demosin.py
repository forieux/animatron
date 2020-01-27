import numpy as np

name = "Sinus"


class Demo:
    def __init__(self, fig):
        self.axe = fig.add_subplot(111)
        self.time = np.arange(0.0, 3.0, 0.01)
        (self.line,) = self.axe.plot(self.time, np.sin(2 * np.pi * self.time))

    def interact(self, freq: float):
        self.line.set_ydata(np.sin(2 * freq * np.pi * self.time))
