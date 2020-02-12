import numpy as np

title = "Repliement d'un sinus"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.axes = fig.subplots(2, 1)
        length = 1000
        self.time = np.linspace(0.0, 2 * np.pi, length)
        dt = self.time[2] - self.time[1]
        self.freq = np.arange(length) / (length * dt)
        sig = np.sin(2 * np.pi * self.time)
        (self.line,) = self.axes[0].plot(self.time, sig)
        self.axes[0].set_xlabel("t [s]")
        self.axes[0].set_title("s(t)")
        (self.linef,) = self.axes[1].plot(self.freq, np.abs(np.fft.fft(sig)))
        self.axes[1].set_xlabel("ν [Hz]")
        self.axes[0].set_xlim([0, 1])
        self.axes[1].set_title("S(ν) = TF[s(t)]")

    def interact(self, freq: (1, 200, 100) = 1):
        sig = np.sin(2 * freq * np.pi * self.time)
        sigf = np.abs(np.fft.fft(sig))
        self.line.set_ydata(sig)
        self.linef.set_ydata(sigf)


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plt.ion()
    d = Demo(plt.figure())
    d.interact(3)
    plt.show()
