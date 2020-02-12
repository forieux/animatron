import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

title = "Fonctions propres"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


class Demo:
    def __init__(self, fig):
        fig.clf()
        gs = GridSpec(3, 3)
        self.axe1 = fig.add_subplot(gs[0])
        self.axe2 = fig.add_subplot(gs[:, 1:])

        self.t = np.linspace(0, 4, 1000)
        self.h = np.exp(-20 * self.t[:40])
        self.h /= np.sum(self.h)

        self.axe1.plot(self.t[:40], self.h)
        self.axe1.set_title(r"RI $h(t)$")
        self.axe1.grid("on")
        self.axe1.set_xlabel(r"$t$")

        sig = np.sin(10 * self.t)
        out = np.convolve(sig, self.h, "full")

        (self.le,) = self.axe2.plot(self.t, sig, label="e(t)")
        (self.ls,) = self.axe2.plot(self.t, out[: len(sig)], label="s(t)")
        self.axe2.legend(loc="upper right")
        self.axe2.grid("on")
        self.axe2.set_xlabel(r"$t$")
        self.axe2.set_xlim([0.25, 3])
        self.axe2.set_title(
            r"$e(t) = sin(ω t)$    /    $s(t) = e * h = A(ω) sin(ω t + \phi(ω))$"
        )

    def interact(self, ω: (10, 40)):
        sig = np.sin(ω * self.t)
        self.le.set_ydata(sig)
        self.ls.set_ydata(np.convolve(sig, self.h, "full")[: len(sig)])


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plt.ion()
    d = Demo(plt.figure())
    d.interact(10)
    plt.show()
