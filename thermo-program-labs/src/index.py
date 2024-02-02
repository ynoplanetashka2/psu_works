# 38В1
from setup_window import setup_window
from setup_controller import setup_controller

def main():
    setup_controller_result = setup_controller()
    controller = setup_controller_result['controller']
    write_command = setup_controller_result['write_command']

    response = write_command('0301300001')
    # decoded = bytearray.fromhex(str(response)).decode()
    decoded = bytes.fromhex(str(response)).decode('ascii').encode('ascii', 'ignore')
    print(f'response: `{decoded}`')

if __name__ == '__main__':
    main()