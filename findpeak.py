import numpy as np
from scipy import signal
xs = np.arange(0, np.pi, 0.05)
data = np.sin(xs)
print(data)
peakind = signal.find_peaks_cwt(data, np.arange(1,10))
peakind, xs[peakind], data[peakind]