from array import array
import pandas as pd
import numpy as np
import psycopg2 as pg2
from matplotlib import pyplot as plt


class Hostinger_Apps:

    '''
    Date: 2022-12-25
    Developer: Roger De Four
    Description: This class was developed due to problem that I encountered on the Titan Email app - receipts
                of spam email from apparently russian origin

    '''

    def __init__(self):
    
        pass
     # int_x , int_end the lower and upper range of the dynamic integers, used to generate the email address, that 
     # needs to be moved to spam/trash folder
     
     
    def alex_dud_email(int_x  , int_end = 200):
    
        '''
            date: 2022-12-25
            description: developed to generate emails with a dynamic integer variable
                        which , in theory could go on indefinitely
        '''

        txt1 = 'info@s'
        txt2 = range(int_x , int_end)
        
        email_index_num  = []
        
        
        # create the dynamic number that appear withihn the spam email I am 
        # receiving in my business email: 'rogerdefour@radfinancialsystems.com'
        
        for str_x in txt2:
            email_index_num.append(str(str_x))
            
        
        
        str_output = '.alexdf.ru , '.join(email_index_num)
        
        
        # # # the split() function can be used to alter a string value to a list
        
        str_output_to_iter = str_output.split(", ")
        print("\n")
        
       
        str_output_to_iter.pop()
        # str_output_to_iter.remove('0.alexdf.ru ')
       
        
        for x in str_output_to_iter:
        
            email_addr ='info@s'+x
            print(email_addr)

        
        
        return
        
    

