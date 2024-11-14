import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation 
df = pd.read_csv('C:/Users/Amrita/OneDrive/Documents/pandasApp/pfrcsv.csv')
#content = csv.reader('C:/Users/Amrita/OneDrive/Documents/pandasApp/pfrcsv.csv')
pressure = []
time = []
altitude = []
velocity = []
def draw_graph(i):
    if len(df):
            time = df['TIME_STAMPING']
            altitude = df['ALTITUDE']
            pressure=df['PRESSURE']
            velocity=df['GNSS_ALTITUDE']
            
anima = animation.FuncAnimation(plt.gcf(),draw_graph,interval=30000)
plt.ylabel('altitude')
plt.xlabel('time')
plt.cla()
plt.plot(time,altitude)
plt.show()
plt.ylabel('pressure')
plt.xlabel('time')
#plt.subplot(2,2,2)
plt.cla()
plt.plot(time,pressure)
plt.show()
plt.ylabel('pressure')
plt.xlabel('time')
#plt.subplot(2,2,3)
plt.ylabel('velocity')
plt.xlabel('time')
plt.cla()
plt.plot(time,velocity)
plt.show()
