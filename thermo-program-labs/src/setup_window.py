import tkinter as tk

def setup_window(**kwargs):
    main = kwargs['main']
    window = tk.Tk()
    lbl = None

    def timer_tick():
        res = main()
        lbl.config(text=res)
        window.after(300, timer_tick)

    btn = tk.Button(
        text='trigger',
        width=25,
        height=5,
    )
    lbl = tk.Label()
    btn.pack()
    lbl.pack()
    window.after(0, timer_tick)
    window.mainloop()