import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

class concentration:
    def __init__(self, conc, t, filename):
        self.conc = conc
        self.filename = filename
        self.t = t
    
    #equation 
    def f(self, C, t):
        """
        Equation to look at molecule synthesis and degradation at specified concentration 
        dx/dt = S(x) - d(x) * X
        
        Parameters
        ----------
        X: concentration 
        t: timepoint
        
        Returns
        -------
        Concentration at time point
        """ 
        S = 0.06
        d = 0.04
        derv = 0.06 - 0.04 * C  
        return derv
    
    #solve for days: 
    def solve(self, c):
        """solve ode
        
        Arguments:
            c {[type]} -- single concentration
        
        Returns:
            [X] -- results of odeint
        """
        X = odeint(self.f, c, self.t)
        return X
        
    def plotting(self):
        """
        
        iterates through list of concentrations and plots the decay
        """
        for x in self.conc:
            temp = self.solve(x)
        
            plt.ylim(1.25, 2.75)
            plt.plot(self.t, temp)
        plt.savefig("Output_{:.03f}.png".format(x))
        return