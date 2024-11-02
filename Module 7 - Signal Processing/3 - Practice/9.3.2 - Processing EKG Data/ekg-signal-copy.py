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
Step 2: Pass data through weighted differentiator
"""

## YOUR CODE HERE ##
differentiated_signal = np.convolve(signal, [1, -1], mode='same')


"""
Step 3: Square the results of the previous step
"""
 ## YOUR CODE HERE ##
squared_signal = differentiated_signal ** 2

"""
Step 4: Pass a moving filter over your data
"""

## YOUR CODE HERE
window_size = 30
moving_average_signal = np.convolve(squared_signal, np.ones(window_size)/window_size, mode='same')

# make a plot of the results. Can change the plot() parameter below to show different intermediate signals
plt.title('Process Signal for ' + database_name)
plt.plot(time, moving_average_signal)
plt.xlabel("Time")
plt.ylabel("Signal")
plt.show()