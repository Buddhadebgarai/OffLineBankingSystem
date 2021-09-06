import admin.admin1 as aa
import user.user1 as uu
print("WELCOMT TO CHIT BANK")
while 1:
    print("1 for Admin\n2 for user\n3 for exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        aob=aa.adminc()
        aob.amenu()
    elif ch==2:
        uob=uu.userc()
        uob.umenu()
    else:
        break
