import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import t
from scipy.stats import norm

def p_chart(n, p):
    p_bar = np.mean(p) #Mean proportion
    stdev = np.sqrt(p_bar * (1 - p_bar) / n) #Std. dev. for a binomial dist.
    
#Control limits (+/- 3 std dev. from the center line) and center line
    #Upper control limit is bounded by 1.0
    upper = np.where((p_bar + (3 * stdev) < 1.0), p_bar + (3 * stdev), 1.0)
    
    center = [p_bar] * len(p) #Convert p_bar into single value array
    
    #Lower control limit is bounded by 0.0
    lower = np.where((p_bar - (3 * stdev) > 0.0) ,p_bar - (3 * stdev), 0.0) 
    
    #Return series as data frames for charting
    ucl = pd.DataFrame(upper)
    cl = pd.DataFrame(center)
    lcl = pd.DataFrame(lower)
    
    return {'ucl':ucl, 'cl':cl, 'lcl':lcl, 'p_bar':np.round(p_bar, 2)}
