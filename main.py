import matplotlib.pyplot as plt

# Here are the three microstates for which you are to 
# compute the average correlation function
microstate1 = [1,-1,1,1,-1,1,1,1,-1,-1]
microstate2 = [-1,1,1,1,-1,-1,1,1,1,-1]
microstate3 = [-1,1,1,1,-1,1,1,-1,1,-1]

rvalues, correlation = [0,1,2,3,4,5], 6*[0]
average = ( sum(microstate1)/len(microstate1) + sum(microstate2) / len(microstate2) + sum(microstate3) / len(microstate3) ) / 3
# Your code to calculate the average correlation function 
# for the three microstates above goes here.
for i in range(6) :
  var, cov = 0, 0 
  for j in range(len(microstate1)) : 
    var = var + (microstate1[j] - average)*(microstate1[j] - average)
    var = var + (microstate2[j] - average)*(microstate2[j] - average)
    var = var + (microstate3[j] - average)*(microstate3[j] - average)
    cov = cov + (microstate1[j] - average)*(microstate1[(j+i)%len(microstate1)] - average)
    cov = cov + (microstate2[j] - average)*(microstate2[(j+i)%len(microstate1)] - average)
    cov = cov + (microstate3[j] - average)*(microstate3[(j+i)%len(microstate1)] - average)
  correlation[i] = cov / var 


# This plots the final correlation function you obtain
plt.plot( rvalues, correlation, 'ko')
plt.plot( rvalues, correlation, 'k-')
plt.savefig("correlation_function.png")
