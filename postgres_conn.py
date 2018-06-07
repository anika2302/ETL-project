import psycopg2
import pprint
import csv
import sys
conn_string="host='localhost' dbname='ZAGDB' user='postgres' password='Anik@2302'"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()
#cursor.execute("select relname,relpages from pg_class order by relpages DESC")
cursor.execute("select * from soldvia")
records=cursor.fetchall()
pprint.pprint(records)

with open('C:/Users/Anika/PycharmProjects/redshift/soldvia.csv', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for row in records:
        writer.writerow(row)