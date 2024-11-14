import csv
import matplotlib.pyplot as plt
#with open('C:/Users/Amrita/Downloads/pfrcsv.csv')as file:
    #content = csv.reader(file)
    #for row in content:
        #print(row)
with open('pfrcsv.csv', 'r')as file:
    content = csv.reader(file)
    pressure = []
    time = []
    next(content)
    for row in content:
        print(row)
#    for row in content:
#        pressure.append(float(row[4]))
#        time.append(str(row[7]))
#plt.plot(pressure,time)
#plt.show()