import math
from pprint import pprint
from FFTutils import initlist, butterfly


def W(n, N):
    result = math.e ** complex(0, -2 * math.pi * n / N)         # Twiddle factor function
    return result


def dit_fft(series):
    obj, digt = initlist(series)
    length = 2 ** digt
    for i in range(digt):
        leap = 2 ** i
        group = 2 ** (i + 1)
        medium = obj.copy()
        for k in range(length // group):
            for j in range(leap):                               # Core algebra of FFT recursion
                medium[j + k * group], medium[j + leap + k * group] = butterfly(obj[j + k * group],
                                                                                obj[j + leap + k * group],
                                                                                W(j, 2 ** group))
        obj = medium
    return obj


if __name__ == '__main__':
    demolist = [1, 1, 1, 1, 1, 1, 1, 1]
    pprint(dit_fft(demolist))
