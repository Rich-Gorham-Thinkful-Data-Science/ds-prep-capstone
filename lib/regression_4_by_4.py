import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.stats import t
from scipy.stats import norm
import lib.least_squares as ls


def regression_4_by_4(x, y_0, y_1 = None, y_2 = None, y_3 = None, cols = 1, 
                      rows = 1, suptitle = None, subtitle_0 = None, 
                      subtitle_1 = None, subtitle_2 = None, subtitle_3 = None,
                      xlabels = None, ylabels = None, xmin = None, xmax = None,
                      xticks = None):

    plt.figure(figsize = (15, rows * 5))
    if isinstance(suptitle, str):
        plt.suptitle('Regression Analysis \n' + suptitle)
    else:
        plt.suptitle('Regression Analysis')

    plt.subplot(rows, cols, 1)
#Underscore and the start of label text will surpress the label on the plot
    plt.scatter(x, y_0, label = '_x') 
    plt.plot(x, ls.least_squares(x, y_0).get('upi'), 'r--', label = '_x')
    plt.plot(x, ls.least_squares(x, y_0).get('l'), 'b--', label = '_x')
    plt.plot(x, ls.least_squares(x, y_0).get('lpi'), 'r--', label = '_x')
    plt.fill_between(x, ls.least_squares(x, y_0).get('uci')['Data Year'],\
                     ls.least_squares(x, y_0).get('lci')['Data Year'],\
                     alpha = 0.25, color = '#99caff')
    plt.grid()
    
    if xmin or xmax != None:
        plt.xlim(xmin, xmax)
    else:
        None
    
    if xticks != None:  
        plt.xticks(xticks)
    else:
        None
        
    if isinstance(subtitle_0, str):
        plt.title(subtitle_0)
    else:
        plt.title('Observations')
        
    if isinstance(ylabels, str):
        plt.ylabel(ylabels)
    else:
        plt.ylabel('Obs.')
        
    if isinstance(xlabels, str):
        plt.xlabel(xlabels)
    else:
        plt.xlabel('Index')

#The emplty plots below are used to hold custom labels for the legend
    plt.plot([], [], ' ', label = 'Slope: '\
         + ls.least_squares(x, y_0).get('m').astype(str)) 
    plt.plot([], [], ' ', label = 'R-sq: '\
         + ls.least_squares(x, y_0).get('r_sq').astype(str))
    if ls.least_squares(x, y_0).get('p') < 0.0001:
        p_value = 'p value: <0.0001'
    else:
        p_value = 'p value: ' + ls.least_squares(x, y_0).get('p').astype(str)
    plt.plot([], [], ' ', label = p_value)
    plt.legend(loc = 2)

    plt.subplot(rows, cols, cols)
#Underscore and the start of label text will surpress the label on the plot
    plt.scatter(x, y_1, label = '_x')
    plt.plot(x, ls.least_squares(x, y_1).get('upi'), 'r--', label = '_x')
    plt.plot(x, ls.least_squares(x, y_1).get('l'), 'b--', label = '_x')
    plt.plot(x, ls.least_squares(x, y_1).get('lpi'), 'r--', label = '_x')
    plt.fill_between(x, ls.least_squares(x, y_1).get('uci')['Data Year'],\
                     ls.least_squares(x, y_1).get('lci')['Data Year'],\
                     alpha = 0.25, color = '#99caff')
    plt.grid()
    
    if xmin or xmax != None:
        plt.xlim(xmin, xmax)
    else:
        None
             
    if xticks != None:  
        plt.xticks(xticks)
    else:
        None
        
    if isinstance(subtitle_1, str):
        plt.title(subtitle_1)
    else:
        plt.title('Observations')
        
    if isinstance(ylabels, str):
        plt.ylabel(ylabels)
    else:
        plt.ylabel('Obs.')
        
    if isinstance(xlabels, str):
        plt.xlabel(xlabels)
    else:
        plt.xlabel('Index')

