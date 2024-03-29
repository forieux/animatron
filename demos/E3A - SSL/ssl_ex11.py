import matplotlib.pyplot as plt
import numpy as np

title = "Ex. 11"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.axes = fig.subplots(2, 2)
        self.axes[1, 0].set_visible(False)

        α = 0.5

        #%% Sig
        self.n = np.arange(-20, 20)
        (self.lm,) = self.axes[0][0].plot(self.n, self.sig(α), color="C0", alpha=0.5)
        (self.ll,) = self.axes[0][0].plot(self.n, self.sig(α), "o", color="C0")
        self.axes[0][0].set_xlabel(r"$n$")
        self.axes[0][0].set_title(r"$x[n] = α^{|n|}, α \in R$")

        #%% TF
        ω = np.linspace(-2 * np.pi, 6 * np.pi, 400)
        self.z = np.exp(1j * ω)
        (self.ltf,) = self.axes[1][1].plot(ω, np.abs(self.tf(α)), "-")
        self.axes[1][1].set_xlabel(r"$ω$")
        self.axes[1][1].set_title(r"TFD $|X(ω)|$")

        #%% TZ
        xmin, xmax, ymin, ymax = -2.5, 2.5, -2.5, 2.5
        X, Y = np.meshgrid(np.linspace(xmin, xmax, 200), np.linspace(ymin, ymax, 200))
        self.Z = X + 1j * Y
        self.rc = np.logical_and(abs(self.Z) < (1 / abs(α)), abs(α) < abs(self.Z))
        self.im = self.axes[0][1].imshow(
            np.abs(self.tz(α)), extent=(xmin, xmax, ymin, ymax)
        )
        self.axes[0][1].grid(False)

        self.axes[0][1].add_artist(
            plt.Circle((0, 0), radius=1, fill=False, lw=2, color="red", alpha=0.7)
        )

        self.axes[0][1].set_title(r"TZ $|X(z)|$")
        self.axes[0][1].set_xlabel(r"$\Re[z]$")
        self.axes[0][1].set_ylabel(r"$\Im[z]$")

    #%% Method
    def sig(self, α):
        return α ** np.abs(self.n)

    def tz(self, α):
        if α == 0:
            rc = np.full(self.Z.shape, True)
            tz = np.full(self.Z.shape, 1)
        else:
            rc = np.logical_not(
                np.logical_and(abs(self.Z) < (1 / abs(α)), abs(α) < abs(self.Z))
            )
            tz = (1 - α ** 2) / (1 - α * (self.Z + self.Z ** (-1)) + α ** 2)
            tz[rc] = np.nan
        return tz

    def tf(self, α):
        return (1 - α ** 2) / (1 - α * (self.z + self.z ** (-1)) + α ** 2)

    #%% TZ
    def interact(
        self,
        α: (-1.1, 1.1, 20) = 0.5,
    ):
        self.ll.set_ydata(self.sig(α))
        self.lm.set_ydata(self.sig(α))
        self.axes[0][0].relim()
        self.axes[0][0].autoscale_view()  # enable=True, axis="Y")

        if abs(α) < 1:
            self.im.set_data(np.log(np.abs(self.tz(α))))
            self.im.autoscale()
            self.ltf.set_ydata(np.abs(self.tf(α)))
            self.axes[1][1].relim()
            self.axes[1][1].autoscale_view()  # enable=True, axis="Y")
        else:
            self.im.set_data(np.full(self.Z.shape, np.nan))
            self.ltf.set_ydata(np.full(self.z.shape, np.nan))


if __name__ == "__main__":
    plt.ion()
    fig = plt.figure(1)
    plt.clf()
    d = Demo(fig)
    plt.show()
