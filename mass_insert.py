from insert import insert_mobile



phones = {
    'model': ['g1', 'g2', 'rx'],
    'price': [400, 500, 749.99],
    }

for phone in range(len(phones['model'])):
    insert_mobile(phones['model'][phone], phones['price'][phone])


