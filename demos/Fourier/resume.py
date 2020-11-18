import numpy as np
from matplotlib.ticker import MaxNLocator

title = "Résumé"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"
dontload = True


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.axe = fig.add_subplot(111)

        self.t = np.linspace(0, 1, 1001)

        self.sig = sum(c * np.sin(2 * np.pi * f * self.t) for f, c in enumerate(coeffs))

        self.sige = np.zeros_like(self.sig)
        self.sige[::50] = self.sig[::50]

        self.sigq = (self.sig // 0.3) * 0.3

        self.axe.plot(self.t, self.sig, label=r"$s_a(t)$")
        self.xlim = self.axe.get_xlim()
        self.ylim = [1.1 * lim for lim in self.axe.get_ylim()]

        self.interact(slide=0)

    def interact(self, slide: range(6) = 0):
        self.axe.cla()
        if slide == 0:
            self.axe.plot(self.t, self.sig, label=r"$s_a(t)$")
            self.axe.set_xlabel("t [s]")
            self.axe.set_xlim(self.xlim)
            self.axe.set_title("Signal analogique continue")

        elif slide == 1:
            self.axe.plot(self.t, self.sig, label=r"$s_a(t)$")
            self.axe.plot(self.t, self.sige, alpha=0.4, label=r"$s_e(t)$")
            self.axe.set_xlabel("t [s]")
            self.axe.set_xlim(self.xlim)
            self.axe.set_title("Version échantillonée")

        elif slide == 2:
            self.axe.plot(self.t, self.sig, label=r"$s_a(t)$")
            self.axe.plot(self.t, self.sigq, label=r"$s_q(t)$")
            self.axe.set_title("Version quantifiée")
            self.axe.set_xlim(self.xlim)
            self.axe.set_xlabel("t [s]")

        elif slide == 3:
            self.axe.plot(self.t, self.sig, label=r"$s_a(t)$")
            self.axe.plot(self.t, self.sige, alpha=0.4, label=r"$s_e(t)$")
            self.axe.step(
                self.t[::50],
                (self.sig[::50] // 0.3) * 0.3,
                where="post",
                label=r"$s_q(t)$",
            )  # ds="steps-post")
            self.axe.set_xlabel("t [s]")
            self.axe.set_xlim(self.xlim)
            self.axe.set_title("Version quantifiée régulièrement")

        elif slide == 4:
            self.axe.plot(self.t, self.sig, label=r"$s_a(t)$")
            stem = self.axe.stem(
                self.t[::50], (self.sig[::50] // 0.3) * 0.3, use_line_collection=True
            )
            stem[2].set_color(stem[0].get_color())
            self.axe.set_xlabel("t [s]")
            self.axe.set_xlim(self.xlim)
            self.axe.set_title("Version numérisée")

        elif slide == 5:
            stem = self.axe.stem(
                (self.sig[::50] // 0.3) * 0.3, use_line_collection=True, label=r"$s_n$"
            )
            stem[2].set_alpha(0)
            self.axe.xaxis.set_major_locator(MaxNLocator(integer=True))
            self.axe.set_xlabel(r"Indice $n$")
            self.axe.set_title("Signal numérique (pas = {:.2f} [s])".format(self.t[50]))

        self.axe.legend(loc="upper right")
        self.axe.set_ylim(self.ylim)
