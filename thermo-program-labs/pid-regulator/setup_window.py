import tkinter as tk

import numpy as np
from plot import plot

# frames interval (in milis)
TIMER_INTERVAL = 30
# impulse interval (in timer interval)
IMPULSE_INTERVAL = 10
TAU_0 = 15
TEMP_0 = 100

def iteration(T, delta_t, p_relative):
    delta_T = (p_relative * TEMP_0 / TAU_0 - T / TAU_0) * delta_t
    return T + delta_T

def setup_window(compute_p, T_INI):
    window = tk.Tk()
    lbl = None
    T_value = T_INI
    T_all_values = [T_value]
    (ax, canvas) = plot(window, T_all_values)
    lbl = tk.Label()
    checkvar = tk.BooleanVar(value=False)
    checkbox = tk.Checkbutton(text="Power", variable=checkvar)
    p_relative = 0

    def timer_tick():
        nonlocal T_value, p_relative
        if (len(T_all_values) - 1) % IMPULSE_INTERVAL == 0:
            p_relative = compute_p(T_all_values[::IMPULSE_INTERVAL])
        checkvar.set(p_relative > 0)
        p_relative -= 1 / IMPULSE_INTERVAL
        if p_relative > 0:
            res = iteration(T_value, TIMER_INTERVAL / 1000, 1)
        else:
            res = iteration(T_value, TIMER_INTERVAL / 1000, 0)
        T_value = res
        T_all_values.append(T_value)
        lbl.config(text=res)
        domain = np.arange(len(T_all_values)) * TIMER_INTERVAL
        ax.plot(domain, T_all_values, color='blue')
        ax.set_xlim((max(0, domain[-1] - 5 * 1_000), domain[-1]))
        canvas.draw()
        window.update()
        window.after(TIMER_INTERVAL, timer_tick)
    lbl.pack()
    checkbox.pack()
    window.after(0, timer_tick)
    window.geometry("500x600")
    window.mainloop()