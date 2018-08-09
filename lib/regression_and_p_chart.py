import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import t
from scipy.stats import norm
import lib.p_chart as pc
import lib.least_squares as ls

def regression_and_p_chart(x, y_0, y_1, y_2, suptitle = None, 
                      subtitle_0 = None, subtitle_1 = None, subtitle_2 = None, 
                      subtitle_3 = None, subtitle_4 = None, subtitle_5 = None,
                      xlabels_r = None, xlabels_p = None, ylabels_r = None, 
                      ylabels_p = None, xmin = None, xmax = None, 
                      xticks = None):
    
    p_0 = y_0 / (y_0 + y_1 + y_2)
    p_1 = y_1 / (y_0 + y_1 + y_2)
    p_2 = y_2 / (y_0 + y_1 + y_2)
    
    #Plot charts
    plt.figure(figsize = (15, 12))
    plt.subplots_adjust(hspace = 0.5)
    if isinstance(suptitle, str):
        plt.suptitle('Regression and p Charts'
                     '\nfor Suceptibility / Resistance\n' + suptitle)
    else:
        plt.suptitle('Regression and p Charts'
                     '\nfor Suceptibility / Resistance\n')

    plt.subplot(321)
#Underscore and the start of label text will surpress the label on the plot
    plt.scatter(x, y_0, label =  '_x') 
    plt.plot(x, ls.least_squares(x, y_0).get('upi'), 'r--', label = '_x')
    plt.plot(x, ls.least_squares(x, y_0).get('l'), 'b--', label = '_x')
    plt.plot(x, ls.least_squares(x, y_0).get('lpi'), 'r--', label = '_x')
    plt.fill_between(x, ls.least_squares(x, y_0).get('uci')['Data Year'],\
                 ls.least_squares(x, y_0).get('lci')['Data Year'],\
                 alpha = 0.25, color = '#99caff')
    plt.grid()
    
    if xmin and xmax != None:
        plt.xlim(xmin, xmax)
    else:
        None
    
    if xticks != None:  
        plt.xticks(xticks)
    else:
        None
      
    if isinstance(subtitle_0, str):
        plt.title(subtitle_0, y = 1.125)
    else:
        plt.title('Observations', y = 1.125)
        
    if isinstance(ylabels_r, str):
        plt.ylabel(ylabels_r)
    else:
        plt.ylabel('Obs.')
        
    if isinstance(xlabels_r, str):
        plt.xlabel(xlabels_r)
    else:
        plt.xlabel('Index')
   
#The emplty plots below are used to hold custom labels for the legend
    plt.plot([], [], ' ', label = 'Slope: ' \
         + ls.least_squares(x, y_0).get('m').astype(str)) 
    plt.plot([], [], ' ', label='R-sq: ' \
         + ls.least_squares(x, y_0).get('r_sq').astype(str))
    if ls.least_squares(x, y_0).get('p') < 0.0001:
        p_value = 'p value: <0.0001'
    else:
        p_value = 'p value: ' + ls.least_squares(x, y_0).get('p').astype(str)
    plt.plot([], [], ' ', label = p_value)
    plt.legend(bbox_to_anchor = (0, 1.05, 1, 0.2), \
           loc = 2, ncol = 3, mode = "expand", borderaxespad = 2)

    plt.subplot(322)
    plt.plot(x, p_0,'bo--', label = '_x')
    plt.step(x, pc.p_chart(y_0, p_0).get('ucl'), 'r--', \
             label = 'Control Limits', where = 'mid')
    plt.plot(x, pc.p_chart(y_0, p_0).get('cl'), 'g--', label = 'Center Line')
    plt.step(x, pc.p_chart(y_0, p_0).get('lcl'), \
            'r--', label = '_x', where = 'mid')
    plt.grid()
    
    if xmin and xmax != None:
        plt.xlim(xmin, xmax)
    else:
        None
    
    if xticks != None:  
        plt.xticks(xticks)
    else:
        None
    
    if isinstance(subtitle_1, str):
        plt.title(subtitle_1, y = 1.125)
    else:
        plt.title('Proportions', y = 1.125)
        
    if isinstance(ylabels_p, str):
        plt.ylabel(ylabels_p)
    else:
        plt.ylabel('proportion')
        
    if isinstance(xlabels_p, str):
        plt.xlabel(xlabels_p)
    else:
        plt.xlabel('Index')
    
    plt.plot([], [], ' ', label = 'Mean: ' \
         + pc.p_chart(y_0,p_0).get('p_bar').astype(str))
    plt.legend(bbox_to_anchor = (0, 1.05, 1, 0.2), \
           loc = 2, ncol = 3, mode = "expand", borderaxespad = 2)

    plt.subplot(323)
    plt.scatter(x, y_1, label = '_x')
    plt.plot(x, ls.least_squares(x, y_1).get('upi'), 'r--', label = '_x')
    plt.plot(x, ls.least_squares(x, y_1).get('l'), 'b--', label = '_x')
    plt.plot(x, ls.least_squares(x, y_1).get('lpi'), 'r--', label = '_x')
    plt.fill_between(x, ls.least_squares(x, y_1).get('uci')['Data Year'],\
                 ls.least_squares(x, y_1).get('lci')['Data Year'],\
                 alpha = 0.25, color = '#99caff')
    plt.grid()
    
    if xmin and xmax != None:
        plt.xlim(xmin, xmax)
    else:
        None
    
    if xticks != None:  
        plt.xticks(xticks)
    else:
        None

    if isinstance(subtitle_2, str):
        plt.title(subtitle_2, y = 1.125)
    else:
        plt.title('Observations', y = 1.125)
        
    if isinstance(ylabels_r, str):
        plt.ylabel(ylabels_r)
    else:
        plt.ylabel('Obs.')
        
    if isinstance(xlabels_r, str):
        plt.xlabel(xlabels_r)
    else:
        plt.xlabel('Index')
    
