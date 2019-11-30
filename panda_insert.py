from insert import insert_mobile
import pandas as pd
import sqlalchemy

engine_def = 'postgresql+psycopg2://clouduser:cloudpass@postgres-db-instance.cqzncuj1ztnt.us-east-2.rds.amazonaws.com/postgresdb'

engine = sqlalchemy.create_engine(engine_def)

phones = pd.DataFrame({
    'model': ['panda', 'g2', 'rx'],
    'price': [400, 500, 749.99],
    })

phones.to_sql('mobile', engine, if_exists='append', index=False)

# for phone in range(len(phones['model'])):
#     insert_mobile(phones['model'][phone], phones['price'][phone])


