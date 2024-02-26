import tkinter as tk

import numpy as np
from plot import plot

TIMER_INTERVAL = 30
TAU_0 = 30
TEMP_0 = 100
T_INI = 0

def iteration(T, delta_t, p_relative):
    delta_T = (p_relative * TEMP_0 / TAU_0 - T / TAU_0) * delta_t
    return T + delta_T

def setup_window(compute_p):
    window = tk.Tk()
    lbl = None
    T_value = T_INI
    T_all_values = [T_value]
    (ax, canvas) = plot(window, T_all_values)

    def timer_tick():
        nonlocal T_value
        p_relative = compute_p(T_value)
        res = iteration(T_value, TIMER_INTERVAL / 1000, p_relative)
        T_value = res
        T_all_values.append(T_value)
        lbl.config(text=res)
        domain = np.arange(len(T_all_values)) * TIMER_INTERVAL
        ax.plot(domain, T_all_values, color='blue')
        ax.set_xlim((max(0, domain[-1] - 10 * 1000), domain[-1]))
        canvas.draw()
        window.update()
        window.after(TIMER_INTERVAL, timer_tick)
    lbl = tk.Label()
    lbl.pack()
    window.after(0, timer_tick)
    window.geometry("500x500")
    window.mainloop()