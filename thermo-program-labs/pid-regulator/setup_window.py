import tkinter as tk
from plot import plot

TIMER_INTERVAL = 300
TAU_0 = 50
TEMP_0 = 10
T_INI = 0
T_SP = 30
HE = 0.2

def iteration(T, delta_t, p_relative):
    delta_T = (p_relative * T_SP / TAU_0 - T / TAU_0) * delta_t
    return T + delta_T

def compute_p(T):
    if T >= T_SP + HE:
        return 0
    return 1

def setup_window():
    window = tk.Tk()
    lbl = None
    T_value = T_INI

    def timer_tick():
        nonlocal T_value
        p_relative = compute_p(T_value)
        res = iteration(T_value, TIMER_INTERVAL / 1000, p_relative)
        T_value = res
        lbl.config(text=res)
        plot(window)
        window.after(TIMER_INTERVAL, timer_tick)
    lbl = tk.Label()
    lbl.pack()
    window.after(0, timer_tick)
    window.geometry("500x500")
    window.mainloop()