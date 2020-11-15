import matplotlib.pyplot as plt

# Here are the three microstates for which you are to 
# compute the average correlation function
microstate1 = [1,-1,1,1,-1,1,1,1,-1,-1]
microstate2 = [-1,1,1,1,-1,-1,1,1,1,-1]
microstate3 = [-1,1,1,1,-1,1,1,-1,1,-1]

rvalues, correlation = [0,1,2,3,4,5], 6*[0]
# Your code to calculate the average correlation function 
# for the three microstates above goes here.



# This plots the final correlation function you obtain
plt.plot( rvalues, correlation, 'ko')
plt.plot( rvalues, correlation, 'k-')
plt.savefig("correlation_function.png")
