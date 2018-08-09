import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import t
from scipy.stats import norm

def least_squares(x, y):
    #from SciPy Stats
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y) 
    
    #Calculate R-Squared (coefficient of determination) from r (corr. coef.)
    r_sq = r_value**2 
    y_hat_i = slope * x + intercept #The fitted line
    s_y = np.sqrt(np.sum((y - y_hat_i)**2) / (len(y) - 2)) #Std. dev. of y
    
    #t-crit. from SciPy Stats
    t_df = t.isf(0.025, len(x) - 2, loc = 0, scale = 1) 
    
    #Prediction intervals of data
    y_pred_upper = y_hat_i \
        + (t_df * s_y * np.sqrt(1 + (1 / len(x))\
        + (x - x.mean())**2 / ((len(x) - 1) * x.var())))
    
    y_pred_lower = y_hat_i \
        - (t_df * s_y * np.sqrt(1 + (1 / len(x)) \
        + (x - x.mean())**2 / ((len(x) - 1) * x.var())))
    
    #Confidencce inverals for the line
    y_confidence_upper = y_hat_i \
        + (t_df * s_y * np.sqrt((1 / len(x)) \
        + (x - x.mean())**2 / ((len(x) - 1) * x.var())))
    
    y_confidence_lower = y_hat_i \
        - (t_df * s_y * np.sqrt((1 / len(x)) \
        + (x - x.mean())**2 / ((len(x) - 1) * (x.var()))))
    
    #Return series as data frames for charting
    l = pd.DataFrame(y_hat_i)
    upi = pd.DataFrame(y_pred_upper)
    lpi = pd.DataFrame(y_pred_lower)
    uci = pd.DataFrame(y_confidence_upper)                                                      
    lci = pd.DataFrame(y_confidence_lower)       

    return {'m':np.round(slope,2), 'b':np.round(intercept,2),\
            'r_sq':np.round(r_sq,2), 'p':np.round(p_value,4),\
            'l':l, 'upi':upi, 'lpi':lpi, 'uci':uci, 'lci':lci}
