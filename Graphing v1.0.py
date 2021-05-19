# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
#This imports the libraries that will be used

#Now to import the data that I will be fitting.
#df = pd.read_csv('FILENAME.CSV')
df = pd.read_csv('LN2 3343 1.csv')

# This will put the data file  data into separate numpy arrays
xdata = df['Time (hrs)'].to_numpy()
ydata = df['Thickness'].to_numpy()
air = df['Air'].to_numpy()
adjust = df['adjust'].to_numpy()
#You can add more data arrays based on the number of collummns in the csv file.  

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉") #For sumbsript
SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
ox = "Al2O3".translate(SUB) #The command to change from regular to sub/super script

#time to define the model to be used to fit the data. 
def log(xdata,a,b):
    return a*np.log(xdata)+b

consts = curve_fit(log,xdata,ydata)
a_fit = consts[0][0]
b_fit = consts[0][1]

print('A = ',a_fit,', B = ',b_fit)

fit = []  #This appends the fitted y data to the x values.  
for i in xdata:
    fit.append(log(i,a_fit,b_fit))


third = curve_fit(log,adjust,ydata)  #The constants for the adjusted data set
q_fit = third[0][0]
w_fit = third[0][1]
print('Q = ' ,q_fit,', W = ',w_fit)

fit2 =[] #The fitted data for the adjusted time values
for i in adjust:
    fit2.append(log(i,q_fit,w_fit))


#Plot the data

plt.title('No Adjustment to time in storage')
plt.semilogx(xdata,ydata,'o--', label = 'Original')
plt.semilogx(xdata,fit ,label = "Log Fit")
plt.legend()
plt.xlabel("Time since depostion (hrs)")
plt.ylabel("Apparent " +ox +" thickness (nm)")
plt.grid(which = 'major', axis = 'x')
plt.show()
plt.close()


plt.title('Adjustment: storage / 500')
plt.semilogx(adjust,ydata,'o-', label = "Adjusted")
plt.semilogx(adjust,fit2,label = 'Logarithmic Fit')
plt.legend()
plt.xlabel("Adjusted time since depostion (hrs)")
plt.ylabel("Apparent " +ox +" thickness (nm)")
plt.grid(which = 'major', axis = 'x')
plt.show()
plt.close()


