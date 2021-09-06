import conc.connect as cc
import datetime
class AdminWork:
    def create_acc(self):
        ob=cc.connect()
        con=ob.con1()
        stm=con.cursor()
        q="select max(accno) from user_details"
        stm.execute(q)
        result=stm.fetchall()#to store the data into result exeute by quere
        accno=0
        for r in result:
            accno=r[0]
        accno=accno + 1
        print("New account no:",accno)
        name=input("Enter name:")
        address=input("Enter address:")
        phno=input("Enter phno:")
        aadhaar_id=input("Enter aadhaar id:")
        email=input("Enter email:")
        password=input("Enter password:")
        q1="insert into user_details values('%d','%s','%s','%s','%s','%s','%s')"%(accno,name,address,phno,aadhaar_id,email,password)
        stm.execute(q1)
        tid=1
        today=datetime.date.today()
        
        dt=str(today)
        damt=int(input("Enter opp bal:"))
        wamt=0
        bal=damt
        q2="insert into transaction values('%d','%d','%s','%d','%d','%d')"%(accno,tid,dt,damt,wamt,bal)
        stm.execute(q2)
        con.commit()
        print("Account created successfully")
        con.close()
    def deposit(self):
        ob=cc.connect()
        con=ob.con1()
        stm=con.cursor()
        accno=int(input("Enter accno:"))
        today=datetime.date.today()
        dt=str(today)
        damt=int(input("Enter amount to deposit"))
        q="select bal,tid from transaction where accno='%d' and tid=(select max(tid) from transaction where accno='%d')"%(accno,accno)
        stm.execute(q)
        result=stm.fetchall()
        (bal,tid)=(0,0)
        for r in result:
            bal=r[0]
            tid=r[1]
        wamt=0
        tid=tid+1
        bal=bal+damt
        q1="insert into transaction values('%d','%d','%s','%d','%d','%d')"%(accno,tid,dt,damt,wamt,bal)
        stm.execute(q1)
        con.commit()
        print("deposited successfully and bal is Rs.",bal,"/-")
        con.close()
    def withdrawl(self):
        ob=cc.connect()
        con=ob.con1()
        stm=con.cursor()
        accno=int(input("Enter accno:"))
        today=datetime.date.today()
        
        dt=str(today)
        wamt=int(input("Enter amount to withdrawl"))
        q="select bal,tid from transaction where accno='%d' and tid=(select max(tid) from transaction where accno='%d')"%(accno,accno)
        stm.execute(q)
        result=stm.fetchall()
        (bal,tid)=(0,0)
        for r in result:
            bal=r[0]
            tid=r[1]
        damt=0
        tid=tid+1
        if(bal-wamt>0):
            bal=bal-wamt
            q1="insert into transaction values('%d','%d','%s','%d','%d','%d')"%(accno,tid,dt,damt,wamt,bal)
            stm.execute(q1)
            con.commit()
            print("withdrawl successfully and bal is Rs.",bal,"/-")
        else:
            print("Insufficiant bal")
        con.close()
    def ministmt(self):
        ob=cc.connect()
        con=ob.con1()
        stm=con.cursor()
        accno=int(input("Enter accono:"))
        q="select * from transaction where accno='%d' order by tid desc"%(accno)
        stm.execute(q)
        result=stm.fetchall()
        for r in result:
            print(r[1],r[2],r[3],r[4],r[5])
        con.close()
    def transfer(self):
        ob=cc.connect()
        con=ob.con1()
        stm=con.cursor()
        print("Enter from account:")
        faccno=int(input())
        taccno=int(input("Enter to account"))
        amt=int(input("Enter amount:"))
        today=datetime.date.today()
        
        dt=str(today)
        q="select bal,tid from transaction where accno='%d' and tid=(select max(tid) from transaction where accno='%d')"%(faccno,faccno)
        stm.execute(q)
        (bal,tid)=(0,0)
        result=stm.fetchall()
        for r in result:
            bal=r[0]
            tid=r[1]
        tid=tid+1
        damt=0
        wamt=amt
        bal=bal-amt
        q1="insert into transaction values('%d','%d','%s','%d','%d','%d')"%(faccno,tid,dt,damt,wamt,bal)
        stm.execute(q1)
        (tid,bal)=(0,0)
        q2="select bal,tid from transaction where accno='%d' and tid=(select max(tid) from transaction where accno='%d')"%(taccno,taccno)
        stm.execute(q2)
        result=stm.fetchall()
        for r in result:
            bal=r[0]
            tid=r[1]
        tid=tid+1
        wamt=0
        damt=amt
        bal=bal+amt
        q3="insert into transaction values('%d','%d','%s','%d','%d','%d')"%(taccno,tid,dt,damt,wamt,bal)
        stm.execute(q3)
        print("balance transfer successfully")
        con.commit()
        con.close()
    def balcheck(self):
        accno=int(input("Enter accno:"))
        ob=cc.connect()
        con=ob.con1()
        stm=con.cursor()
        q="select bal from transaction where accno='%d' and tid=(select max(tid) from transaction where accno='%d')"%(accno,accno)
        stm.execute(q)
        bal=0
        result=stm.fetchall()
        for r in result:
            bal=r[0]
        print("Account balance is ",bal)
        con.close()
    def cpass(self,userid):
        pass1=input("enter new password:")
        ob=cc.connect()
        con=ob.con1()
        stm=con.cursor()
        q="update admin_login set password='%s' where userid='%s'"%(pass1,userid)
        stm.execute(q)
        con.commit()
        print("password changed successfully")
        con.close()
        








        





        






        
    
        





        


        
        



        


        






        

        
        





        
        




        
        
        




        

        




        




        



        






        








        
            
        
