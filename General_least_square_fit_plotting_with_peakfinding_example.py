
#This script performs general nonlinear least square fits.
#Usage:
#1) Import data by changing the file name and the columns to be used. The data file needs to be in the same folder as the skript
#for the script to be able to work with relative paths. I only give relative paths to allow you to use it with whatever operating
#system you might have. Absolute paths work as well so if you want to adjust your script to work systemwide on your OS just put
#it in a path where you can find and run it easily and change relative paths to absolute paths.
#2) Define your fit function with the fit parameters and use scipy.optimize
#You can fit about any function that you can imagine. Still there might be some trouble on functions defined over an integral
#such as the error function
#You are free to use this script, modify it and redistribute it at your will
#I, the author hereby give no guarantee and do not accept responsibility for any results that might be the outcome of your use of this script.
#If you detect some issues or errors please just tell me or suggest changes via a pull request.
####The example here delivers the position of peaks in a LEED spectrum and will in this form be of use mostly for
####people doing some spectroscopy of any kind.
####It shall illustrate how to define non-linear models in Python and then fit them to data using a least square fit
####The model does not necessarily have to be a Lorentzian fitted to an optical spectrum, it can have any form you like
####and yes, linear fits work as well but it is much easier to use numpy.polyfit for that


import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as S

################## import data ##################################
#insert the name of your data file here
energy, imax, itotal, ibackground = np.loadtxt('examplespectrum.dat',usecols=(0,2,3,4),unpack=True)
#put variables separated by commata, the variables will be lists including your data points
#data must be in collumns separated by a tab in a text file
#usecols indicates which collumns you are using eg. if you want to use the first three collumns, you give a tuple
#to the parameter indicating columns 1, 2, 3. Careful, enumeration in python always starts with zero
#python uses American notation, meaning commata are represented by points

###########I here use Lorentzian fits to a spectrum as an example#######################

#assign new values by substracting background noise
imax_neu = [imax[i] - ibackground[i] for i in range(len(imax))]
itotal_neu = np.array([itotal[i] - ibackground[i] for i in range(len(itotal))])
print(energy)


#######Define your model function here - can be linear, Gaussian, Lorentzian, whatever#####################
#######Important, for fitting scipy optimize needs the data as an array, therefore you don't define your function
#######for a single point or single tuple of points and then create the list with values, but instead the defined 
#######function by you ABSOLUTELY NEEDS TO TAKE A LIST of data points as input and return the model function applied
#######to the data points as an output !!!
#######Then the function needs take the fit parameters as input !!!
def lorentzian(xlist,s,t):
    lorentz = [np.float(1/np.pi)*np.float(s/(s**2+(x-t)**2)) for x in xlist]
    #t - center of the Lorentzian that we are looking for
    #s - FWHM
    #x energy data points for the fit
    return lorentz
#fit function with itotal_neu
#parameters a,b correspond to the optimized parameters s,t from the Lorentzian fit !
#I here restricted the fit to a subset of data points of energy and imax_neu but that's up to you

fitdata, covariance = S.curve_fit(lorentzian,energy[122:139],imax_neu[122:139])
print('Your fitparameter are', fitdata)
print('Your covariance is', covariance)
print('Your maximum is located at', fitdata[1], 'eV')

###############plot data, fit etc##########################

plt.figure(1)
plt.plot(energy,imax_neu)
plt.plot(energy[122:139],llorentzian(energy[122:139],fitdata[0],fitdata[1]))
plt.title('Maximal intensity vs. energy - I(V) curve')
plt.xlabel('Energy in eV')
plt.ylabel('Intensity')
plt.show()

############use for this special script, to determine the intervall in which the maxima lie so that you can
############optimally use the Lorentzian fit for your maxima

#Usage : You want to plot each peak individualy. Search in your plot the interval in which your peak is located and then
#####search corresponding values in the list
#e. g. a big peak between 250 and 300 eV
#look in your data set which values come close -> e.g. 251 eV and 296 eV
liste = copy.deepcopy(energy)
energy2 = list(liste)
firstposition = energy2.index(386) #put interval limits as seen in the list below here, the beginning of your interval
lastposition = energy2.index(437) #and the end of your interval -> you give the x-axis interval and get the corresponding 
#entries in the list which you need to restrict the fit to this subset of data points in the interval
print('Your beginning of the interval is at', firstposition)
print('Your end of the interval is at', lastposition)
