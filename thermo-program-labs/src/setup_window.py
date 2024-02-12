import tkinter as tk

def setup_window(**kwargs):
    entry = None
    window = tk.Tk()
    def insert_value(value):
        content = entry.get()
        # entry.insert(tk.END, content + ' hello world')
        entry.insert(0, value)

    btn = tk.Button(
        text='trigger',
        width=25,
        height=5,
    )
    entry = tk.Entry()
    btn.pack()
    entry.pack()
    window.mainloop()

    return {
        'insert_value': insert_value,
    }