import matplotlib.pyplot as plt
import numpy as np


# import the CSV file using numpy
path = '../../../data/ekg/mitdb_201.csv'

# load data in matrix from CSV file; skip first two rows

### Your code here ###
data = np.loadtxt(path, delimiter=',', skiprows=2)

# save each vector as own variable

### Your code here ###
time = data[:, 0]      
signal = data[:, 1]

# Plot the EKG signal over time using Matplotlib
plt.figure(figsize=(10, 5))
plt.plot(time, signal, label='EKG Signal')
plt.xlabel('Time (s)')
plt.ylabel('Signal Amplitude')
plt.title('EKG Signal over Time')
plt.legend()
plt.grid(True)
plt.show()