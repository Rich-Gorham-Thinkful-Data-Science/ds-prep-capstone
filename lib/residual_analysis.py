import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import t
from scipy.stats import norm
import lib.residuals as res
import lib.least_squares as ls
import lib.p_from_ad as pad

def residual_analysis(x, y, d, response = None):
    plt.figure(figsize = (15, 10))
    if isinstance(response, str):
        plt.suptitle('Residual Analysis \nResponse is ' + response)
    else:
        plt.suptitle('Residual Analysis')

    plt.subplot(221)
    plt.hist(res.residuals(x,y).get('stand_residuals'), \
         density = True, label = 'Residuals')
    x_axis = np.arange(-3.0, 3, 0.00001)
    plt.plot(x_axis, norm.pdf(x_axis,0,1), 'r--', label = 'Normal')
    plt.ylabel('Density')
    plt.xlabel('Standard Normal')
    plt.title('Histogram of Residuals')
    plt.legend(loc = 2)
    plt.grid()

    plt.subplot(222)
    plt.subplots_adjust(hspace = 0.25)
    osm, osr  = stats.probplot(res.residuals(x,y).get('stand_residuals'))
    x1 = osm[0]
    y1 = osm[1]
    stats.probplot(res.residuals(x,y).get('stand_residuals'), plot = plt)
    plt.fill_between(x1, ls.least_squares(x1, y1).get('uci')[0],\
                 ls.least_squares(x1, y1).get('lci')[0],\
                 alpha = 0.25, color = '#99caff')
    plt.plot([],[], 'r-', label = 'Normal Fit')
    plt.plot([],[], 'bo', label = 'Residual Fit')
    plt.plot([],[], ' ', label = 'R-Sq: ' \
         + ls.least_squares(x1, y1).get('r_sq').astype(str))
    plt.plot([],[], ' ', label = 'AD p-value: ' \
         + pad.p_from_ad(x, y, d).astype(str))
    plt.plot([],[], ' ', label = 'KS p-value: ' \
         + np.round(stats.kstest(res.residuals(x, y)\
         .get('stand_residuals'), d)[1], 4).astype(str))
    plt.ylabel('Observed Residuals')
    plt.xlabel('Theoretical Residuals')
    plt.title('Q-Q Plot')
    plt.legend(loc = 2)
    plt.grid()

    plt.subplot(223)
    plt.plot(x, res.residuals(x, y).get('stand_residuals'), 'bo-')
    plt.axhline(y = 0, color = 'k', dashes = (1, 1))
    plt.xlim((1995, 2016))
    plt.xticks([1996, 2001, 2006, 2011, 2015])
    plt.ylabel('Observed Residuals')
    plt.xlabel('Order')
    plt.title('Residual v Order')
    plt.grid()

    plt.subplot(224)
    plt.subplots_adjust(hspace = 0.25)
    plt.scatter(res.residuals(x, y).get('l'), \
        res.residuals(x, y).get('stand_residuals'))
    plt.axhline(y = 0, color = 'k', dashes = (1, 1))
    plt.ylabel('Observed Residuals')
    plt.xlabel('Fitted Data')
    plt.title('Residual v Fit')
    plt.grid()

    plt.show()
