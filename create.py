#installed library mysql-connector-python
import mysql.connector


#creating connection
class insert:
    def __init__(self):
        self.conn=mysql.connector.connect(
                host='localhost',
                user='root',
                password='Pavanpavvi@2',
                database='bank')

    def personal_details(self,cid,fname,lname,addr,pn,an,pan):
        cur = self.conn.cursor() # creating cursor
        cur.execute(f"INSERT INTO PERSONAL_DETAILS VALUES({cid},'{fname}','{lname}','{addr}',{pn},'{an}','{pan}')")
        self.conn.commit()
        print('----------------Personal Details have been saved successfully------------------')

    def bank_details(self,acn,cid,ifsc,actype):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO BANK_DETAILS VALUES({acn},{cid},'{ifsc}','{actype}')")
        self.conn.commit()
        print("------------------Bank details has been sucessfully saved-----------------------")

    def transaction_details(self,tid,sact,ract,amnt,mtd):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO TRANSACTION_DETAILS VALUES({tid},{sact},{ract},{amnt},'{mtd}')")
        self.conn.commit()
        print('--------------Transaction Details have been saved successfully-------------------')

    def account_details(self,acn,tid,amnt,clbln,tt):
        cur = self.conn.cursor()
        cur.execute(f"INSERT INTO ACCOUNT_DETAILS VALUES({acn},{tid},{amnt},{clbln},'{tt}')")
        self.conn.commit()
        print('---------------Account Details have been saved successfully---------------------')