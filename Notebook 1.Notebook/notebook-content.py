# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "cfe5c8eb-d442-4755-a46c-ca6c0d4025a8",
# META       "default_lakehouse_name": "LH1",
# META       "default_lakehouse_workspace_id": "6f2713a3-731f-4a96-bcc9-4508797f6966",
# META       "known_lakehouses": [
# META         {
# META           "id": "cfe5c8eb-d442-4755-a46c-ca6c0d4025a8"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

# Welcome to your new notebook
# Type here in the cell editor to add code!
a= spark.sql(" insert into  LH1.dbo.t1 (col1,col2)  select 'e4' col1, 'f4' col2  ")
b= spark.sql(" select * from LH1.dbo.t1  ")
display(b)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
