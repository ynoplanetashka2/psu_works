import sys
import argparse
import numpy as np
import time
from datetime import datetime, timedelta

from src.setup_arduino import setup_arduino, setup_arduino_mock
from src.setup_multimeter import setup_multimeter, setup_multimeter_mock


#CLI
parser = argparse.ArgumentParser(description='CLI for research facility controlling script')
parser.add_argument(
        '-m', 
        '--mock', 
        help='use multimeter and serial mock objects',
        action='store_true'
        )
parser.add_argument(
        '--iter-count',
        help='iterations count, default is 1',
        default=1,
        type=int
        )
parser.add_argument(
        '--iter-time',
        help='one iteration time, default is 5.0 sec',
        default=5.0,
        type=float
        )
parser.add_argument(
        '--delete-records',
        help='deletes all saved records data',
        action='store_true'
        )

ARGS = parser.parse_args()

if ARGS.delete_records:
    print('error: not implemented')
    exit(2)

#utils
def _throw(err_txt):
    raise Exception(err_txt)

now = datetime.now
timestamp = datetime.timestamp

print('setupping arduino and multimeter')

setup_arduino_func = setup_arduino if not ARGS.mock else setup_arduino_mock
arduino = setup_arduino_func('COM7', 0.1, 9600)
print('arduino got setupped')

#arduino messaging api
def wr(data):
    arduino.write(bytes(str(data), 'utf-8'))
    time.sleep(0.05)

def rd():
    data = arduino.readline()
    time.sleep(0.010)
    return data


setup_multimeter_func = setup_multimeter if not ARGS.mock else setup_multimeter_mock
multimeter = setup_multimeter_func()
print('multimeter got setupped')

#multimeter commands api
def multimeter_read():
    voltage = multimeter.query('READ?', 0.1)
    return float(voltage)

#circuit configuration
shunt_resistor = 97.3 #Ohm
generator_voltage = 10 # AC V
current_freqency = 100 #Hz
power_keys_count = 9

first_pin_index = 2

def calculate_current(shunt_voltage):
    current = shunt_voltage / shunt_resistor
    return current

def calculate_resistance(shunt_voltage):
    current = calculate_current(shunt_voltage)
    X_voltage = generator_voltage - shunt_voltage
    X_resistance = X_voltage / current
    return X_resistance


def calculate_output(record_index, parameter_values):
    output_str = f'{record_index}; {now()}'
    for i in range(parameter_values.shape[0]):
        value = parameter_values[i]
        output_str += f'; {value:.4}'
    return output_str

voltage_file = open('./records/voltage_data.csv', 'a')
current_file = open('./records/current_data.csv', 'a')
resistance_file = open('./records/resistance_data.csv', 'a')

all_files = (voltage_file, current_file, resistance_file)

#main logic

#labels generation
records_date_label = f'records date: {now()}'

pins_labels = list(map(lambda ind: f'pin_{ind}', range(first_pin_index, power_keys_count + first_pin_index)))
pins_label = '; '.join(pins_labels)

record_columns_names = f'record_index; record_date; {pins_label}'

#appending records labels
for file in all_files:
    file.write('\n')
    file.write(records_date_label + '\n')
    file.write(record_columns_names + '\n')

#date saving
records_start_time = now()
cur_record_time = records_start_time

print(f'start recording at {now()}')
for iter_index in range(ARGS.iter_count):
    is_last_cycle = iter_index == ARGS.iter_count - 1

    voltages = np.empty(power_keys_count, float)
    currents = np.empty(power_keys_count, float)
    resistances = np.empty(power_keys_count, float)

    all_parameters = (voltages, currents, resistances)

    for i in range(power_keys_count):
        wr(i + first_pin_index)
        voltage = multimeter_read()
        current = calculate_current(voltage)
        resistance = calculate_resistance(voltage)
        voltages[i] = voltage
        currents[i] = current
        resistances[i] = resistance

    #writes -1 in order to lock all relays
    wr(-1)

    for file, parameter in zip(all_files, all_parameters):
        output_data = calculate_output(iter_index, parameter)
        line_ending = '\n' if not is_last_cycle else ''
        file.write(output_data + line_ending)
        file.flush()

    cur_record_time, pre_record_time = now(), cur_record_time
    iteration_time = timestamp(cur_record_time) - timestamp(pre_record_time)
    sleep_delay = max(0, ARGS.iter_time - iteration_time)
    print(f'cycle #{iter_index}: all points are measured within {iteration_time} s')

    if is_last_cycle:
        print(f'last cycle ended')
        break

    print(f'waiting for next cycle start for next {sleep_delay} s')
    time.sleep(sleep_delay)
    cur_record_time = now()

records_end_time = now()
total_records_time = timestamp(records_end_time) - timestamp(records_start_time)
print(f'end recording at {now()}')
print(f'total recoring time: {total_records_time} seconds')
