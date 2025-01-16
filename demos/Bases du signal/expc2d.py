import matplotlib.pyplot as plt
import numpy as np

title = "Exponentielle complexe 2D"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


def expc(t, σ=0.2, ω=5):
    p = σ + 1j * ω
    return np.exp(2 * np.pi * p * t)


class Demo:
    def __init__(self, fig):
        fig.clf()
        axes = fig.subplots(2, 3)
        axes[1, 0].set_visible(False)

        self.t = np.linspace(-1, 1, 1000)
        res = expc(self.t)

        (self.pt,) = axes[0, 0].plot(0.2, 5, "o")
        (self.rayon,) = axes[0, 0].plot([0, 0.2], [0, 5], alpha=0.5)
        axes[0, 0].grid("on")
        axes[0, 0].set_xlim(-0.35, 0.35)
        axes[0, 0].set_ylim(-11, 11)
        axes[0, 0].set_title("p = σ + ιω")
        axes[0, 0].set_xlabel("σ = Re[p]")
        axes[0, 0].set_ylabel("ω = Im[p]")

        (self.lr,) = axes[0, 1].plot(self.t, np.real(res))
        axes[0, 1].set_xlabel("t")
        axes[0, 1].set_title("$Re[e^{pt}]$")
        axes[0, 1].set_ylim([-3.5, 3.5])
        axes[0, 1].grid("on")

        (self.li,) = axes[0, 2].plot(self.t, np.imag(res))
        axes[0, 2].set_xlabel("t")
        axes[0, 2].set_title("$Im[e^{pt}]$")
        axes[0, 2].set_ylim([-3.5, 3.5])
        axes[0, 2].grid("on")

        (self.la,) = axes[1, 1].plot(self.t, np.abs(res))
        axes[1, 1].set_xlabel("t")
        axes[1, 1].set_title("$|e^{pt}| = e^{σt}$")
        axes[1, 1].set_ylim([-3.5, 3.5])
        axes[1, 1].grid("on")

        (self.lp,) = axes[1, 2].plot(self.t, np.angle(res))
        axes[1, 2].set_xlabel("t")
        axes[1, 2].set_title(r"$\phi [e^{pt}] = ω t$")
        axes[1, 2].set_ylim([-3.5, 3.5])
        axes[1, 2].grid("on")

        plt.suptitle(
            r"L'exponentielle complexe $e^{pt} = e^{σt} \times e^{ιωt} = e^{σt} \times [cos(ωt) + ι sin(ω t)]$, avec $p = σ + ι ω$",
        )
        plt.tight_layout()

    def interact(self, σ: (-0.3, 0.3, 10) = 0.2, ω: (-10.0, 10.0, 10) = 5):
        res = expc(self.t, σ=σ, ω=ω)

        self.pt.set_xdata([σ])
        self.pt.set_ydata([ω])
        self.rayon.set_xdata([0, σ])
        self.rayon.set_ydata([0, ω])
        self.lr.set_ydata(np.real(res))
        self.li.set_ydata(np.imag(res))
        self.la.set_ydata(np.abs(res))
        self.lp.set_ydata(np.angle(res))
