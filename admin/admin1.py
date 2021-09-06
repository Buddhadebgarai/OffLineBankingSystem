#admin1.py
import admin.admin2 as aa
import conc.connect as cc
class adminc:
    def validate(self):
        userid=input("Enter userid:")
        password=input("Enter password")
        ob=cc.connect()
        con=ob.con1()
        stm=con.cursor()
        q="select * from admin_login where userid='%s' and password='%s'"%(userid,password)
        stm.execute(q)
        result=stm.fetchall()
        con.close()
        return len(result),userid
    def amenu(self):
        (f,userid)=self.validate()
        if f==1:
            print("welcome admin:")
            ob=aa.AdminWork()
            while 1:
                print("1 for create new acc")
                print("2 for deposit")
                print("3 for withdrawl")
                print("4 for mini statement")
                print("5 for transfer")
                print("6 for bal check")
                print("7 for change password")
                print("8 for exit")
                ch=int(input("Enter your choice"))
                if ch==1:
                    ob.create_acc()
                if ch==2:
                    ob.deposit()
                if ch==3:
                    ob.withdrawl()
                if ch==4:
                    ob.ministmt()
                if ch==5:
                    ob.transfer()
                if ch==6:
                    ob.balcheck()
                if ch==7:
                    ob.cpass(userid)
                if ch==8:
                    break
        else:
            print("invalid userid or password")
            


    
        
    
