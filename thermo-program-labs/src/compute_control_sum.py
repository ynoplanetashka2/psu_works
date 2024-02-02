import binascii
# def to_hex(num):
#     return str('%#4x' % (0xffffffff & num))[]

def chunk_2(iter):
    return zip(
        iter[::2],
        iter[1::2],
    )
def digchar(char):
    byte_value = ord(char)
    byte_value -= ord('0')
    if byte_value > 41:
        return byte_value - 39
    if byte_value > 9:
        return byte_value - 7
    return byte_value

def LRC(line):
    acc = 0
    for (char1, char2) in chunk_2(line):
        acc += (digchar(char1) << 4) | digchar(char2)
    
    return (-acc)

def compute_control_sum(line):
    return LRC(line)

control_sum = compute_control_sum(':06030803AC03B603E8')
print(control_sum)
print(binascii.unhexlify(str(control_sum)))
exit()