import matplotlib.pyplot as plt
import numpy as np

title = "TL Heaviside"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


limits = (-0.33, 1, -8, 8)


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.axes = fig.subplots(2, 2)
        # self.axes[1, 0].set_visible(False)

        self.t = np.linspace(-0.3, 1, 1000)

        # Σ, Ω = np.meshgrid(np.linspace(-0.3, 0.3, 200), np.linspace(-10, 10, 200))
        self.ω = np.linspace(limits[2], limits[3], 200)
        self.Σ, self.Ω = np.meshgrid(np.linspace(limits[0], limits[1], 200), self.ω)
        self.P = self.Σ + 1j * self.Ω

        self.u = np.where(self.t < 0, 0, 1)
        res = self.prod()

        # (self.point,) = self.axes[0, 0].plot(0.2, 5, "o")
        # (self.rayon,) = self.axes[0, 0].plot([0, 0.2], [0, 5], alpha=0.5)

        # self.axes[0, 0].grid("on")
        # self.axes[0, 0].set_xlim(-0.35, 0.35)
        # self.axes[0, 0].set_ylim(-11, 11)
        # self.axes[0, 0].set_title("p = σ + iω")
        # self.axes[0, 0].set_xlabel("σ = Re[p]")
        # self.axes[0, 0].set_ylabel("ω = Im[p]")
        # self.axes[0, 0].set_xlim(limits[:2])
        # self.axes[0, 0].set_ylim(limits[2:])

        self.axes[0, 0].fill_between(self.t, np.real(res))
        self.axes[0, 0].set_xlabel("t")
        self.axes[0, 0].set_title(r"$Re[u(t)e^{-pt}]$")
        self.axes[0, 0].set_ylim([-3.5, 3.5])
        self.axes[0, 0].grid(True)

        self.axes[0, 1].fill_between(self.t, np.imag(res))
        self.axes[0, 1].set_xlabel("t")
        self.axes[0, 1].set_title(r"$Im[u() e^{-pt}]$")
        self.axes[0, 1].set_ylim([-3.5, 3.5])
        self.axes[0, 1].grid(True)

        self.axes[1, 0].imshow(
            np.log(np.abs(self.tl())), "gray", extent=limits, aspect="auto"
        )
        (self.red1,) = self.axes[1, 0].plot(0.2, 5, "o", color="red")
        self.axes[1, 0].axvline(0, color="red", alpha=0.7)
        self.axes[1, 0].set_title(r"$|U(p)| = \left|\frac{1}{p}\right|$")
        self.axes[1, 0].grid(False)
        self.axes[1, 0].set_xlabel(r"$σ = Re[p]$")
        self.axes[1, 0].set_ylabel(r"$ω = Im[p]$")

        # self.axes[1, 1].imshow(
        #     np.angle(self.tl()), "gray", extent=limits, aspect="auto"
        # )
        # (self.red2,) = self.axes[1, 1].plot(0.2, 5, "o", color="red")
        # self.axes[1, 1].set_title(r"$|\phi(p)|$")
        # self.axes[1, 1].grid(False)
        # self.axes[1, 1].set_xlabel(r"$σ = Re[p]$")
        # self.axes[1, 1].set_ylabel(r"$ω = Im[p]$")

        (self.lf,) = self.axes[1, 1].plot(self.ω, np.abs(self.tf()))
        self.axes[1, 1].set_title(r"|U(ω)|")
        self.axes[1, 1].set_xlabel(r"$ω$")
        (self.red2,) = self.axes[1, 1].plot(5, 0, "o", color="red")

        plt.suptitle(r"L'échelon $u(t)$")

    def sig(self):
        return self.u

    def prod(self, σ=0.2, ω=5):
        p = σ + 1j * ω
        return self.sig() * np.exp(-2 * np.pi * p * self.t)

    def tl(self):
        out = 1 / self.P
        out[np.real(self.P) <= 0] = np.nan
        return out

    def tf(self):
        return 1 / (1j * self.ω)

    def interact(
        self, σ: (limits[0], limits[1], 10) = 0.2, ω: (limits[2], limits[3], 10) = 2
    ):
        res = self.prod(σ=σ, ω=ω)

        # self.point.set_xdata(σ)
        # self.point.set_ydata(ω)
        # self.rayon.set_xdata([0, σ])
        # self.rayon.set_ydata([0, ω])

        self.axes[0, 0].clear()
        self.axes[0, 0].fill_between(self.t, np.real(res))
        self.axes[0, 0].set_xlabel("t")
        self.axes[0, 0].set_title(r"$Re[u(t)e^{-pt}]$")

        self.axes[0, 1].clear()
        self.axes[0, 1].fill_between(self.t, np.imag(res))
        self.axes[0, 1].set_xlabel("t")
        self.axes[0, 1].set_title(r"$Im[u() e^{-pt}]$")

        self.red1.set_xdata(σ)
        self.red1.set_ydata(ω)
        self.red2.set_xdata(ω)
        # self.red2.set_ydata(ω)

        # self.lr.set_ydata(np.real(res))
        # self.li.set_ydata(np.imag(res))
        # self.la.set_ydata(np.abs(res))
        # self.lp.set_ydata(np.angle(res))
