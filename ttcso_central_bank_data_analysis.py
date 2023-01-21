import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class trust_fin_cos:

    def __init__(self):
        pass
    
    
    def trust_mortgage_cos_charting(self):
    
    
        npat = np.array([22470	, 146629,	237008,	290949,	112556,	187749, 168769	, 195508,	44487,	72223	, 61680])
        
        fin_years = np.array([2010	,2011,	2012	, 2013 ,	2014	, 2015,	2016,	2017,	2018,	2019,	2020
                                ])
        fin_yr_segments = np.array ([0,0,0,0,0 ,0, 0,0,0,0,.2])
        plt.title("T&T - Net Profit of Mortgage & Finance Companies")
        # # plt.pie(npat, labels= fin_years , explode= fin_yr_segments, center=(40,30))
        plt.pie(npat, labels= fin_years , explode= fin_yr_segments)
        plt.legend(title='Financial Years' , bbox_to_anchor=(1.4, 1.0) , loc = 'upper right')
        plt.show()
        return 



demo_fin_rpt = trust_fin_cos()
demo_fin_rpt.trust_mortgage_cos_charting()