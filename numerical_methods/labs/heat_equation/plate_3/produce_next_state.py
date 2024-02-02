L_VALUE = 10;
H_VALUE = 10;

XI = 1e-3;

BOUNDARY_TEMP = 0;
MID_TEMP = 1;
INITIAL_TEMP = .5;

COORD_STEP = 3.3e-1;
TIME_STEP = COORD_STEP**2 / 4;

def produce_next_state(cur_state, i, j):
    return (
        cur_state[i][j] 
        + XI * (TIME_STEP / COORD_STEP**2) 
        * (
            (cur_state[i + 1][j] - 2*cur_state[i][j] + cur_state[i - 1][j]) 
            + (cur_state[i][j + 1] - 2*cur_state[i][j] + cur_state[i][j - 1])
        )    
    )