import psycopg2
import pprint


conn_string="host='redshift.czbxvxl421qz.us-east-2.redshift.amazonaws.com' port='5439' dbname='zagdb' user='anika2302' password='Anika2302'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
#cursor.execute("select relname,relpages from pg_class order by relpages DESC")
cursor.execute("select * from soldvia")
records=cursor.fetchall()
pprint.pprint(records)

