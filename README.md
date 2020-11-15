# The average correlation function

We are now going to work towards calculating the ensemble average of the correlation function.   Before we get on to that, however, we are, in this exercise, going to have a brief digression in order to understand one particular aspect of associated with the calculation of correlation functions. 

With this in mind lets look at the expression for the correlation function one further time:

![](https://render.githubusercontent.com/render/math?math=\delta(r)=\frac{\frac{1}{N}\sum_{i=1}^N(s_i-\langle\s\rangle)(s_{i%2Br}-\langle\s\rangle)}{\frac{1}{N}\sum_{i=1}^N(s_i-\langle\s\rangle)^2})

The important thing to recognise here is that the ![](https://render.githubusercontent.com/render/math?math=\langle\s\rangle) that appears in this expression is the __ensemble average__ for the spin.  In other words, __![](https://render.githubusercontent.com/render/math?math=\langle\s\rangle) is not the average instantaneous spin for the microstate that we are in__.  The fact that this is not the instantaneous spin makes complete sense in terms of what we have learned as statistical mechanics, tells us that there is nothing special about any instantaneous configuration.  The only thing that matters is the ensemble of configurations.

In this exercise, I would thus like to see if you have understood this idea.  With this in mind, I have provided you with three different microstates for a system with 10 spins.  I would like you to write a program to calculate the average over these three microstates for the correlation function.  To be clear, __I do not want you to compute the ensemble average yet__.  I just want you to compute a simple, unweighted average i.e.

![](https://render.githubusercontent.com/render/math?math=\langle\X\rangle=\frac{1}{N}\sum_{i=1}^NX_i)

Notice that like in the previous exercise the final result from your program should be a graph showing the degree of correlation as a function of the separation, r, between the spins.  With this in mind, I have created two lists for you called `rvalues` and `correlation`.  `rvalues` contain the various values of r at which the correlation should be computed.  You must, meanwhile, write the code to calculate the elements of `correlation`, which will be the values that the correlation function takes for the various values of r.
 
