import matplotlib.pyplot as plt  
from matplotlib.animation import FuncAnimation
import numpy as np   
from itertools import count
import pandas as pd
df = pd.read_csv('C:\\Users\\Amrita\\OneDrive\\Documents\\pandasApp\\pfrcsv.csv')
pressure = []
altitude = []
time = []
velocity = []

fig,ax=plt.subplots()
ax.plot(time,pressure)
ax.plot(time,altitude)
ax.plot(time,pressure)
counter = count(0,1)
def update(i):
    
        idx = next(counter)
        pressure.append(df.iloc[idx,4])
        time.append(df.iloc[idx,7])
        velocity.append(df.iloc[idx,10])
        altitude.append(df.iloc[idx,3])
        #plt.cla()
        #plt.xlabel('time')
        #plt.ylabel('pressure')
        #ax.set_xlim(0,10)
        #ax.plot(time,pressure)
        plt.cla()
        plt.xlabel('time') 
        plt.ylabel('altitude') 
        ax.plot(time,altitude)
        #plt.cla()
        #plt.xlabel('time')
        #plt.ylabel('velocity')
        #ax.plot(time,velocity)
ani = FuncAnimation(fig=fig,func = update,interval = 100)
plt.show()
#ax.plot(altitude,time)
#ax.plot(velocity,time)