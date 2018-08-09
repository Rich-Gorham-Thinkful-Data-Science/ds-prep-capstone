import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import t
from scipy.stats import norm

def residuals(x, y):
    #From SciPy Stats
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    
    y_hat_i = slope * x + intercept #The fitted line
    r_y = y - y_hat_i #Raw residuals
    sr_y = (r_y - r_y.mean()) / r_y.std() #Standardized residuals
    
    #Return series as data frames for charting
    r = pd.DataFrame(r_y)
    sr = pd.DataFrame(sr_y)
    l = pd.DataFrame(y_hat_i)
    return {'residuals':r_y, 'stand_residuals':sr_y, 'l':l}
