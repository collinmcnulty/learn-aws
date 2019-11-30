import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="clouduser",
            password="cloudpass",
            host="postgres-db-instance.cqzncuj1ztnt.us-east-2.rds.amazonaws.com",
            database="postgresdb")

    cursor = connection.cursor()

    create_table_query = '''SELECT * from mobile; '''

    cursor.execute(create_table_query)
    record = cursor.fetchall()
    connection.commit()
    print(record)

except Exception as error:
    print("Table creation error:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection to db closed")
