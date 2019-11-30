import psycopg2
try:
    connection = psycopg2.connect(user="clouduser",
            password="cloudpass",
            host="postgres-db-instance.cqzncuj1ztnt.us-east-2.rds.amazonaws.com",
            port="5432",
            database="postgresdb")

    cursor = connection.cursor()

    print(connection.get_dsn_parameters(), "\n")

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("Connected to:", record, "\n")

except(Exception) as error:
    print("Error while connecting:", error)

finally:
    if(connection):
        cursor.close()
        connection.close()
        print("Connection Closed")
