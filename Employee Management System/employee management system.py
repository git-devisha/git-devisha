import pymysql as sql
import sys
con1 = sql.connect(host="127.0.0.1", user="root", password="sql", database="empdb", charset="utf8")
def insertRecord():
    id=int(input("enter employee id- "))
    name = input("name:")
    gender = input("gender:")
    email = input("email:")
    date = input("date:")
    dept = input("dept:")
    password = input("password:")
    
    cur=con1.cursor()
    qry="insert into empinfo values(%d,'%s', '%s','%s', '%s','%s','%s')"%(id, name, gender, email,date, dept, password)
    print(qry)
    cur.execute(qry)
    if cur.rowcount==1:
        print("inserted")
    else:
        print("error")
    con1.commit()
def deleteRecord():
    id = int(input("enter id:"))
    qry= f"delete from empinfo where eid(id)"
    cur= con1.cursor()
    cur.execute(qry)
    con1.commit()
    if cur.rowcount==1:
        print("inserted")
    else:
        print("error")
def updateRecord():
    id=int(input("employee id:"))
    cur=con.cursor()
    cur.execute(f"select *from empinfo where eid=(id)")
    if cur.rowcount ==1:
        print("press 21 to update name:")
        print("press 22 to update gender:")
        print("press 23 to update email:")
        print("press 24 to update date:")
        print("press 25 to update dept:")
        print("press 26 to update password:")
        print("press 27 to update previous menu:")
        ch = int(input("enter choice:"))
        if ch==221:
            name = input("enter name:")
            qry = f"update empinfo set name='{name}' where eid ={id}"
            
        elif ch==222:
            name = input("enter gender:")
            qry = f"update empinfo set gender='{gender}' where eid ={id}"
        elif ch==223:
            name = input("enter email:")
            qry = f"update empinfo set email='{email}' where eid ={id}"
        elif ch==224:
            name = input("enter join date:")
            qry = f"update empinfo set date='{date}' where eid ={id}"
        elif ch==225:
            name = input("enter password:")
            qry = f"update empinfo set password='{password}' where eid ={id}"
        elif ch==226:
            name = input("enter dept:")
            qry = f"update empinfo set dept='{dept}' where eid ={id}"
        else:
            pass
        if ch<227:
            cur.execute(qry)
            if cur.rowcount==1:
                print("record updated")
            else:
                print("updation failed")
        else:
            print("invalid employee id")
        
def displayRecord():
    qry = 'select * from empinfo'
    cur= con1.cursor()
    cur.execute(qry)
    if cur.rowcount !=0:
        print(cur.fetchone())
        print(cur.fetchone())
        print(cur.fetchone())
    else:
        print("no record")
while True:
    print("press 21 to insert")
    print("press 22 to update")
    print("press 23 to delete")
    print("press 24 to display")
    print("press 25 to exit")
    choice= int(input("choice:"))
    if choice ==21:
       insertRecord()
    elif choice ==22:
       updateRecord()
    elif choice == 23:
       deleteRecord()
    elif choice==24:
       displayRecord()
    else:
       sys.exit

con1.close()

