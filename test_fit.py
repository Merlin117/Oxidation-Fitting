import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

df = pd.read_csv('TestData.csv')

x1= df['orig'].to_numpy()
y1= df['Y0'].to_numpy()
x2 = df['storage'].to_numpy()
y2= df['Y1'].to_numpy()
print(y1,y2)

def func(x,a,b,c):
    if x< 2:
        return 0 #This can just be the initial point, so the fitting function returns the initial point 
    #and the initial point isn't factored into the logarithmic trend, or is the starting point
    else:
        return a*np.log(x-c)+b
    
def model(x,a,b,c):
    return[func(t,a,b,c) for t in x]
    
orig = curve_fit(model,x1,y1)
a1 = orig[0][0]
b1 = orig[0][1]
c1= orig[0][2]
#print(orig)
'''
fit1 = []
for i in x1:
    fit1.append(model(i,a1,b1,c1))
'''
store = curve_fit(model,x1,y1)
a2 = store[0][0]
b2 = store[0][1]
c2= store[0][2]
print(store)

'''    
fit2=[]
for i in x2:
    fit2.append(model(i,a2,b2,c2))
print(fit2)
'''
plt.plot(x1,y1,'o--')
plt.plot(x1,model(x1,a1,b1,c1))
plt.title('Origianl data')
plt.show()
plt.close()


plt.plot(x2,y2,'o-')
plt.plot(x2,model(x2,a2,b2,c2))
plt.title('Stored Data')
plt.show()
plt.close()

