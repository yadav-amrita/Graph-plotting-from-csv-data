import matplotlib.pyplot as plt  
from matplotlib.animation import FuncAnimation
import pandas as pd
from itertools import count

# Load data
df = pd.read_csv('C:\\Users\\Amrita\\OneDrive\\Documents\\pandasApp\\pfrcsv.csv')

# Initialize lists
pressure = []
altitude = []
time = []
velocity = []

# Create figure and axis
fig, ax = plt.subplots()

# Create initial lines for pressure, altitude, and velocity
line_pressure, = ax.plot([], [], label='Pressure', color='r')
line_altitude, = ax.plot([], [], label='Altitude', color='g')
line_velocity, = ax.plot([], [], label='Velocity', color='b')

# Set labels, title, and legend
ax.set_xlabel('Time')
ax.set_ylabel('Values')
ax.set_xlim(0, 10)  # Adjust as necessary
ax.set_ylim(-1, 1)  # Adjust as necessary for your data
ax.legend()

# Counter for indexing
counter = count(0, 1)

def update(i):
    idx = next(counter)
    
    # Ensure idx does not exceed the length of df
    if idx < len(df):
        # Append new data
        pressure.append(df.iloc[idx, 4])
        time.append(df.iloc[idx, 7])
        velocity.append(df.iloc[idx, 10])
        altitude.append(df.iloc[idx, 3])
        
        # Update line data
        line_pressure.set_data(time, pressure)
        line_altitude.set_data(time, altitude)
        line_velocity.set_data(time, velocity)
        
        # Adjust limits if necessary
        ax.relim()
        ax.autoscale_view()

# Create animation
ani = FuncAnimation(fig, update, interval=1000)

plt.show()
