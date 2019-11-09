import math

import matplotlib.pyplot as plt

from FFTutils import initlist, butterfly


def W(n, N):
    result = math.e ** complex(0, -2 * math.pi * n / N)  # Twiddle factor function
    return result


def dit_fft(series):
    obj, digt = initlist(series)
    length = 2 ** digt
    for i in range(digt):
        leap = 2 ** i
        group = 2 ** (i + 1)
        medium = obj.copy()
        for k in range(length // group):
            for j in range(leap):  # Core algebra of FFT recursion
                medium[j + k * group], medium[j + leap + k * group] = butterfly(obj[j + k * group],
                                                                                obj[j + leap + k * group],
                                                                                W(j, 2 ** group))
        obj = medium
    Rseries = []
    Iseries = []
    raw = []
    for i in range(len(obj)):
        Rseries.append(abs(obj[i].real))
        Iseries.append(obj[i].imag)
        raw.append(obj[i])

    return Rseries, Iseries, raw


if __name__ == '__main__':
    demolist = [math.sin(i * math.pi / 8) for i in range(128)]
    YR, YI, raw = dit_fft(demolist)
    X = [i for i in range(len(YR))]

    origin = plt.subplot(211)
    origin.set_xlabel('Time')
    origin.set_ylabel('Amp')
    origin.stem(X, demolist)
    origin.set_title('Time-Sequence')

    freq = plt.subplot(212)
    freq.set_xlabel('Freq')
    freq.set_ylabel('Amp')
    freq.set_title('Freq-Sequence')
    freq.stem(X, YR)
    plt.show()
