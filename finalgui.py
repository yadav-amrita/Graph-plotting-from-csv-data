import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import pandas as pd
from itertools import count

# Load the CSV data
df = pd.read_csv('C:\\Users\\Amrita\\OneDrive\\Documents\\pandasApp\\pfrcsv.csv')

# Initialize lists for data
pressure = []
altitude = []
time = []
velocity = []

# Create the main window
root = tk.Tk()
root.title("Cansat")

# Function to handle button clicks
def button_click(button_name):
    messagebox.showinfo("Button Clicked", f"You clicked the {button_name} button")

# Create and place buttons
buttons = [
    "0 Boot",
    "1 Test_Mode",
    "2 Launch_PAD",
    "3 Ascent",
    "4 Descent",
    "5 Rocket_Deploy",
    "6 Aerobrake Release",
    "7 Impact"
]

for button_name in buttons:
    button = tk.Button(root, text=button_name, font=("Arial", 14),
                       command=lambda bn=button_name: button_click(bn))
    button.pack(side=tk.BOTTOM, anchor="se")

# Create a matplotlib figure and axis
fig, ax = plt.subplots()
ax.set_xlabel('Time')
ax.set_ylabel('Pressure')
line_pressure, = ax.plot([], [], label='Pressure')
line_altitude, = ax.plot([], [], label='Altitude')

# Create the canvas to embed the plot in the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Animation update function
def update(i):
    idx = next(counter)
    if idx >= len(df):
        return
    pressure.append(df.iloc[idx, 4])
    time.append(df.iloc[idx, 7])
    velocity.append(df.iloc[idx, 10])
    altitude.append(df.iloc[idx, 3])
    
    ax.clear()
    ax.set_xlabel('Time')
    ax.set_ylabel('Pressure')
    ax.plot(time, pressure, label='Pressure')
    ax.plot(time, altitude, label='Altitude')
    ax.legend()
    plt.xlim(0, max(time[-1], 10))  # Set xlim based on data or default to 10

# Create a counter for the animation
counter = count(0, 1)
ani = FuncAnimation(fig, update, interval=1000)

# Start the Tkinter event loop
root.mainloop()
