# Date: 2022-01-02
# Description: a program which extracts information from a postgres databse utilizing SQL 
#              CREATE command.
# Data Engineer: Roger De Four
    




import pandas as pd
import numpy as np
import psycopg2 as pg2
import pymongo as mg
from matplotlib import pyplot as plt

#1 Open a connection to a Postgres server
conn = pg2.connect(host="localhost" , dbname="demo" , user="postgres" , port="5433" ,   options="-c search_path=bookings,public")

#2 Add the cursor
cur = conn.cursor()

#3 Connect to table in database


sql = """


    
CREATE TABLE IF NOT EXISTS bordeing_pass_tickets_details  as 

SELECT 
   bpass.ticket_no , bpass.flight_id , bpass.boarding_no, bpass.seat_no ,
   tik.book_ref , tik.passenger_id , tik.passenger_name  , tik.contact_data
   ,  tfl.fare_conditions , tfl.amount
FROM  

   bookings.boarding_passes as bpass
INNER JOIN bookings.ticket_flights as tfl
      
ON
  tfl.ticket_no  = bpass.ticket_no
  AND  tfl.flight_id = bpass.flight_id	

INNER JOIN 	
 bookings.tickets as  tik 	
ON
	tfl.ticket_no = tik.ticket_no
	

 ;


"""

sql_input_data = "SELECT * FROM  bordeing_pass_tickets_details ORDER BY flight_id ASC LIMIT 100000"


cur.execute(sql )
cur.execute(sql_input_data )

#4 Fetch the records

data_records = cur.fetchall()

# # print(data_records)

# df_flights  = pd.DataFrame(data_records, columns=["flight_id" , "flight_no" , "scheduled_departure" , "scheduled_arrival " , "departure_airport" ,"arrival_airport" , "status" , "aircraft_code" , "actual_departure" , "actual_arrival"])

df_flights  = pd.DataFrame(data_records , columns = [

 "ticket_no" , "flight_id" , "boarding_no", "seat_no" ,
   "book_ref" , "passenger_id" , "passenger_name"  , "contact_data"
   ,  "fare_conditions" , "amount"
])


print(df_flights )
