import numpy as np

title = "Sinus"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.axe = fig.add_subplot(111)
        self.time = np.arange(0.0, 3.0, 0.01)
        (self.line,) = self.axe.plot(self.time, np.sin(2 * np.pi * self.time))

    def interact(self, freq: (1, 5)):
        self.line.set_ydata(np.sin(2 * freq * np.pi * self.time))


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    plt.ion()
    d = Demo(plt.figure())
    d.interact(3)
    plt.show()