#The emplty plots below are used to hold custom labels for the legend
    plt.plot([], [], ' ', label = 'Slope: '\
         + ls.least_squares(x, y_1).get('m').astype(str)) 
    plt.plot([], [], ' ', label = 'R-sq: '\
         + ls.least_squares(x, y_1).get('r_sq').astype(str))
    if ls.least_squares(x, y_1).get('p') < 0.0001:
        p_value = 'p value: <0.0001'
    else:
        p_value = 'p value: ' + ls.least_squares(x, y_1).get('p').astype(str)
    plt.plot([], [], ' ', label = p_value)
    plt.legend(loc = 2)

    if rows == 2:
    
        plt.subplot(rows, cols, rows + 1)
#Underscore and the start of label text will surpress the label on the plot
        plt.scatter(x, y_2, label = '_x') 
        plt.plot(x, ls.least_squares(x, y_2).get('upi'), 'r--', label = '_x')
        plt.plot(x, ls.least_squares(x, y_2).get('l'), 'b--', label = '_x')
        plt.plot(x, ls.least_squares(x, y_2).get('lpi'), 'r--', label = '_x')
        plt.fill_between(x, ls.least_squares(x, y_2).get('uci')['Data Year'],\
                     ls.least_squares(x, y_2).get('lci')['Data Year'],\
                     alpha = 0.25, color = '#99caff')
        plt.grid()
    
        if xmin or xmax != None:
            plt.xlim(xmin, xmax)
        else:
            None
             
        if xticks != None:
            plt.xticks(xticks)
        else:
            None
        
        if isinstance(subtitle_2, str):
            plt.title(subtitle_2)
        else:
            plt.title('Observations')
        
        if isinstance(ylabels, str):
            plt.ylabel(ylabels)
        else:
            plt.ylabel('Obs.')
        
        if isinstance(xlabels, str):
            plt.xlabel(xlabels)
        else:
            plt.xlabel('Index')

#The emplty plots below are used to hold custom labels for the legend
        plt.plot([], [], ' ', label = 'Slope: '\
             + ls.least_squares(x, y_2).get('m').astype(str)) 
        plt.plot([], [], ' ', label = 'R-sq: '\
             + ls.least_squares(x, y_2).get('r_sq').astype(str))
        if ls.least_squares(x, y_2).get('p') < 0.0001:
            p_value = 'p value: <0.0001'
        else:
            p_value = 'p value: ' + ls.least_squares(x, y_2).get('p').astype(str)
        plt.plot([], [], ' ', label = p_value)
        plt.legend(loc = 2)

        plt.subplot(rows, cols, cols + rows)
#Underscore and the start of label text will surpress the label on the plot
        plt.scatter(x, y_3, label = '_x') 
        plt.plot(x, ls.least_squares(x, y_3).get('upi'), 'r--', label = '_x')
        plt.plot(x, ls.least_squares(x, y_3).get('l'), 'b--', label = '_x')
        plt.plot(x, ls.least_squares(x, y_3).get('lpi'), 'r--', label = '_x')
        plt.fill_between(x, ls.least_squares(x, y_3).get('uci')['Data Year'],\
                     ls.least_squares(x, y_3).get('lci')['Data Year'],\
                     alpha = 0.25, color = '#99caff')
        plt.grid()
    
        if xmin or xmax != None:
            plt.xlim(xmin, xmax)
        else:
            None
             
        if xticks != None:  
            plt.xticks(xticks)
        else:
            None
        
        if isinstance(subtitle_3, str):
            plt.title(subtitle_3)
        else:
            plt.title('Observations')
        
        if isinstance(ylabels, str):
            plt.ylabel(ylabels)
        else:
            plt.ylabel('Obs.')
        
        if isinstance(xlabels, str):
            plt.xlabel(xlabels)
        else:
            plt.xlabel('Index')

#The emplty plots below are used to hold custom labels for the legend
        plt.plot([], [], ' ', label = 'Slope: '\
             + ls.least_squares(x, y_3).get('m').astype(str)) 
        plt.plot([], [], ' ', label = 'R-sq: '\
             + ls.least_squares(x, y_3).get('r_sq').astype(str))
        if ls.least_squares(x, y_3).get('p') < 0.0001:
            p_value = 'p value: <0.0001'
        else:
            p_value = 'p value: ' + ls.least_squares(x, y_3).get('p').astype(str)
        plt.plot([], [], ' ', label = p_value)
        plt.legend(loc = 2)
    else:
        None

    plt.show()
