import matplotlib.pyplot as plt
import numpy as np

title = "Système Linéaire Non Invariant"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.axes = fig.subplots(2, 1)

        self.t = np.linspace(0, 10, 1000)
        self.sig = np.zeros_like(self.t)
        self.sig[0] = 1
        self.sig[500] = 1
        a = np.fmax(0, self.t.reshape((-1, 1)) - self.t.reshape((1, -1)))
        self.H = np.exp(-np.linspace(1, 8, len(self.t)) * a)
        self.H[a == 0] = 0
        out = np.dot(self.H, self.sig)

        (self.le,) = self.axes[0].plot(self.t, self.sig, label="e(t)")
        (self.ls,) = self.axes[1].plot(self.t, out, label="s(t)")
        self.axes[0].legend()
        self.axes[1].legend()
        self.axes[1].set_xlabel(r"$t$")

    def interact(self, τ: (0.1, 9.0, 100) = 5):
        self.sig.fill(0)
        self.sig[0] = 1
        self.sig[np.where(self.t <= τ)[0][-1]] = 1
        out = np.dot(self.H, self.sig)

        self.le.set_ydata(self.sig)
        self.ls.set_ydata(out)
        self.axes[1].set_ylim([self.axes[1].get_ylim()[0], 1.1 * out.max()])


if __name__ == "__main__":
    plt.ion()
    d = Demo(plt.figure())
    d.interact(10)
    plt.show()
