import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import t
from scipy.stats import norm
import lib.residuals as res

def p_from_ad(x, y, d):
    try:
        a_2 = stats.anderson(res.residuals(x, y)\
                   .get('stand_residuals'), dist = d)[0]
        
        a_2_prime = a_2 * (1 + 0.75 / len(x) + 2.25 / len(x)**2)
        d = 'norm'
        len(x) >= 8.0   
        a_2_prime <= 13
     
    except ValueError:
        print('Test distribution must be \'norm\'.')
    except ValueError:
        print('Sample size must be 8 or greater.')
    except ValueError:
        print('Anderson Darling Statistic is too large.')
        
    else:
        if 13 >= a_2_prime > 0.6:
            p = math.exp(1.2937 - 5.709 * a_2_prime + 0.0186 * a_2_prime**2)
        elif 0.6 >= a_2_prime > 0.34:
            p = math.exp(0.9177 - 4.279 * a_2_prime - 1.38 * a_2_prime**2)
        elif 0.34 >= a_2_prime > 0.2:
            p = 1 - math.exp(-8.318 - 42.796 * a_2_prime \
                - 59.938 * a_2_prime**2)
        else:
            p = 1 - math.exp(-13.436 - 101.14 * a_2_prime \
                - 223.73 * a_2_prime**2)
            
    return np.round(p, 4)
