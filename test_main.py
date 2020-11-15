import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_rvalues(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        nr = int( len(microstate1)/2+1 )
        self.assertTrue( (len(microstate1)/2+1)==len(this_x), "You have calculated the correlation function for the wrong number of points." )
        for i in range(nr) : self.assertTrue( np.abs(this_x[i]-i)<1e-8, "The r values at which you have computed the correlation function are wrong" )
        
    def test_correlation(self) :
      fighand=plt.gca()
      figdat = fighand.get_lines()[0].get_xydata()
      this_x, this_y = zip(*figdat)
      average = sum(microstate1) / len(microstate1) + sum(microstate2) / len(microstate2) + sum(microstate3) / len(microstate3)
      nr = int( len(microstate1)/2+1 )
      for i in range(nr) : 
          var, cor = 0, 0
          for j in range(len(microstate1)) :
             var = var + ( microstate1[j] - average )*( microstate1[j] - average )
             var = var + ( microstate2[j] - average )*( microstate2[j] - average )
             var = var + ( microstate3[j] - average )*( microstate3[j] - average )
             cor = cor + ( microstate1[j] - average )*( microstate1[(j+i)%len(microstate1)] - average )
             cor = cor + ( microstate2[j] - average )*( microstate2[(j+i)%len(microstate2)] - average )
             cor = cor + ( microstate3[j] - average )*( microstate3[(j+i)%len(microstate3)] - average )
          self.assertTrue( np.abs(this_y[i]-cor/var )<1e-8, "The values that you have computed for the correlation function are wrong." )
