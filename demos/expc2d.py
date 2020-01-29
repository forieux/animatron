import numpy as np
import matplotlib.pyplot as plt

title = "Exponentielle complexe"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


def expc(t, r=0.2, ω=5):
    p = r + 1j * ω
    return np.exp(2 * np.pi * p * t)


class Demo:
    def __init__(self, fig):
        fig.clf()

        self.t = np.linspace(-1, 1, 1000)
        res = expc(self.t)

        plt.subplot(2, 3, 1)
        (self.pt,) = plt.plot(0.2, 5, "o")
        (self.rayon,) = plt.plot([0, 0.2], [0, 5], alpha=0.5)
        plt.grid()
        plt.xlim(-0.35, 0.35)
        plt.ylim(-11, 11)
        plt.title("p")
        plt.xlabel("Re[p]")
        plt.ylabel("Im[p]")

        plt.subplot(2, 3, 2)
        (self.lr,) = plt.plot(self.t, np.real(res))
        plt.xlabel("t")
        plt.title("$Re[e^{pt}]$")
        plt.ylim([-3.5, 3.5])
        plt.grid()

        plt.subplot(2, 3, 3)
        (self.li,) = plt.plot(self.t, np.imag(res))
        plt.xlabel("t")
        plt.title("$Im[e^{pt}]$")
        plt.ylim([-3.5, 3.5])
        plt.grid()

        plt.subplot(2, 3, 5)
        (self.la,) = plt.plot(self.t, np.abs(res))
        plt.xlabel("t")
        plt.title("$|e^{pt}| = e^{rt}$")
        plt.ylim([-3.5, 3.5])
        plt.grid()

        plt.subplot(2, 3, 6)
        (self.lp,) = plt.plot(self.t, np.angle(res))
        plt.xlabel("t")
        plt.title(r"$\phi [e^{pt}] = i ω t$")
        plt.ylim([-3.5, 3.5])
        plt.grid()

        plt.suptitle(
            r"L'exponentielle complexe $e^{pt} = e^{rt}e^{iωt} = e^{rt} (cos(ωt) + sin(ω t))$, $p = r + i ω$",
        )

    def interact(self, r: (-0.3, 0.3, 10) = 0.2, ω: (-10.0, 10.0, 10) = 5):
        res = expc(self.t, r=r, ω=ω)

        self.pt.set_xdata(r)
        self.pt.set_ydata(ω)
        self.rayon.set_xdata([0, r])
        self.rayon.set_ydata([0, ω])
        self.lr.set_ydata(np.real(res))
        self.li.set_ydata(np.imag(res))
        self.la.set_ydata(np.abs(res))
        self.lp.set_ydata(np.angle(res))
