import time
import pyvisa as pyv
from compute_control_sum import compute_control_sum
from random import random as rand

def _throw(err):
    raise Exception(err)

#connecting to controller
def setup_controller(**kwargs):
    controller_address = kwargs['address'] if 'address' in kwargs else '01'
    rm = pyv.ResourceManager()
    resources_list = rm.list_resources()
    # print(resources_list)
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
    controller.write_termination = '\r\n'

    def write_command(command_code):
        msg_without_control_sum = f':{controller_address}{command_code}'
        control_sum = compute_control_sum(msg_without_control_sum)
        msg = f'{msg_without_control_sum}{control_sum}'
        print('msg: ', msg)
        return controller.write(msg)

    # multimeter.write('CONF:VOLT:AC 10, 0.001')
    # time.sleep(0.1)
    # multimeter.write('TRIG:SOUR BUS')
    # time.sleep(0.1)
    # multimeter.write('TRIG:DEL 0.2')
    # time.sleep(0.1)

    return {
        'controller': controller,
        'write_command': write_command,
    }