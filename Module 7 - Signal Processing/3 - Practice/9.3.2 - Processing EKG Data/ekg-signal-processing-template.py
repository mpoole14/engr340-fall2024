import matplotlib.pyplot as plt
import numpy as np

"""
Step 0: Select which database you wish to use.
"""

# database name
database_name = 'mitdb_201'

# path to ekg folder
path_to_folder = "../../../data/ekg/"

# select a signal file to run
signal_filepath = path_to_folder + database_name + ".csv"

"""
Step #1: load data in matrix from CSV file; skip first two rows. Call the data signal.
"""


## YOUR CODE HERE ##
data = np.loadtxt(signal_filepath, delimiter=',', skiprows=2)
time = data[:, 0]
signal = data[:, 1]

"""
Step 2: (OPTIONAL) pass data through LOW PASS FILTER (fs=250Hz, fc=15, N=6). These may not be correctly in radians
"""

## YOUR CODE HERE ##
fs = 250
fc = 15
n = 6


"""
Step 3: Pass data through weighted differentiator
"""

## YOUR CODE HERE ##
differentiated_signal = np.convolve(signal, [1, -1], mode='same')


"""
Step 4: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
squared_signal = differentiated_signal ** 2

"""
Step 5: Pass a moving filter over your data
"""

## YOUR CODE HERE
# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Process Signal for ' + database_name)
plt.plot(squared_signal)
plt.show()