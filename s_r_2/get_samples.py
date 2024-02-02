import csv

def flatten(_list):
    return [item for sublist in _list for item in sublist]

def get_samples():
    jump_rest = csv.reader(open('./data_jump_rest.csv'), delimiter='\t')
    jump_act = csv.reader(open('./data_jump_act.csv'), delimiter='\t')
    sit_act = csv.reader(open('./data_sit_act.csv'), delimiter='\t')
    sit_rest = csv.reader(open('./data_sit_rest.csv'), delimiter='\t')
    lazy_rest = csv.reader(open('./data_lazy_rest.csv'), delimiter='\t')
    lazy_act = csv.reader(open('./data_lazy_act.csv'), delimiter='\t')

    jump_rest = flatten(jump_rest)
    jump_act = flatten(jump_act)
    sit_rest = flatten(sit_rest)
    sit_act = flatten(sit_act)
    lazy_rest = flatten(lazy_rest)
    lazy_act = flatten(lazy_act)

    return (jump_rest, jump_act, sit_rest, sit_act, lazy_rest, lazy_act)
