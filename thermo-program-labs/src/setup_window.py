import tkinter as tk

def setup_window(**kwargs):
    main = kwargs['main']
    window = tk.Tk()
    lbl = None
    def insert_value(value):
        # entry.insert(tk.END, content + ' hello world')
        lbl.config(text=value)

    btn = tk.Button(
        text='trigger',
        width=25,
        height=5,
        command=lambda: main(insert_value=insert_value)
    )
    lbl = tk.Label()
    btn.pack()
    lbl.pack()
    # window.after(0, lambda: main(insert_value=insert_value))
    window.mainloop()