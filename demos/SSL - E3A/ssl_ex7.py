import matplotlib.pyplot as plt
import numpy as np

title = "SSL E3A: ex. 7"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


def expnumc(n, m=0.9, φ=0.1):
    z = m * np.exp(1j * φ)
    return z ** n


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.axes = fig.subplots(1, 2)

        ω = 1
        Te = 0.1

        #%% TZ
        X, Y = np.meshgrid(np.linspace(-2, 2, 100), np.linspace(-2, 2, 100))
        self.Z = X + 1j * Y
        tz = self.Z * np.sin(ω * Te) / (self.Z ** 2 - 2 * self.Z * np.cos(ω * Te) + 1)

        # tz = np.abs(Z * np.sin(ω * Te) / (Z**2 - 2 * Z * np.cos(ω * Te) + 1))
        # self.im = self.axes.plot_surface(X, Y, np.abs(1 / (1 - a * (X + Y)**-1)))

        self.im = self.axes[0].imshow(np.abs(tz), extent=(-2, 2, -2, 2))
        self.axes[0].add_artist(
            plt.Circle((0, 0), radius=1, fill=False, color="white", alpha=0.5)
        )

        # self.im = self.axes[1].imshow(np.angle(tz), extent=(-2, 2, -2, 2))

        self.axes[0].set_title(r"TZ d'un sinus causal $\sin(ω t) u(t)$")
        self.axes[0].set_xlabel(r"$\Re[z]$")
        self.axes[0].set_ylabel(r"$\Im[z]$")

        #%% Time
        t = np.arange(0, 500) * Te
        sig = np.sin(ω * t)
        (self.l,) = self.axes[1].plot(t, sig, ".-")
        self.axes[1].set_xlabel(r"$t$")
        self.axes[1].set_xlim([0, t[200]])

    def interact(
        self, ω: (1, 20, 19) = 1, Te: (0.05, 0.15, 20) = 0.1,
    ):
        tz = self.Z * np.sin(ω * Te) / (self.Z ** 2 - 2 * self.Z * np.cos(ω * Te) + 1)
        self.im.set_data(np.abs(tz))

        t = np.arange(0, 500) * Te
        self.l.set_xdata(t)
        self.l.set_ydata(np.sin(ω * t))


if __name__ == "__main__":
    plt.ion()
    fig = plt.figure(1)
    plt.clf()
    d = Demo(fig)
    plt.show()
