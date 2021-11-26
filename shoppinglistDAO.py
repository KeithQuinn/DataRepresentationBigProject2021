import mysql.connector
import dbconfig as cfg

class shoppinglistDAO:
    db=""
    def __init__(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database'],
    )
    def create(self, values):
        cursor = self.db.cursor()
        sql="insert into shoppinglist (item, brand, quantity) values (%s,%s,%s)"
        cursor.execute(sql, values)
        
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from shoppinglist"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            returnArray.append(self.convertToDictionary(result))
        return returnArray

    def findByID(self, id):
        cursor = self.db.cursor()
        sql="select * from shoppinglist where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update shoppinglist set item= %s, brand=%s, quantity=%s where id = %s"
        cursor.execute(sql, values)
        self.db.commit()
    
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from shoppinglist where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.db.commit()
        print("delete done")

    def convertToDictionary(self, result):
        colnames=['id', 'item', 'brand', 'quantity']

        item={}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                item[colName] = value
        return item

shoppinglistDAO = shoppinglistDAO()