import numpy as np

title = "TF de signaux finis"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"
dontload = True


class Demo:
    def __init__(self, fig):
        fig.clf()
        self.axes = fig.subplots(2, 1)
        N = 1000
        self.Ntile = 100
        self.time = np.linspace(0.0, 3.0, N)
        Fe = 1 / (self.time[1] - self.time[0])
        self.freq = np.arange(self.Ntile * N) * 1 / ((self.time[1] - self.time[0]) * self.Ntile * N)
        self.freq = np.fft.fftshift(np.fft.fftfreq(self.Ntile * N)) * Fe
        sig, ft = self.gensig(1)
        (self.line0, ) = self.axes[0].plot(self.time, sig )
        (self.line1, ) = self.axes[1].plot(self.freq, ft)
        self.axes[1].set_xlim([-10, 10])

    def gensig(self, length):
        sig = np.ones_like(self.time)
        sig[self.time < 1.5 - length / 2] = 0
        sig[1.5 + length / 2 < self.time] = 0
        return sig, np.fft.fftshift(np.abs(np.fft.fft(np.tile(sig, self.Ntile), norm="ortho")))
        # return sig, np.abs(np.fft.fft(np.tile(sig, 100)))

    def interact(self, T: (0.5, 2) = 1.5):
        sig, ft = self.gensig(T)
        self.line0.set_ydata(sig)
        self.line1.set_ydata(ft)


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    plt.ion()
    d = Demo(plt.figure(1))
    d.interact(0.5)
    plt.show()
