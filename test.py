from shoppinglistDAO import shoppinglistDAO as shopDAO

shop = shopDAO.getAll()
for i in shop:
    print(i)