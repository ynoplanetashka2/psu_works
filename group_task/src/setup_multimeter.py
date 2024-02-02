import time
import pyvisa as pyv
from random import random as rand

#connecting to multimeter
def setup_multimeter():
    rm = pyv.ResourceManager()
    resources_list = rm.list_resources()
    #print(resources_list)
    vm_name = None
    for resource_name in resources_list:
        if resource_name.startswith('USB'):
            vm_name = resource_name
            break

    if not vm_name:
        _throw('voltemeter not found')

    multimeter = rm.open_resource(vm_name)

    #configuring multimeter
    #multimeter.read_termination = '\n' ??
    multimeter.write_termination = '\n'

    multimeter.write('CONF:VOLT:AC 10, 0.001')
    time.sleep(0.1)
    multimeter.write('TRIG:SOUR BUS')
    time.sleep(0.1)
    multimeter.write('TRIG:DEL 0.2')
    time.sleep(0.1)

    return multimeter

class Multimeter_mock:
    def query(*args):
        return 0.5 + rand()

#mock setup
def setup_multimeter_mock(*args):

    return Multimeter_mock
