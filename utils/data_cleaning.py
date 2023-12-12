import pandas as pd
from db_connection import create_db_engine

# import the data from postgresql to pandas dataframe
df = pd.read_sql_table("xdr_data", con=create_db_engine())
print(df.head(15))
