#install library mysql-connector-python
import mysql.connector

#creating connection


class update:
    def __init__(self):
        self.conn=mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Pavanpavvi@2",
                database = "bank"
                )
        
    def myupdate(self,table_name,column_name,new_value,cusid):
        cur = self.conn.cursor()
        if new_value.isnumeric():
            print("test1")
            cur.execute(f"UPDATE {table_name} set {column_name}={int(new_value)} where customerID={cusid}")
        else:
            print("test2")
            cur.execute(f"UPDATE {table_name} set {column_name}='{new_value}' where customerID={cusid}")
        self.conn.commit()
        print("updated sucessfully")