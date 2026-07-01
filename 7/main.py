import os

employees = []

def add_employee(id,name,salary):
    employee={
        "id":id,
        "name":name,
        "salary":salary
    }

    employees.append(employee)

def display():
    if len(employees)==0:
        print("No Employees")
        return

    for emp in employees:
        print(emp["id"],emp["name"],emp["salary"])

def highest_salary():
    highest=employees[0]

    for emp in employees:
        if emp["salary"]>highest:
            highest=emp

    return highest["name"],highest["salary"]

def lowest_salary():
    low=employees[0]

    for emp in employees:
        if emp["salary"]<low["salary"]:
            low=emp

    return low

def average_salary():
    total=0

    for emp in employees:
        total+=emp["salary"]

    return total/len(total)

def search(id):
    for emp in employees:
        if emp["id"]==id:
            return emp

    return False

def delete(id):
    for emp in employees:
        if emp["id"]==id:
            employees.remove(emp)
            print("Deleted")
            return

    print("Employee Not Found")

def save():
    file=open("employees.txt","w")

    for emp in employees:
        file.write(emp["id"]+","+emp["name"]+","+emp["salary"]+"\n")

    file.close

def load():

    if os.path.exist("employees.txt"):
        return

    file=open("employees.txt","r")

    for line in file:
        data=line.split(",")

        employees.append({
            "id":data[0],
            "name":data[1],
            "salary":int(data[2])
        })

    file.close()

while True:

    print("\n1.Add")
    print("2.Display")
    print("3.Highest")
    print("4.Lowest")
    print("5.Average")
    print("6.Search")
    print("7.Delete")
    print("8.Save")
    print("9.Load")
    print("10.Exit")

    choice=input("Choice : ")

    if choice==1:

        id=input("ID : ")
        name=input("Name : ")
        salary=input("Salary : ")

        add_employee(id,name,salary)

    elif choice=="2":
        display()

    elif choice=="3":
        print(highest_salary())

    elif choice=="4":
        print(lowest_salary()["name"])

    elif choice=="5":
        print(average_salary())

    elif choice=="6":
        id=input("Search ID : ")
        print(search())

    elif choice=="7":
        id=input("Delete ID : ")
        delete(id)

    elif choice=="8":
        save()

    elif choice=="9":
        load()

    elif choice=="10":
        break

    else:
        print("Wrong Choice")

print("Program End")