import psycopg2 as pg2
import psycopg2.pool as pg2_pool
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



conn = pg2.connect("user=postgres port=5433 dbname=pagila")
demo_pool = pg2.pool.ThreadedConnectionPool(2 , 25 ,port=5433 ,user="postgres" ,dbname="pagila")




# # demo_pool.closeall()
# # conn.close()

conn_3 = demo_pool.getconn()

cur = conn_3.cursor()
cur.execute("SELECT * FROM actor")
data =  cur.fetchall()


# attach postgres dataset to Pandas dataframe

df_pagila_actors = pd.DataFrame(data)
print(df_pagila_actors)




conn_1 = demo_pool.getconn()
conn_2 = demo_pool.getconn()
conn_4 = demo_pool.getconn()
conn_5 = demo_pool.getconn()

conn_6 = demo_pool.getconn()
conn_7 = demo_pool.getconn()
conn_8 = demo_pool.getconn()
conn_9 = demo_pool.getconn()

# conn_10 = demo_pool.getconn()
# conn_11 = demo_pool.getconn()
# conn_12 = demo_pool.getconn()
# conn_13 = demo_pool.getconn()

# conn_14 = demo_pool.getconn()
# conn_15 = demo_pool.getconn()
# conn_16 = demo_pool.getconn()
# conn_17 = demo_pool.getconn()

# conn_18 = demo_pool.getconn()
# conn_19 = demo_pool.getconn()
# conn_21 = demo_pool.getconn()
# conn_22 = demo_pool.getconn()

conn_23= demo_pool.getconn()
conn_25 = demo_pool.getconn()



cur25 = conn_3.cursor()
cur25.execute("SELECT * FROM inventory")
data_invtr =  cur25.fetchall()


# attach postgres dataset to Pandas dataframe

df_pagila_inventory = pd.DataFrame(data_invtr)
print(df_pagila_inventory)


conn_24 = demo_pool.getconn()
conn_26 = demo_pool.getconn()

demo_pool.closeall()
conn.close()



# conn_27 = demo_pool.getconn()
# conn_28 = demo_pool.getconn()
# conn_29 = demo_pool.getconn()
# conn_30 = demo_pool.getconn()