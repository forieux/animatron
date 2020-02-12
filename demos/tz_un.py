import numpy as np
from mpl_toolkits.mplot3d import Axes3D

title = "TZ échelon"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


class Demo:
    def __init__(self, fig):
        fig.clf()
        # self.axe = fig.add_subplot(111, projection="3d")
        self.axe = fig.add_subplot(111)

        self.rez = np.linspace(-2, 2, 100)
        self.imz = np.linspace(-2, 2, 100)

        a = -1.5
        X, Y = np.meshgrid(self.rez, self.imz)
        radius = np.sqrt(X ** 2 + Y ** 2)

        tz = np.abs(1 / (1 - a * (X + Y) ** -1))
        tz[np.abs(radius) <= 1] = 0

        # self.im = self.axe.plot_surface(X, Y, np.abs(1 / (1 - a * (X + Y)**-1)))
        self.im = self.axe.imshow(tz, extent=(-2, 2, -2, 2))
        self.axe.add_artist(plt.Circle((0, 0), radius=1, fill=False))

    def interact(self, freq: (1, 5)):
        self.line.set_ydata(np.sin(2 * freq * np.pi * self.time))


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plt.ion()
    fig = plt.figure(1)
    plt.clf()
    d = Demo(fig)
    # d.interact(3)
    plt.show()
