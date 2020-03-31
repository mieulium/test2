import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import minimize

class optimize:
    def __init__(self, conc, t, initial):
        self.conc = conc
        self.t = t
        self.initial = initial
    
    #equation 
    def f(self, S, C, t):
        """
        Equation to look at molecule synthesis and degradation at specified concentration 
        dx/dt = S(x) - d(x) * C
        
        Parameters
        ----------
        C: concentration 
        t: timepoint
        
        Returns
        -------
        Concentration at time point
        """
        d = 0.04
        derv = 0.06 - S * C
        return derv

    #obj
    def obj(self, S):
        temp = odeint(self.f, self.conc[0], self.t, args=(S,))
        print(temp)
        print(self.conc)
        rmse = np.sqrt(np.mean((np.array(self.conc) - temp)**2))
        return rmse

    def optimisation(self):
        print(minimize(self.obj, self.initial, method = "BFGS"))

