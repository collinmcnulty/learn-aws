import psycopg2
from psycopg2 import Error


def insert_mobile(model, price):
    
    
    price = float(price)
    model = str(model)
    print(price, model)
    if "'" in model:
        raise(ValueError, "model must not contain '")
    try:
        connection = psycopg2.connect(user="clouduser",
                password="cloudpass",
                host="postgres-db-instance.cqzncuj1ztnt.us-east-2.rds.amazonaws.com",
                database="postgresdb")

        cursor = connection.cursor()

        create_table_query = '''INSERT INTO mobile(MODEL, PRICE)
        VALUES('{}', {}); '''.format(model, price)

        cursor.execute(create_table_query)
        connection.commit()
        print("Record inserted successfully")

    except Exception as error:
        print("Table creation error:", error)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection to db closed")

if __name__ == '__main__':
    insert_mobile('iPhone', 1000)
