import numpy as np
import re
import matplotlib.pyplot as plt
import sys
from scipy.io import wavfile
from os import listdir
from os.path import isfile, join

def fft(seq, step_size = 1, elements_count = 30):
    output = np.empty((elements_count, 2), float)
    for index in range(elements_count):
        domain = 2 * np.pi * index * step_size * np.arange(seq.size)
        a = np.sin(domain)
        b = np.cos(domain)
        a *= seq
        b *= seq
        a = np.sum(a)
        b = np.sum(b)
        output[index, 0] = a
        output[index, 1] = b
    return output

def audio_freq(file_path, take_precents = 0.05, max_freq = 800):
    samplerate, data = wavfile.read(file_path)
    data = data[:,0] # read only 1-st channel
    data = data[data.size // 3:] # discard first 1/3 'cause its commonly def
    data = data[:round(data.size * take_precents)]
    domain = 1 / samplerate * np.arange(data.size)
    fourier_freq = fft(data, 1 / samplerate, max_freq)
    fourier_coef = np.linalg.norm(fourier_freq, axis=1)
    freq = np.argmax(fourier_coef)
    return freq

def _throw(txt):
    raise Exception(txt)

audio_path = 'audio'
output_file_name = sys.argv[1] if len(sys.argv) >= 1 else _throw('output file was not provided')
output_file = open(output_file_name, 'w')
iter_count = 0
for file_name in listdir(audio_path):
    print(f'iter_count={iter_count}')
    iter_count += 1
    file_path = join(audio_path, file_name)
    if not isfile(file_path):
        continue
    base_name = '.'.join(file_name.split('.')[0:-1])
    ext_name = file_name.split('.')[-1]
    #print(file_name, ext_name)
    if ext_name != 'wav':
        continue
    sample = re.search('(\d{1,2})_(\d{3})_(\d{1})', file_name)
    if not sample:
        continue
    sample_id = sample.group(1)
    sample_freq = sample.group(2)
    sample_try = sample.group(3)
    #print(f'id = {sample_id}; freq = {sample_freq}; try = {sample_try}')
    subject_freq = audio_freq(file_path, take_precents=0.50)
    output_line = f'{sample_id},{sample_try},{sample_freq},{subject_freq}\n'
    output_file.write(output_line)
