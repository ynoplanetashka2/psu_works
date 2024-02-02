import sys
import json
import numpy as np
import scipy.stats as stats


input1_file_name = sys.argv[1]

input1_file = open(input1_file_name, 'r')

input1_file_text = input1_file.read()
data1 = json.loads(input1_file_text)

data2 = data1['delayed_tests']['matches']
data1 = np.array(data1['immediate_tests']['matches'])
data2 = np.array(data2)

print(stats.ttest_ind(data1, data2))
