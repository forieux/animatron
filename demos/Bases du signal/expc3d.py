import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

assert Axes3D

title = "Exponentielle complexe 3D"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


def expc(t, A=1, r=0.2, ω=5):
    p = r + 1j * ω
    return A * np.exp(2 * np.pi * p * t)


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.t = np.linspace(-1, 1, 1000)
        # self.axe = fig.add_subplot(111, projection="3d", proj_type="ortho")
        self.axe = fig.add_subplot(111, projection="3d", proj_type="ortho")
        res = expc(self.t)
        (self.line,) = self.axe.plot(self.t, np.real(res), np.imag(res))

        self.axe.set_xlabel("t", labelpad=30)
        self.axe.set_ylabel(r"$Re[e^{pt}]$", labelpad=30)
        self.axe.set_zlabel(r"$Im[e^{pt}]$", labelpad=30)

        self.axe.set_title(
            r"L'exponentielle complexe $e^{pt} = e^{σt}e^{ιωt} = "
            r"e^{σt} × [cos(ωt) + ι sin(ω t)]$, $p = σ + ι ω$",
        )
        # self.axe.set_aspect("auto")
        # self.axe.set_box_aspect(
        #     [ub - lb for lb, ub in (getattr(self.axe, f"get_{a}lim")() for a in "xyz")]
        # )
        # plt.tight_layout()

    def interact(
        self,
        A: (0, 2, 10) = 1,
        σ: (-0.3, 0.3, 10) = 0.2,
        ω: (-10.0, 10.0, 10) = 5,
        pr: "Im." = None,
        pi: "Re." = None,
        pt: "Proj. t" = None,
    ):
        res = expc(self.t, A=A, r=σ, ω=ω)
        self.line.set_data_3d(self.t, np.real(res), np.imag(res))

        if pr:
            self.axe.view_init(elev=0, azim=-90)

        if pi:
            self.axe.view_init(elev=90, azim=-90)

        if pt:
            self.axe.view_init(elev=0, azim=0)
