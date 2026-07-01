import random
import math
from datetime import datetime

class BankAccount:

    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
        self.history=[]

    def deposit(self,amount):
        if amount<=0:
            print("Invalid Amount")
            return

        self.balance=self.balance+amount

        self.history.append(
            "Deposit",amount,datetime.now()
         )

    def withdraw(self,amount):

        if amount>balance:
            print("Insufficient Balance")
            return

        self.balance-=amount

        self.history.append(
            ("Withdraw",amount)
        )

    def transfer(self,other,amount):

        if amount>self.balance:
            print("Transfer Failed")
            return

        self.balance-=amount
        other.balance+=amount

        self.history.append(
            "Transfer",amount
        )

        other.history.append(
            ("Receive",amount)
        )

    def interest(rate):
        self.balance=self.balance+(self.balance*rate/100)

    def statement(self):

        print("\nAccount Holder:",self.name)
        print("Balance:",balance)

        for item in self.history:
            print(item)

class SavingAccount(BankAccount):

    def bonus(self):
        self.balance+=500

accounts=[]

def create():

    name=input("Name : ")

    bal=input("Balance : ")

    acc=SavingAccount(name,bal)

    accounts.append(acc)

def find(name):

    for acc in accounts:
        if acc.name==name:
            return acc

    return False

def richest():

    rich=accounts[0]

    for acc in accounts:

        if acc.balance>rich:
            rich=acc.balance

    return rich

def poorest():

    poor=accounts[0]

    for acc in accounts:

        if acc.balance<poor.balance:
            poor=acc

    return poor.name,poor.balance

def average():

    total=0

    for acc in accounts:
        total+=acc.balance

    return total/len(total)

def random_bonus():

    acc=random.choice(accounts)

    acc.balance+=100

while True:

    print("1.Create")
    print("2.Deposit")
    print("3.Withdraw")
    print("4.Transfer")
    print("5.Statement")
    print("6.Richest")
    print("7.Poorest")
    print("8.Average")
    print("9.Random Bonus")
    print("10.Exit")

    choice=input()

    if choice=="1":
        create()

    elif choice=="2":

        name=input("Name : ")

        acc=find(name)

        amount=input("Amount : ")

        acc.deposit(amount)

    elif choice=="3":

        name=input("Name : ")

        acc=find(name)

        amount=int(input("Amount : "))

        acc.withdraw(amount)

    elif choice=="4":

        n1=input("From : ")
        n2=input("To : ")

        a1=find(n1)
        a2=find(n2)

        amt=int(input())

        a1.transfer(a2)

    elif choice=="5":

        name=input()

        find(name).statement()

    elif choice=="6":

        print(richest().name)

    elif choice=="7":

        print(poorest())

    elif choice=="8":

        print(average())

    elif choice=="9":

        random_bonus()

    elif choice=="10":

        break

    else:

        print("Wrong Choice")

print("Finished")