#The emplty plots below are used to hold custom labels for the legend
    plt.plot([], [], ' ', label = 'Slope: ' \
         + ls.least_squares(x, y_1).get('m').astype(str)) 
    plt.plot([], [], ' ', label = 'R-sq: ' \
         + ls.least_squares(x, y_1).get('r_sq').astype(str))
    if ls.least_squares(x, y_0).get('p') < 0.0001:
        p_value = 'p value: <0.0001'
    else:
        p_value = 'p value: ' + ls.least_squares(x, y_1).get('p').astype(str)
    plt.plot([], [], ' ', label = p_value)
    plt.legend(bbox_to_anchor = (0, 1.05, 1, 0.2),
           loc = 2, ncol = 3, mode = "expand", borderaxespad = 2)

    plt.subplot(324)
    plt.plot(x,p_1,'bo--',label='_x')
    plt.step(x, pc.p_chart(y_1, p_1).get('ucl'), 'r--', \
         label = 'Control Limits', where = 'mid')
    plt.plot(x, pc.p_chart(y_1, p_1).get('cl'), 'g--', label = 'Center Line')
    plt.step(x, pc.p_chart(y_1, p_1).get('lcl'), \
            'r--', label = '_x', where = 'mid')
    plt.grid()
    
    if xmin and xmax != None:
        plt.xlim(xmin, xmax)
    else:
        None
    
    if xticks != None:  
        plt.xticks(xticks)
    else:
        None

    if isinstance(subtitle_3, str):
        plt.title(subtitle_3, y = 1.125)
    else:
        plt.title('Proportions', y = 1.125)
        
    if isinstance(ylabels_p, str):
        plt.ylabel(ylabels_p)
    else:
        plt.ylabel('proportion')
        
    if isinstance(xlabels_p, str):
        plt.xlabel(xlabels_p)
    else:
        plt.xlabel('Index')

    plt.plot([], [],' ', label = 'Mean: ' \
         + pc.p_chart(y_1, p_1).get('p_bar').astype(str))
    plt.legend(bbox_to_anchor = (0, 1.05, 1, 0.2), \
           loc = 2, ncol = 3, mode = "expand", borderaxespad = 2)

    plt.subplot(325)
    plt.scatter(x, y_2, label = '_x') 
    plt.plot(x, ls.least_squares(x, y_2).get('upi'), 'r--', label = '_x')
    plt.plot(x, ls.least_squares(x, y_2).get('l'), 'b--', label = '_x')
    plt.plot(x, ls.least_squares(x, y_2).get('lpi'), 'r--', label = '_x')
    plt.fill_between(x, ls.least_squares(x, y_2).get('uci')['Data Year'],\
                 ls.least_squares(x, y_2).get('lci')['Data Year'],\
                 alpha = 0.25, color = '#99caff')
    plt.grid()
    
    if xmin and xmax != None:
        plt.xlim(xmin, xmax)
    else:
        None
    
    if xticks != None:  
        plt.xticks(xticks)
    else:
        None

    if isinstance(subtitle_4, str):
        plt.title(subtitle_4, y = 1.125)
    else:
        plt.title('Observations', y = 1.125)
        
    if isinstance(ylabels_r, str):
        plt.ylabel(ylabels_r)
    else:
        plt.ylabel('Obs.')
        
    if isinstance(xlabels_r, str):
        plt.xlabel(xlabels_r)
    else:
        plt.xlabel('Index')
    
#The emplty plots below are used to hold custom labels for the legend
    plt.plot([], [],' ', label = 'Slope: ' \
         + ls.least_squares(x, y_2).get('m').astype(str)) 
    plt.plot([], [],' ', label = 'R-sq: ' \
         + ls.least_squares(x, y_2).get('r_sq').astype(str))
    if ls.least_squares(x, y_0).get('p') < 0.0001:
        p_value = 'p value: <0.0001'
    else:
        p_value = 'p value: ' + ls.least_squares(x, y_2).get('p').astype(str)
    plt.plot([], [], ' ', label = p_value)
    plt.legend(bbox_to_anchor = (0, 1.05, 1, 0.2), \
           loc = 2, ncol = 3, mode = "expand", borderaxespad = 2)

    plt.subplot(326)
    plt.plot(x, p_2,'bo--', label = '_x')
    plt.step(x, pc.p_chart(y_2, p_2).get('ucl'), 'r--', \
         label = 'Control Limits', where = 'mid')
    plt.plot(x, pc.p_chart(y_2, p_2).get('cl'), 'g--', label = 'Center Line')
    plt.step(x, pc.p_chart(y_2, p_2).get('lcl'), \
            'r--',label = '_x', where = 'mid')
    plt.grid()
    
    if xmin and xmax != None:
        plt.xlim(xmin, xmax)
    else:
        None
    
    if xticks != None:  
        plt.xticks(xticks)
    else:
        None

    if isinstance(subtitle_5, str):
        plt.title(subtitle_5, y = 1.125)
    else:
        plt.title('Proportions', y = 1.125)
        
    if isinstance(ylabels_p, str):
        plt.ylabel(ylabels_p)
    else:
        plt.ylabel('proportion')
        
    if isinstance(xlabels_p, str):
        plt.xlabel(xlabels_p)
    else:
        plt.xlabel('Index')
    
    plt.plot([], [],' ', label = 'Mean: ' \
         + pc.p_chart(y_2, p_2).get('p_bar').astype(str))
    plt.legend(bbox_to_anchor = (0, 1.05, 1, 0.2), \
           loc = 2, ncol = 3, mode = "expand", borderaxespad = 2)

    plt.show()
