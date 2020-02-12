import numpy as np
import matplotlib.pyplot as plt

title = "Système non Linéaire"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.axes = fig.subplots(2, 1)

        self.t = np.linspace(0, 10, 1000)
        self.sig = np.zeros_like(self.t)
        self.sig[0] = 1
        self.sig[400] = 1
        self.sig[800] = 0.5
        a = np.fmax(0, self.t.reshape((-1, 1)) - self.t.reshape((1, -1)))
        self.H = np.exp(-np.ones((1, len(self.t))) * a)
        self.H[a == 0] = 0
        out = np.dot(self.H, self.sig)

        (self.le,) = self.axes[0].plot(self.t, self.sig, label="e(t)")
        (self.ls,) = self.axes[1].plot(self.t, np.fmin(1.5, out), label="s(t)")
        self.axes[0].legend()
        self.axes[1].legend()
        self.axes[1].set_xlabel(r"$t$")
        # self.axes[0].set_title("Système linéaire invariant")
        # self.axes[0].grid('on')
        # self.axes[1].grid('on')

    def interact(self, A: (0.0, 2, 100) = 1):
        self.sig[400] = A
        out = np.dot(self.H, self.sig)

        self.le.set_ydata(self.sig)
        self.ls.set_ydata(np.fmin(1.5, out))
        self.axes[0].set_ylim([-0.1, 2.2])
        # self.axes[0].set_ylim([self.axes[1].get_ylim()[0], 1.1 * self.sig.max()])
        self.axes[1].set_ylim([-0.1, 2.2])
        # self.axes[1].set_ylim([self.axes[1].get_ylim()[0], 1.1 * out.max()]) #


if __name__ == "__main__":
    plt.ion()
    d = Demo(plt.figure())
    d.interact(10)
    plt.show()
