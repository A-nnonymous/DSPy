from math import ceil, log2
import math

def initlist(series):
    if log2(len(series)) % 1:                               # Zeroize series to satisfy FFT algebra
        newdit = ceil(log2(len(series)))
        newlen = 2 ** newdit
        aplen = newlen - len(series)
        for i in range(aplen):
            series.append(0)
    else:
        newdit = log2(len(series))
        newdit = int(newdit)
        newlen = 2 ** newdit
    indexlist = []

    for i in range(newlen):                                 # Align the string to fixed length and reverse in binomial
        ind = bin(i)[2:]
        if len(ind) < newdit:
            for j in range(newdit - len(ind)):
                ind = '0' + ind
        ind = ind[::-1]
        newind = trim(ind)                                  # Some string magics :)
        newind = '0b' + newind                              # Concatenate in order to transform to decimal
        ind = int(newind, 2)
        indexlist.append(ind)
    obj = series.copy()
    series = []
    for i in indexlist:
        series.append(obj[i])
    return series, newdit


def trim(string):
    for i in range(len(string)):                            # String magics
        if string[i:].startswith('0'):
            if i == len(string) - 1:
                return '0'
            else:
                continue
        else:
            break
    return string[i:]

def twiddle(digt, conjugate = 0):
    WN= []
    if not conjugate:
        for n in range(2**(digt-1)):
            i= complex(0, 1.0)
            power = -2 * math.pi * n * i / 2**digt
            result = math.e ** power
            WN.append(result)
    else:
        for n in range(2**(digt-1)):
            i= complex(0, 1.0)
            power = -2 * math.pi * n * i / 2**digt
            result = math.e ** power
            WN.append(result.conjugate())

    return WN


def butterfly(x1, x2, wn):                                   # Just a little butterfly
    y1 = x1 + x2 * wn
    y2 = x1 - x2 * wn
    return y1, y2

