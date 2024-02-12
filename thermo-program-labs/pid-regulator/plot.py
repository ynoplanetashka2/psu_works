from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk) 

# plot function is created for 
# plotting the graph in 
# tkinter window 
def plot(window, data): 

    # the figure that will contain the plot 
    fig = Figure(figsize = (5, 5), 
                dpi = 100) 

    # adding the subplot 
    plot1 = fig.add_subplot(111) 

    # plotting the graph 
    plot1.plot(data) 

    # creating the Tkinter canvas 
    # containing the Matplotlib figure 
    canvas = FigureCanvasTkAgg(fig, 
                            master = window) 
    canvas.draw() 

    # placing the canvas on the Tkinter window 
    tk_widget = canvas.get_tk_widget() 
    tk_widget.pack()

    # creating the Matplotlib toolbar 
    toolbar = NavigationToolbar2Tk(canvas, 
                                window) 
    toolbar.update() 

    # placing the toolbar on the Tkinter window 
    canvas.get_tk_widget().pack() 
    return (plot1, canvas)


