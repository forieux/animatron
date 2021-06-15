import numpy as np

title = "Repliement d'un sinus"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


class Demo:
    def __init__(self, fig):
        fig.clf()
        axes = fig.subplots(2, 1)
        Te = 0.005
        n_point = 20
        extra = 100
        self.discret_time = np.arange(0.0, extra * n_point * Te, Te)
        self.continous_time = np.arange(0.0, extra * n_point * Te, Te / 100)
        self.Fe = 1 / Te

        sig, siga, sige, sigf = self.get_sig(1)

        (self.line_sig,) = axes[0].plot(
            self.continous_time,
            sig,
            alpha=0.3,
            color="C0",
            label=r"Vrai $s(t) = sin(2 π f t)$",
        )
        (self.line_siga,) = axes[0].plot(
            self.continous_time, siga, alpha=1, color="C1", label="Apparent"
        )
        (self.line_sige,) = axes[0].plot(
            self.discret_time,
            sige,
            "o",
            color="C0",
            label=rf"Echant. $s_e(t)$  avec  $Fe = {int(1 / Te)}$ Hz",
        )
        axes[0].legend(bbox_to_anchor=(0.5, 1.3), loc="upper center", ncol=3)

        axes[0].set_xlim([0, n_point * Te])
        axes[0].set_ylim([-1.3, 1.3])
        axes[0].set_xlabel(r"$t$ [s]")

        (self.line_f,) = axes[1].plot(
            np.arange(extra * n_point) / (extra * n_point * Te), sigf
        )
        axes[1].set_xlabel(r"$\nu$ [Hz]")
        axes[1].set_title(r"$\left|S_e(\nu)\right| = \left|TF[s_e(t)]\right|$")

    def get_sig(self, freq):
        sig = np.sin(2 * freq * np.pi * self.continous_time)
        if freq < 100:
            siga = np.sin(2 * freq * np.pi * self.continous_time)
        else:
            siga = np.sin(-2 * (self.Fe - freq) * np.pi * self.continous_time)

        sige = np.sin(2 * freq * np.pi * self.discret_time)
        sigf = np.abs(np.fft.fft(sige, norm="ortho"))

        return sig, siga, sige, sigf

    def interact(self, f: (1, 150, 149) = 1):
        sig, siga, sige, sigf = self.get_sig(f)

        self.line_sig.set_ydata(sig)
        self.line_siga.set_ydata(siga)
        self.line_sige.set_ydata(sige)
        self.line_f.set_ydata(sigf)


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plt.ion()
    d = Demo(plt.figure())
    d.interact(3)
    plt.show()
