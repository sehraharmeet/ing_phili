x=0
while x<=3:
    emp_Name=input("Enter Name")
    emp_Age=int(input("Enter Age"))
    print(f'Employee Name {emp_Name} Employee Age {emp_Age}')
    emp_Age=emp_Age+50

    #start
    if(emp_Age>100):
        print("goood")    
    else:
        print("Not OK")   
    #end if
    print("Thanks")
    x+=1