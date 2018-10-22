##This script can perform any polynominal least square fit and display the results. For general fits use the next cell
##Uncomment whatever you don't need
## Copyright 2018 by sycramore. The account redundanceredundance where this script was first found is my account to play with stuff.
## I'd put this under GPL licence if this works with the licences for juypter and python

import numpy as np
import matplotlib.pyplot as plt
import copy as copy

################## import data ##################################
#insert the name of your data file here
data1, data2, data3 = np.loadtxt('exampledata.txt',usecols=(0,1,2),unpack=True)
#put variables separated by commata, the variables will be lists including your data points
#data must be in collumns separated by a tab in a text file
#usecols indicates which collumns you are using eg. if you want to use the first three columns, you give a tuple
#to the parameter indicating columns 1, 2, 3. Careful, enumeration in python always starts with zero
#python uses American notation, meaning commata are represented by points

################## fit your data with a polynom ############################
fitparameter,covariance = np.polyfit(data1,data2,1,full=False,cov=True)
#indicate degree of polynominal at third place (1 equals a linear least sqare fit)
#indicate as parameter the data set with your arguments and second the data set with your values corresponding
#to the arguments
#The diagonal entries of the covariance matrix contain your errors from the fit for each parameter, e. g. covariance[0][0]
#contains the error for the coefficient of highest order, covariance[1][1] the error for the coefficient of second highest
#order etc
print('The fitparameters are', fitparameter)
print('Your covariance matrix of the least square fit is', covariance)

#fitparameter includes the coefficients of your polynominal starting with the highest order

#calculate data points of your fitfunction
#this example works for linear fits. In case you want to plot polynominals of higher degree just expand the equation in the
#fit list accordingly eg fitparameter[0]*data**2 + fitparameter[1] * data + fitparameter[3] for data in data 1 etc.
fit = [fitparameter[0]*data + fitparameter[1] for data in data1]

#plot your data as well as your fit
plt.plot(data1,data2,'ro') #for points drawn in a different colour use 'bo' for blue dots etc. Consult the pyplot documentation for this
plt.plot(data1,fit)
#plt.errorbar(xdata,ydata,xerr=errordataofx,yerr=errordataofy) #to plot data with errorbars, if you only want to use errorbars on x or y, just leave out yerr or xerr
#plt.xlim(20,21) #uncomment to set axis intervals and restrict axis to a certain interval
#plt.ylim(300,400) #syntax is as follows : plt.xlim(minimum,maximum), use plt.xlim for x-axis and plt.ylim for y-axis
plt.xlabel('data1')
plt.ylabel('data2')
plt.show()
#save the plot using right click on the plot and then use "save as" function, default for saving is png format
