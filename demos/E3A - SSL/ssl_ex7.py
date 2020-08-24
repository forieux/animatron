import matplotlib.pyplot as plt
import numpy as np

title = "Ex. 07"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


def expnumc(n, m=0.9, φ=0.1):
    z = m * np.exp(1j * φ)
    return z ** n


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.axes = fig.subplots(2, 2)
        self.axes[1, 0].set_visible(False)

        ω0 = 1
        Te = 0.1

        #%% Sig
        self.n = np.arange(500)

        t, sig = self.sig(ω0, Te)
        (self.ll,) = self.axes[0][0].plot(t, sig, color="C0", alpha=0.5)
        (self.lm,) = self.axes[0][0].plot(t, sig, ".", color="C0")
        self.axes[0][0].set_title(r"Sinus causal $\sin(ω0 nT_e) u(nTe)$")
        self.axes[0][0].set_xlabel(r"$t$")
        self.axes[0][0].set_xlim([0, t[200]])

        #%% TZ
        X, Y = np.meshgrid(np.linspace(-2, 2, 100), np.linspace(-2, 2, 100))
        self.Z = X + 1j * Y

        # tz = np.abs(Z * np.sin(ω0 * Te) / (Z**2 - 2 * Z * np.cos(ω0 * Te) + 1))
        # self.im = self.axes.plot_surface(X, Y, np.abs(1 / (1 - a * (X + Y)**-1)))

        self.im = self.axes[0][1].imshow(
            np.log(np.abs(self.tz(ω0, Te))), extent=(-2, 2, -2, 2)
        )
        self.axes[0][1].add_artist(
            plt.Circle((0, 0), radius=1, fill=False, color="white", alpha=0.5)
        )

        # self.im = self.axes[1].imshow(np.angle(tz), extent=(-2, 2, -2, 2))

        self.axes[0][1].set_title(r"TZ $|X(z)|$")
        self.axes[0][1].set_xlabel(r"$\Re[z]$")
        self.axes[0][1].set_ylabel(r"$\Im[z]$")

        #%% TF
        ω, tf = self.tf(ω0, Te)
        (self.ltf,) = self.axes[1][1].plot(ω, np.abs(tf), "-")
        self.axes[1][1].set_xlabel(r"$ω$")
        self.axes[1][1].set_title(r"TFD $|X(ω)|$")

    def sig(self, ω0, Te):
        t = self.n * Te
        return t, np.sin(ω0 * t)

    def tz(self, ω0, Te):
        return (
            self.Z * np.sin(ω0 * Te) / (self.Z ** 2 - 2 * self.Z * np.cos(ω0 * Te) + 1)
        )

    def tf(self, ω0, Te):
        ω = self.n / (500 * Te)
        z = np.exp(1j * ω)
        return ω, z * np.sin(ω0 * Te) / (z ** 2 - 2 * z * np.cos(ω0 * Te) + 1)

    def interact(
        self, ω0: (1, 20, 19) = 1, Te: (0.05, 0.15, 20) = 0.1,
    ):
        self.im.set_data(np.log(np.abs(self.tz(ω0, Te))))

        self.ll.set_xdata(self.sig(ω0, Te)[0])
        self.ll.set_ydata(self.sig(ω0, Te)[1])
        self.lm.set_xdata(self.sig(ω0, Te)[0])
        self.lm.set_ydata(self.sig(ω0, Te)[1])

        self.ltf.set_xdata(self.tf(ω0, Te)[0])
        self.ltf.set_ydata(np.abs(self.tf(ω0, Te)[1]))


if __name__ == "__main__":
    plt.ion()
    fig = plt.figure(1)
    plt.clf()
    d = Demo(fig)
    plt.show()
