import matplotlib.pyplot as plt
import numpy as np

title = "TL Exp."
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


limits = (-1.2, 1.2, -8, 8)


class Demo:
    def __init__(self, fig):
        fig.clf()

        self.t = np.linspace(-2, 5, 1000)
        self.σ = np.linspace(limits[0], limits[1], 200)
        self.ω = np.linspace(limits[2], limits[3], 200)
        self.Σ, self.Ω = np.meshgrid(
            self.σ,
            self.ω,
        )
        self.P = self.Σ + 1j * self.Ω
        self.u = np.where(self.t < 0, 0, 1)

        self.axes = fig.subplots(2, 3)
        self.axes[1, 0].set_visible(False)

        (self.ls,) = self.axes[0, 0].plot(self.t, self.sig(), label=r"$e^{\alpha t}$")
        (self.le,) = self.axes[0, 0].plot(
            self.t, np.real(self.exp()), alpha=0.7, label=r"$Re[e^{-pt}]$"
        )
        self.axes[0, 0].grid(True)
        # self.axes[0, 0].set_xlim(-0.35, 0.35)
        self.axes[0, 0].set_ylim([-3, 3])
        self.axes[0, 0].legend(loc="upper center", ncol=2)
        self.axes[0, 0].set_xlabel("t")
        # self.axes[0, 0].set_title("p = σ + iω")
        # self.axes[0, 0].set_xlabel("σ = Re[p]")
        # self.axes[0, 0].set_ylabel("ω = Im[p]")
        # self.axes[0, 0].set_xlim(limits[:2])
        # self.axes[0, 0].set_ylim(limits[2:])

        self.fr = self.axes[0, 1].fill_between(self.t, np.real(self.prod()), color="C0")
        self.axes[0, 1].set_xlabel("t")
        self.axes[0, 1].set_title(r"$Re[u(t)e^{αt}e^{-pt}]$")
        self.axes[0, 1].set_ylim([-3, 3])
        self.axes[0, 1].grid(True)

        self.fi = self.axes[0, 2].fill_between(self.t, np.imag(self.prod()), color="C0")
        self.axes[0, 2].set_xlabel("t")
        self.axes[0, 2].set_title(r"$Im\left[u(t)e^{αt}e^{-pt}\right]$")
        self.axes[0, 2].set_ylim([-3, 3])
        self.axes[0, 2].grid(True)

        self.ima = self.axes[1, 1].imshow(
            np.log(np.abs(self.tl())), cmap="gray", extent=limits, aspect="auto"
        )
        (self.red1,) = self.axes[1, 1].plot(0.2, 5, "o", color="red")
        self.axes[1, 1].set_title(r"$|X(p)| = \left|\frac{1}{p - \alpha}\right|$")
        self.axes[1, 1].grid(False)
        self.axes[1, 1].axvline(0, color="red", alpha=0.7)
        self.axes[1, 1].set_xlabel(r"$σ = Re[p]$")
        self.axes[1, 1].set_ylabel(r"$ω = Im[p]$")

        (self.lf,) = self.axes[1, 2].plot(self.ω, np.abs(self.tf()))
        self.axes[1, 2].set_title(r"|X(ω)|")
        self.axes[1, 2].set_xlabel(r"$ω$")
        (self.red2,) = self.axes[1, 2].plot(5, 0, "o", color="red")

        # self.imf = self.axes[1, 2].imshow(
        #     np.angle(self.tl()), cmap="gray", extent=limits, aspect="auto"
        # )
        # (self.red2,) = self.axes[1, 2].plot(0.2, 5, "o", color="red")
        # self.axes[1, 2].set_title(r"$arg(X(p))$")
        # self.axes[1, 2].grid(False)
        # self.axes[1, 2].axvline(0, color="red", alpha=0.7)

        plt.suptitle(r"Exponentielle causale $e^{αt}$")

    def sig(self, α=-0.1):
        return self.u * np.exp(α * self.t)

    def exp(self, σ=0.2, ω=4):
        p = σ + 1j * ω
        return np.exp(-p * self.t)

    def prod(self, α=-0.1, σ=0.2, ω=4):
        return self.sig(α) * self.exp(σ, ω)

    def tl(self, α=-0.1):
        out = 1 / (self.P - α)
        out[np.real(self.P) < α] = np.nan
        return out

    def tf(self, α=-0.1):
        if α < 0:
            return 1 / (1j * self.ω - α)
        else:
            return np.full_like(self.ω, np.nan)

    def interact(
        self,
        α: (-1, 1, 20) = -0.2,
        σ: (-1, 1, 20) = 0.2,
        ω: (-7, 7, 20) = 5,
    ):
        res = self.prod(α=α, σ=σ, ω=ω)

        self.ls.set_ydata(self.sig(α))
        self.le.set_ydata(np.real(self.exp(σ, ω)))

        self.fr.remove()
        self.fr = self.axes[0, 1].fill_between(self.t, np.real(res), color="C0")
        # self.axes[0, 1].set_xlabel("t")
        # self.axes[0, 1].set_title(r"$Re[u(t)e^{-pt}]$")
        self.axes[0, 1].set_ylim([-2, 2])

        self.fi.remove()
        self.fi = self.axes[0, 2].fill_between(self.t, np.imag(res), color="C0")
        # self.axes[0, 2].set_xlabel("t")
        # self.axes[0, 2].set_title(r"$Im[u() e^{-pt}]$")
        self.axes[0, 2].set_ylim([-2, 2])

        self.ima.set_data(np.log(np.abs(self.tl(α))))
        # self.ima.relim()
        # self.ima.autoscale_view()  # enable=True, axis="Y")

        # self.imf.set_data(np.angle(self.tl(α)))

        self.lf.set_ydata(np.abs(self.tf(α)))

        self.red1.set_xdata(σ)
        self.red1.set_ydata(ω)
        self.red2.set_xdata(ω)
        # self.red2.set_xdata(σ)
        # self.red2.set_ydata(ω)

        # self.lr.set_ydata(np.real(res))
        # self.li.set_ydata(np.imag(res))
        # self.la.set_ydata(np.abs(res))
        # self.lp.set_ydata(np.angle(res))
