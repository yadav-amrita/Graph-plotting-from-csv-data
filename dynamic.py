import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt   
from matplotlib.animation import FuncAnimation

GNSS_TIME = []
y_values = []

index = count()

def animate(i):
    data = pd.read_cssv('pfrcsv.csv')
    x = data['GNSS_TIME']
    y1 = data['ALTITUDE']
    y2 = data['PRESSURE']
    y3 = data['GNSS_ALTITUDE']
    plt.cla()
    
    plt.plot(x,y1,label='Altitude V/S Time Graph')
    plt.plot(x,y2,label='Pressure V/S Time Graph')
    plt.plot(x,y3,label='Velocity V/S Time Graph')
    
    plt.tight_layout()
    if len(data):   
     ani = FuncAnimation(plt.gcf(),animate,interval=30000)

plt.tight_layout()
plt.show()