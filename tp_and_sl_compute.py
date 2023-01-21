## Software Engineer: Roger De Four
## Date: 2023-01-20
## Description:  a FOREX related function the I want to use to assist me in computing 
##              a Stop Loss (sl) & Target Profit (tp) for the currenc y pair that I am trading

import pandas as pd
import math as m
import statistics as stat
import numpy as np



def fx_trade_limits (order_type , curr ,  fx_rate , sl):

    '''
        Date: 2023-01-20 08:59 am
        
        Description: this function takes as inputs: 
            * the FX rate of the pair that I am intending to trade , 
            * the stop loss(sl) , 
        then computes the target profit (tp) in a set ratio of 1:3 , and prints out the stats , 
        so I just need to plug them into the FX order in MT4(or relevant trading platform).
    
    '''
    # Authorised list of currencencies to trade in.
    
    permitted_currencies  = set(['AUDUSD' , 'EURUSD' , 'USDJPY' , 
                                        'USDCAD' ,'AUDUSD' ,'EURGBP',
                                        'EURAUD', 'EURCHF', 'EURJPY',
                                        'GBPCHF', 'CADJPY', 'GBPJPY',
                                        'AUDCHF', 'NZDUSD', 'GBPUSD'
                                                                        ])

    if curr in permitted_currencies:
    
        fx_rate = round(fx_rate,4)
            
        if len(str(sl)) >= 1 and  len(str(sl)) <=3:
            sl = sl/10000
        else:
            print("please enter no. of digits less than 4")
        stop_loss_pips = sl
        
        print(stop_loss_pips)
        
        target_profit_pips = round((3 * sl ),4)  # profit ratio
        
      
        
       
        
        if fx_rate <= 0 or fx_rate >= 200:  # checks in rate enter is acceptable ; inclusive of the Japenese Yen
            print("Please enter a valid exchange rate\n")
        else:
            print(fx_rate)
       
        if order_type == 'buy':
            target_profit =  fx_rate + target_profit_pips
            stop_loss =  fx_rate - stop_loss_pips
            
            str_tp = 'The target profit for FX rate {0} , is {1}'.format(fx_rate , target_profit)
            print (str_tp)
            
            str_sl = 'The stop loss for FX rate {0} , is {1}'.format(fx_rate , stop_loss)
            print(str_sl)
        elif order_type == 'sell':
            
            target_profit =  fx_rate - target_profit_pips
            stop_loss =  fx_rate + stop_loss_pips
            
            str_tp = 'The target profit for FX rate {0} is:  {1}'.format(fx_rate , target_profit)
            print (str_tp)
            
            str_sl = 'The stop loss for FX rate {0} is:  {1}'.format(fx_rate , stop_loss)
            print(str_sl)
    else:
        print("Currency pair NOT in approved listing")
        
    return
    
fx_trade_limits('sell' ,'AUDUSD' ,  0.875964 , 135)

print(fx_trade_limits.__doc__)