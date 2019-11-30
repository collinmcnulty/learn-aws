import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="clouduser",
            password="cloudpass",
            host="postgres-db-instance.cqzncuj1ztnt.us-east-2.rds.amazonaws.com",
            database="postgresdb")

    cursor = connection.cursor()

    delete_table_query = '''DROP TABLE IF EXISTS mobile'''

    create_table_query = '''CREATE TABLE mobile
        (ID SERIAL PRIMARY KEY NOT NULL,
        MODEL TEXT NOT NULL,
        PRICE REAL); '''

    cursor.execute(delete_table_query)
    cursor.execute(create_table_query)
    connection.commit()
    print("Table 'mobile' created successfully")

except Exception as error:
    print("Table creation error:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection to db closed")
