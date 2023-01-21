class ttse_data_analysis:
        """
        Developer: Roger De Four
        Date: 2020-06-15
        Description: a class object designed to encapusale the business logic in relation to perfoming
        rudimentary data analysis on publicly available datasets from the TTSE


        """
        
        import pandas as pd
        import psycopg2 as pg2
        import numpy as np
        import matplotlib as mp
        from matplotlib import pyplot as plt
        
        # added 2023-01-08 - the globals added, for accesibility, as initially the import statements 
        # were located within class method
        global pd
        global pg2
        global np
        global plt

        def __init__(self , co_name):

            self.co_name = co_name
            print(self.co_name)  # oututs to the command line the company being analysed
        
        def data_frame(self):
            
            

            ## 2022-01-08 commented out to use a csv file as the input fro the data frame
            # # self.conn = pg2.connect("password='pEfr8mER' user='postgres' dbname='ttse_stocks'")
            # # self.cur = self.conn.cursor()
            # # self.sql = 'select * from angostura_stock_data'
            # # self.cur.execute(self.sql)
            # # self.data = self.cur.fetchall()
            # # self.df_ttse = pd.DataFrame(self.data)

            ## added 2023-01-08
            self.df_ttse = pd.read_csv(r"D:\Databases\PostgreSQL\TTSE_local_data\AngosturaHoldings2006_2020.csv")
            print(self.df_ttse)
            
        def data_analysis(self):
        
            print(self.df_ttse.describe())
             
            print("\n")    ## added 2023-01-08
            print("Top 5 records")  ## added 2023-01-08
            
            # # print(self.df_ttse.sort_values("Volume Traded", ascending=False).head())  ## amended - added sort :: 2023-01-08
            
            print(self.df_ttse[self.df_ttse["Volume Traded"] != 0].sort_values("Volume Traded", ascending=False).head())  ## amended - added sort :: 2023-01-08
            # # # print(self.df_ttse[self.df_ttse["Volume Traded"] != 0])   ## workings
            
            print("\n")    ## added 2023-01-08
             
            print("Bottom 5 records")  ## added 2023-01-08
             
            print(self.df_ttse[self.df_ttse["Volume Traded"] != 0].sort_values("Volume Traded", ascending=False).tail())  ## amended - added sort :: 2023-01-08

            print("\n")
            
        def charting (self):
            
            print("------------------------------- Charting Section-----------------------------------------\n")
            
            df_trades_top25 = self.df_ttse[self.df_ttse["Volume Traded"] != 0].sort_values("Volume Traded", ascending=False).head(10)

            df_trades_bot25 = self.df_ttse[self.df_ttse["Volume Traded"] != 0].sort_values("Volume Traded", ascending=False).tail(10)

            df_t25_chart_data = df_trades_top25[["Date" , "ClosingQuote"]] 
            
            df_bot25_chart_data = df_trades_bot25[["Date" , "ClosingQuote"]]
            
            print("chart data -top 10\n")
            print(df_t25_chart_data)
            print("\n")
            print("chart data -bottom 10\n")
            print(df_bot25_chart_data)
            
            ordinal_category = ['Tier 1', 'Tier2' ,'Tier 3' ,'Tier4' , 'Tier 5', 'Tier6' ,'Tier 7' ,'Tier8' , 'Tier 9' ,'Tier10']
            # # plt.bar(df_t25_chart_data["Date"] , df_t25_chart_data["ClosingQuote"] , color='r')
            
            # # plt.bar(df_t25_chart_data["Date"] , df_bot25_chart_data["ClosingQuote"] , bottom=df_t25_chart_data["ClosingQuote"] ,  color='g')
           
            plt.bar(ordinal_category, df_t25_chart_data["ClosingQuote"] , color='r')
            
            plt.bar(ordinal_category , df_bot25_chart_data["ClosingQuote"] , bottom=df_t25_chart_data["ClosingQuote"] ,  color='g')
            
            plt.title (self.co_name +"'s "+ "Share price - Top 10 Closing Price")
            plt.show()


co_stat = ttse_data_analysis('Angostura')  
co_stat.data_frame()
co_stat.data_analysis()
co_stat.charting()


            

        
            
            