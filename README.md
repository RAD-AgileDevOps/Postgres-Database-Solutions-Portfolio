# Python-data-engineering-Portfolio
#2022-12-29
Showcase of various Python examples for project work, and proof of concepts 

Contents
=================================
1. **Multi-thread program : oc_multithread_example.py**

      In this example I created a connection pool , of one main psycopg2 adapter connection, to a Postgres database. The ThreadConnection method has parameters for  minimum and maximum 'sub-connections 'to a postgres server.

2. **Visualzation of oc_multithread_example.py:**    
       
       This is an image of a test of the code contained in oc_multithread_example.py using the monitoring tool from PgAdmin4 - the default GUI tool for a            Postgres installation.
   
   See : **python_multithread_demonstration.png**
   
 3. **Anti-email spam tool:** 
            alex_spam_manager.py
            spam_mail_defense.sql  [SQL version of script]
            
  
        This was created to remedy a malware problem, that I had encountered on my work email : rogerdefour@radfinancialsystems.com.
        The problem: an email possibly of Russian orgin is continually being sent to my email, and it required the recepient to download 
        attachments - which I haven't done nor intend to do.

        That being said, I wrote a simple program in Python to create an infinite amount of email addresses, with the digit at a 
        particular position - this is a dynamic number, and so filtering the mail to spam/trash was being negated.
        
        

  4. Personal Finance  -- OOP class
 
      I developed a basic class object that can be scaled to suit the requirements of a user , basically for any aditional functionality; just create a             function/method
      
  5. Pandas/Postgres Data Analysis - **demo_pandas_analysis.py**
  
      In this scenario I connected to a Postgres RDBMS and attached it to a Pandas data frame.
      
      There is a minor complexity added to the problem - another schema was  used in th 'demo' database; therefore a normal 
      connection via the psycopg2 Postgres adater would't work. What was required was a further amendment to the
      connection method - psycopg2.connection().
      
      After some research on internet via stackoverflow I came across further information that wasn't explicitly available in the psyocopg2 documentation
      in the connect(); there is an '**options**' parameter, that accepts an input, to stipulate which schema the connection method can lookup.
      
  7. **Data Visualization : Trinidad & Tobago Stock Exchange(TTSE)**
      
            ttse_data_analysis.py
            TTSE_AngostoraSharePrice_top_ten.png 
            
      
     Share price of a large company (Angosturas) was downloaded from the TTSE and analysed in a Panda dataframe.
     
     Matplotlib(a Python Library) was then used to vizualiae the the Top and Bottom 10 share closing prices, 
     into a Stacked Bar chart for easier comparision
 
 8. **Data Visualization II : Trinidad & Tobago Central Statistical Office (CSO)**
      
      A pie chart depicting the net profit of finance & mortgage entities in the local finance sctor
      
            T_and_T_net_profit_finance_and_mortgage.png
            ttcso_central_bank_data_analysis.py
            
 9. Data Modelling - Relational Database Management Systems(RDBMS):
      
            ERD_reverse_engineered.pgerd 
            ERD_reverse_engineered.png 
 
 10. Database Querying:
      
            Postgres -INNER JOIN - part1.zip 
            Postgres INNER JOIN-SummaryReport - part2.zip
            
           
