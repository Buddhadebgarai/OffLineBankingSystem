#user2.py
import conc.connect as cc
class userwork:
    def balcheck(self,accno):
        ob=cc.connect()
        con=ob.con1()
        stm=con.cursor()
        q="select bal from transaction where accno='%d' and tid=(select max(tid) from transaction where accno='%d')"%(accno,accno)
        stm.execute(q)
        bal=0
        result=stm.fetchall()
        for r in result:
            bal=r[0]
        print("balance is",bal)
        con.close()
    def ministmt(self,accno):
        ob=cc.connect()
        con=ob.con1()
        stm=con.cursor()
        q="select * from transaction where accno='%d'"%(accno)
        stm.execute(q)
        result=stm.fetchall()
        for r in result:
            print(r[1],r[2],r[3],r[4],r[5])
        con.close()
    def passchange(self,accno):
        pass1=input("Enter new password:")
        ob=cc.connect()
        con=ob.con1()
        stm=con.cursor()
        q="update user_details set password='%s' where accno='%d'"%(pass1,accno)
        stm.execute(q)
        print("password changed successfully")
        con.commit()
        con.close()
        


        







        





        
