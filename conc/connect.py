#connect.py
import pymysql
class connect:
    def con1(self):
        con=pymysql.connect("localhost","root","","tue530db")
        return con
