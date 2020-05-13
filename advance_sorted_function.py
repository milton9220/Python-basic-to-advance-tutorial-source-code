




products=[
        {'name':'Shirt','price':500},
        {'name':'Shirt','price':600},
        {'name':'Shirt','price':100},
        {'name':'Shirt','price':1500},
]


print(sorted(products,key=lambda item: item.get('price'),reverse=True))


