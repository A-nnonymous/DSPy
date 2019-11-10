import math

import matplotlib.pyplot as plt

from FFTutils import initlist, butterfly, twiddle

import time


def dit_fft(series):
    obj, digt = initlist(series)
    length = 2 ** digt
    WN = twiddle(digt)

    for i in range(digt):
        leap = 2 ** i
        group = 2 ** (i + 1)
        medium = obj.copy()
        for k in range(length // group):
            for j in range(leap):  # Core algebra of FFT recursion
                medium[j + k * group], medium[j + leap + k * group] = butterfly(obj[j + k * group],
                                                                                obj[j + leap + k * group],
                                                                                WN[j*2**(digt-i-1)])
        obj = medium
    Rseries = []
    Iseries = []
    raw = []
    for i in range(len(obj)):
        Rseries.append(abs(obj[i].real))
        Iseries.append(obj[i].imag)
        raw.append(obj[i])

    return Rseries, Iseries, raw

def idft(Fseries):
    obj, digt = initlist(Fseries)
    length = 2 ** digt
    WN = twiddle(digt,conjugate=1)
    for i in range(digt):
        leap = 2 ** i
        group = 2 ** (i + 1)
        medium = obj.copy()
        for k in range(length // group):
            for j in range(leap):  # Core algebra of FFT recursion
                medium[j + k * group], medium[j + leap + k * group] = butterfly(obj[j + k * group],
                                                                                obj[j + leap + k * group],
                                                                                WN[j*2**(digt-i-1)])
        obj = medium
    Rseries = []
    Iseries = []
    raw = []
    for i in range(len(obj)):
        Rseries.append((obj[i].real/length))
        Iseries.append(obj[i].imag/length)
        raw.append(obj[i]/length)

    return Rseries, Iseries, raw

if __name__ == '__main__':
    demolist = [math.sin(i * math.pi / 8) for i in range(512)]
    start_time= time.time()
    YR, YI, raw = dit_fft(demolist)
    end_time= time.time()
    print('Time cost:', end_time-start_time)
    yr, yi, y_ = idft(raw)
    X = [i for i in range(len(YR))]

    plt.figure(figsize=(16,10), dpi =70)
    origin = plt.subplot(311)
    origin.set_xlabel('Time')
    origin.set_ylabel('Amp')
    origin.stem(X, demolist)
    origin.set_title('Time-Sequence')

    freq = plt.subplot(312)
    freq.set_xlabel('Freq')
    freq.set_ylabel('Amp')
    freq.set_title('Freq-Sequence')
    freq.stem(X, YR)

    app = plt.subplot(313)
    app.set_xlabel('Time')
    app.set_ylabel('Amp')
    app.stem(X, yr)
    app.set_title('Time-SequenceA')
    plt.show()
