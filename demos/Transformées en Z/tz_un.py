import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

title = "TZ échelon"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"
dontload = True

limits = (-2, 2, -2, 2)


class Demo:
    def __init__(self, fig):
        fig.clf()
        # self.axe = fig.add_subplot(111, projection="3d")
        self.axes = fig.subplots(2, 2)

        self.n = np.arange(-5, 20)

        self.rez = np.linspace(limits[0], limits[1], 100)
        self.imz = np.linspace(limits[2], limits[3], 100)

        X, Y = np.meshgrid(self.rez, self.imz)
        self.Z = X + 1j * Y

        # self.im = self.axe.plot_surface(X, Y, np.abs(1 / (1 - a * (X + Y)**-1)))
        self.im = self.axes[1, 0].imshow(np.abs(self.tz()), extent=limits)
        self.axes[1, 0].grid(False)
        self.axes[1, 0].add_artist(
            plt.Circle((0, 0), radius=1, color="red", lw=2, fill=False)
        )
        self.axes[1, 0].set_title(r"$|U(z)| = |\frac{1}{1 - z^{-1}}|$")
        self.axes[1, 0].set_xlabel(r"$Re[z]$")
        self.axes[1, 0].set_ylabel(r"$Im[z]$")

    def sig(self):
        return np.where(self.n < 0, 0, 1)

    def tz(self):
        out = 1 / (1 - self.Z ** -1)
        out[np.abs(self.Z) <= 1] = np.nan
        return out

    def interact(self, freq: (1, 5)):
        self.line.set_ydata(np.sin(2 * freq * np.pi * self.time))


if __name__ == "__main__":
    plt.ion()
    fig = plt.figure(1)
    plt.clf()
    d = Demo(fig)
    lt.show()
