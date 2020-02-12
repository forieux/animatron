import numpy as np
import sounddevice as sd
import soundfile as sf

title = "Sound"
authors = "F. Orieux"
email = "orieux@l2s.centralesupelec.fr"


class Demo:
    def __init__(self, fig):
        fig.clf()

        data, self.fs = sf.read("./demos/data/TheHudsuckerislost.wav", dtype="float32")
        duration = 5
        self.Fe = 44100
        self.N = duration * self.Fe
        self.data = data[: self.N, 0]
        self.dataf = np.abs(np.fft.fft(self.data))

        self.t = np.linspace(0, duration, self.N)
        self.f = np.arange(self.N) * self.Fe

        self.axes = fig.subplots(2, 1)
        self.plot()

    def plot(self, scale: float = 1.0):
        self.axes[0].cla()
        self.axes[1].cla()
        self.axes[0].plot(self.t / scale, self.data)
        self.axes[0].set_xlim([self.t[17500] / scale, self.t[30000]])
        self.axes[1].plot(self.f * scale, self.dataf)
        self.axes[1].set_xlim([0, self.f[self.N // 6]])

    def interact(self, n: "Normal", slow: "Slow", fast: "Fast", play: False):
        scale = 1
        sd.stop()
        if n:
            scale = 1
        if slow:
            scale = 0.7
        if fast:
            scale = 1.5

        if play:
            sd.play(self.data, self.fs * scale)

        self.plot(scale=scale)
