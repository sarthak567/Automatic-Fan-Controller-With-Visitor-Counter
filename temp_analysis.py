import serial
import re
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from drawnow import *
import time

# com port initialization
portPath = "COM3"
baud = 9600
sample_time = 0.1
sim_time = 100

# Temp Data collection
data_log = []
line_data = []

# Serial Connection
connection = serial.Serial(portPath,baud)
max_length = sim_time/sample_time

plt.ion() # interactive mode

def makeFig():
    plt.ylim(15,45)
    plt.title('Temperature Sensor Data')
    plt.grid(True)
    plt.ylabel('Temperature C')
    plt.plot(data_log, 'ro-', label='Degrees C')

start_time = round(time.time())

def readdata():
    global start_time
    while True:
        line = connection.readline()
        print(line)
        line_data = re.findall('\d*\.\d*',str(line))
        line_data = filter(None,line_data)
        line_data = [float(x) for x in line_data]
        if len(line_data) > 0:
            print(line_data[0])
            if float(line_data[0]) > 0.0:
                drawnow(makeFig)
                plt.pause(.000001)
                data_log.append(line_data)
        if len(data_log) > max_length - 1:
            break
        print(line_data)

    # Storing data_log in data.csv
        with open('data.csv','w', newline='') as csvfile:
            print("Wrote in csv")
            for line in data_log:
                csvwrite = csv.writer(csvfile)
                csvwrite.writerow(line)

        end_time = round(time.time())

       # Find average, minimum and maximum temperature in every 35 seconds

        if end_time - start_time >= 35:
            start_time = end_time
            df = pd.read_csv('data.csv')
            arr = df.values
            print("Mean value:",arr.mean())
            print("Max Temp:",arr.max())
            print("Min Temp:",arr.min())

readdata()
