import numpy as np
from mpl_toolkits.mplot3d import Axes3D

title = "SSL E3A: ex. 7"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


def expnumc(n, m=0.9, φ=0.1):
    z = m * np.exp(1j * φ)
    return z ** n


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.axes = fig.subplots(1, 1)

        ω = 10
        Te = 0.1

        self.rez = np.linspace(-2, 2, 100)
        self.imz = np.linspace(-2, 2, 100)

        X, Y = np.meshgrid(self.rez, self.imz)
        Z = X + 1j * Y
        radius = np.sqrt(X ** 2 + Y ** 2)

        tz = Z * np.sin(ω * Te) / (Z ** 2 - 2 * Z * np.cos(ω * Te) + 1)
        # tz = np.abs(Z * np.sin(ω * Te) / (Z**2 - 2 * Z * np.cos(ω * Te) + 1))

        # self.im = self.axes.plot_surface(X, Y, np.abs(1 / (1 - a * (X + Y)**-1)))
        self.im = self.axes.imshow(np.abs(tz), extent=(-2, 2, -2, 2))
        self.axes.add_artist(
            plt.Circle((0, 0), radius=1, fill=False, color="white", alpha=0.5)
        )

        # self.im = self.axes[1].imshow(np.angle(tz), extent=(-2, 2, -2, 2))

        # self.axes.set_title(
        #     r"L'exponentielle complexe $e^{pt} = e^{rt}e^{iωt} = e^{rt} (cos(ωt) + sin(ω t))$, $p = r + i ω$",
        # )

    def interact(
        self,
        m: (-1.1, 1.1, 10) = 0.9,
        φ: (-0.1, 0.1, 10) = 0.01,
        pr: "Im." = None,
        pi: "Re." = None,
        pt: "Proj. t" = None,
    ):
        res = expnumc(self.n, m=m, φ=φ)
        self.line.set_data_3d(self.n, np.real(res), np.imag(res))

        if pr:
            self.axes.view_init(elev=0, azim=-90)

        if pi:
            self.axes.view_init(elev=90, azim=-90)

        if pt:
            self.axes.view_init(elev=0, azim=0)


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plt.ion()
    fig = plt.figure(1)
    plt.clf()
    d = Demo(fig)
    plt.show()
