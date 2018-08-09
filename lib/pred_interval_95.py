import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import t
from scipy.stats import norm


def pred_interval_95(x, y, new_x):
    #from SciPy Stats
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y) 
    
    #Calculate R-Squared (coefficient of determination) from r (corr. coef.)
    y_hat_i = slope * x + intercept #The fitted line
    s_y = np.sqrt(np.sum((y - y_hat_i)**2) / (len(y) - 2)) #Std. dev. of y
    
    #t-crit. from SciPy Stats
    t_df = t.isf(0.025, len(x) - 2, loc = 0, scale = 1) 
    
    #Predicted value and 95% prediction interval of data
    y_pred = y_hat_i = slope * new_x + intercept
    y_pred_interval = t_df * s_y * np.sqrt(1 + (1 / len(x)) \
        + (new_x - x.mean())**2 / ((len(x) - 1) * (x.var())))
    
    return(np.round(y_pred, 2), np.round(y_pred_interval, 2))
