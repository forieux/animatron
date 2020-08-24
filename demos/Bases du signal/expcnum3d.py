import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

title = "Exponentielle complexe num. 3D"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


def expc(n, m=1.03, φ=0.2):
    z = m * np.exp(1j * φ)
    return z ** n


class Demo:
    def __init__(self, fig):
        fig.clf()

        self.n = np.arange(-30, 30)
        self.axe = fig.add_subplot(111, projection="3d", proj_type="ortho")
        res = expc(self.n)
        (self.line,) = self.axe.plot(
            self.n, np.real(res), np.imag(res), color="C0", alpha=0.4
        )
        (self.marker,) = self.axe.plot(
            self.n, np.real(res), np.imag(res), "o", color="C0"
        )
        self.axe.set_ylim([-5, 5])
        self.axe.set_zlim([-5, 5])
        # self.axe.grid("on")

        # self.axe.set_xlabel("t")
        # self.axe.set_ylabel(r"$Re[e^{pt}]$")
        # self.axe.set_zlabel(r"$Im[e^{pt}]$")

        # self.axe.set_title(
        #     r"L'exponentielle complexe $e^{pt} = e^{rt}e^{iφt} = e^{rt} (cos(φt) + sin(φ t))$, $p = r + i φ$",
        # )

    def interact(
        self,
        m: (0.95, 1.05, 20) = 1,
        φ: (-0.5, 0.5, 10) = 0.2,
        pr: "Im." = None,
        pi: "Re." = None,
        pt: "Proj. t" = None,
    ):
        res = expc(self.n, m=m, φ=φ)
        self.line.set_data_3d(self.n, np.real(res), np.imag(res))
        self.marker.set_data_3d(self.n, np.real(res), np.imag(res))
        # self.line.set_ydata(np.real(res))
        # self.marker.set_ydata(np.real(res))

        if pr:
            self.axe.view_init(elev=0, azim=-90)

        if pi:
            self.axe.view_init(elev=90, azim=-90)

        if pt:
            self.axe.view_init(elev=0, azim=0)


if __name__ == "__main__":
    plt.ion()
    fig = plt.figure(1)
    plt.clf()
    d = Demo(fig)
    plt.show()


# plt.ion()
# fig = plt.figure(1)
# plt.clf()
# d = Demo(fig)
# plt.show()
