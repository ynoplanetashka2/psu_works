import tkinter as tk

def setup_window(**kwargs):
    entry = None
    window = tk.Tk()
    def anon():
        content = entry.get()
        entry.insert(tk.END, content + ' hello world')

    btn = tk.Button(
        text='trigger',
        width=25,
        height=5,
        command=anon
    )
    entry = tk.Entry()
    btn.pack()
    entry.pack()
    window.mainloop()

    return 123
