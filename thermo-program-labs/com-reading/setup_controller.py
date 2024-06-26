from binascii import unhexlify
import numpy as np
import pyvisa as pyv
from compute_control_sum import compute_control_sum

def _throw(err):
    raise Exception(err)

#connecting to controller
def setup_controller(**kwargs):
    controller_address = kwargs['address'] if 'address' in kwargs else '01'
    rm = pyv.ResourceManager()
    resources_list = rm.list_resources()
    vm_name = None
    for resource_name in resources_list:
        if resource_name.startswith('ASRL'):
            vm_name = resource_name
            break

    if not vm_name:
        _throw('controller not found')

    controller = rm.open_resource(vm_name, baud_rate=115200)

    #configuring controller
    controller.read_termination = '\r\n'
    controller.timeout = 300
    controller.write_termination = '\r\n'

    def query(command_code):
        COMMAND_PREFIX = ':'
        msg_without_control_sum = f'{controller_address}{command_code}'
        control_sum = compute_control_sum(msg_without_control_sum)
        msg = f'{COMMAND_PREFIX}{msg_without_control_sum}{control_sum}'
        print('msg: ', msg)
        res = None
        try:
            while True:
                res = controller.query(msg)
                if res[0:4] != msg[0:4]:
                    continue
                break
            controller.clear()
        except pyv.VisaIOError:
            return None
        # return res[4:]
        temperature = res[7:7+4]
        print(f'bare response {res}: temperature: {temperature}')
        result = np.short(int.from_bytes(unhexlify(temperature), "big")) / 100
        return result

    return {
        'controller': controller,
        'query': query,
    }