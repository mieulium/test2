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
    def f(self, C, t, S):
        """
        must start with concentration and time first
        Equation to look at molecule synthesis and degradation at specified concentration 
        dx/dt = S(x) - d(x) * C
        
        Parameters
        ----------
        C: concentration 
        t: timepoint
        S: constant
        
        Returns
        -------
        Concentration at time point
        """
        d = 0.04
        derv = S - d * C
        return derv

    #obj
    def obj(self, S):
        temp = odeint(self.f, self.conc[0], self.t, args=(S,))
        rmse = np.sqrt(np.mean((np.array(self.conc) - temp)**2))
        return rmse

    def optimisation(self):
        print(minimize(self.obj, self.initial, method = "BFGS"))

optimize([2.1, 2.06, 2.05, 2.04, 2.03, 2.01, 2], [0,10,15,20,30,60,90], 0.01).optimisation()
