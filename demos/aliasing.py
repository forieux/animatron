import numpy as np

title = "Repliement d'un sinus"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.axes = fig.subplots(2, 1)
        length = 20
        self.time = np.linspace(0.0, 0.1, length)
        self.time2 = np.linspace(0.0, 0.1, 10000)
        Te = self.time[2] - self.time[1]
        self.Fe = 1 / Te  # (self.time2[2] - self.time2[1])
        self.freq = np.arange(length) / (length * Te)

        sig = np.sin(2 * np.pi * self.time)
        sig2 = np.sin(2 * np.pi * self.time2)
        sig3 = np.sin(2 * np.pi * self.time2)

        (self.line3,) = self.axes[0].plot(
            self.time2, sig3, alpha=0.4, color="C0", label=r"Vrai $s(t)$"
        )
        (self.line,) = self.axes[0].plot(
            self.time2, sig2, alpha=1, color="C1", label="Apparent"
        )
        (self.linem,) = self.axes[0].plot(
            self.time, sig, "o", color="C0", label=r"Echant. $s_e(t)$"
        )
        self.axes[0].legend(loc="upper center", ncol=3)
        # self.axes[0].set_xlim([0, 0.1])
        self.axes[0].set_ylim([-1.3, 1.3])
        self.axes[0].set_xlabel(r"$t$ [s]")
        self.axes[0].set_title(r"$s(t)$")

        (self.linef,) = self.axes[1].plot(
            self.freq, np.abs(np.fft.fft(sig, norm="ortho"))
        )
        self.axes[1].set_xlabel(r"$\nu$ [Hz]")
        self.axes[1].set_title(r"$\left|S_e(\nu)\right| = \left|TF[s_e(t)]\right|$")

    def interact(self, freq: (1, 150, 100) = 1):
        if freq < 81:
            sig2 = np.sin(2 * freq * np.pi * self.time2)
        else:
            sig2 = np.sin(2 * (self.Fe - freq) * np.pi * self.time2)

        sig = np.sin(2 * freq * np.pi * self.time)
        sigf = np.abs(np.fft.fft(sig))
        self.line.set_ydata(sig2)
        self.line3.set_ydata(np.sin(2 * freq * np.pi * self.time2))
        self.linem.set_ydata(sig)
        self.linef.set_ydata(sigf)
        self.axes[1].relim()
        self.axes[1].autoscale_view()  # enable=True, axis="Y")


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plt.ion()
    d = Demo(plt.figure())
    d.interact(3)
    plt.show()
