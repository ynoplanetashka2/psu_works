# 38В1
import time
from setup_window import setup_window
from setup_controller import setup_controller
import numpy as np

def hex2(char):
    res = hex(np.ubyte(char))[2:].upper()
    if len(res) == 1:
        return '0' + res
    return res

def main():
    # for i in range(256):
    address = 1
    setup_controller_result = setup_controller(address=hex2(address))
    query = setup_controller_result['query']
    def insert_value(**kwargs):
        insert_value = kwargs['insert_value']
        command='0300000001'
        response = query(command)
        print(type(response))
        print(response)
        insert_value(response)
        time.sleep(1)
    setup_window(main=insert_value)

if __name__ == '__main__':
    main()
