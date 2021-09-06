#user1.py
import conc.connect as cc
import user.user2 as uu
class userc:
    def validate(self):
        accno=int(input("Enter accno:"))
        password=input("Enter password:")
        ob=cc.connect()
        con=ob.con1()
        stm=con.cursor()
        q="select * from user_details where accno='%d' and password='%s'"%(accno,password)
        stm.execute(q)
        result=stm.fetchall()
        con.close()
        return len(result),accno
    def umenu(self):
        (f,accno)=self.validate()
        if f==1:
            print("welcome ",accno)
            uob=uu.userwork()
            while 1:
                print("1 for balance check")
                print("2 for mini statement")
                print("3 for password change")
                print("4 for exit")
                ch=int(input("enter your choice"))
                if ch==1:
                    uob.balcheck(accno)
                if ch==2:
                    uob.ministmt(accno)
                if ch==3:
                    uob.passchange(accno)
                if ch==4:
                    break
        else:
            print("invalid accno or password")

            



    

        
