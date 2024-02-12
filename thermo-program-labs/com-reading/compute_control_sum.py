import numpy as np
import warnings

def hex2(n):
    return hex(np.ubyte(n))[2:].upper()

def chunk_2(iter):
    return zip(
        iter[::2],
        iter[1::2],
    )
def digchar(char):
    byte_value = ord(char)
    byte_value -= ord('0')
    if byte_value > 41:
        return np.ubyte(byte_value - 39)
    if byte_value > 9:
        return np.ubyte(byte_value - 7)
    return np.ubyte(byte_value)

def LRC(line):
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')
        warnings.filterwarnings('ignore', r'overflow encountered')
        acc = np.ubyte(0)
        for (char1, char2) in chunk_2(line):
            acc += np.ubyte((digchar(char1) << 4) | digchar(char2))
    
        return np.ubyte(-np.byte(acc))

def compute_control_sum(line):
    return hex2(LRC(line))