# 38В1
from setup_window import setup_window
from setup_controller import setup_controller
import numpy as np

def hex2(char):
    res = hex(np.ubyte(char))[2:].upper()
    if len(res) == 1:
        return '0' + res
    return res

def main():
    for i in [1]:
        setup_controller_result = setup_controller(address=hex2(i))
        controller = setup_controller_result['controller']
        write_command = setup_controller_result['write_command']
        controller_net_id = '06'
        command = '030803AC03B603A203E8'
        # command = '0300000001'
        response = write_command(command)
        resp = np.ushort(response)
        chr1 = chr(resp & 0xff)
        chr2 = chr((resp & 0xff00) >> 2 )
        print(type(response))
        # response = write_command('0301300001')
        # decoded = bytearray.fromhex(str(response)).decode()
        # decoded = bytes.fromhex(str(response)).decode('ascii').encode('ascii', 'ignore')
        print(f'response: `{chr1}{chr2}`')

if __name__ == '__main__':
    main()