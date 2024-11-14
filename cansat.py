import csv
import matplotlib.pyplot as plt  
with open('pfrcsv.csv','r')as file:
    content = csv.reader(file)
    pressure = []
    altitude = []
    time = []
    velocity = []
    next(content)
    for row in content:
        print(row)
        if len(row):
            altitude.append(float(row[3]))
            pressure.append(float(row[4]))
            velocity.append(float(row[11]))
            time.append(str(row[7]))

plt.ylabel('altitude')
plt.xlabel('time')
plt.title('Altitue V/S Time Graph')   
plt.plot(time,altitude)
plt.show()  
plt.ylabel('pressure')
plt.xlabel('time')
plt.title('Pressure V/S Time Graph')   
plt.plot(time,pressure)
plt.show()       
plt.ylabel('velocity')
plt.xlabel('time')
plt.title('Velocity V/S Time Graph')   
plt.plot(time,velocity)
plt.show()  
