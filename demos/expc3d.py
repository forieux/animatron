import numpy as np
from mpl_toolkits.mplot3d import Axes3D

title = "Exponentielle complexe 3D"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


def expc(t, r=0.2, ω=5):
    p = r + 1j * ω
    return np.exp(2 * np.pi * p * t)


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.t = np.linspace(-1, 1, 1000)
        self.axe = fig.add_subplot(111, projection='3d', proj_type='ortho')
        res = expc(self.t)
        (self.line,) = self.axe.plot(
            self.t, np.real(res), np.imag(res)
        )

        self.axe.set_xlabel("t")
        self.axe.set_ylabel(r"$Re[e^{pt}]$")
        self.axe.set_zlabel(r"$Im[e^{pt}]$")

        self.axe.set_title("L'exponentielle complexe $e^{pt}$, $p = r + i ω$")

    def interact(self, r: (-0.3, 0.3, 10) = 0.2, ω: (-10.0, 10.0, 10) = 5):
        res = expc(self.t, r=r, ω=ω)
        self.line.set_data_3d(self.t, np.real(res), np.imag(res))

    # interact(update, r=(-0.2, 0.2, 0.05), ω=(-10, 10))
