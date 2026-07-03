import json
import random


class Product:

    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = float(price)
        self.stock = int(stock)

    def add_stock(self, qty):

        if qty < 0:
            print("Invalid Quantity")
            return

        self.stock += qty

    def remove_stock(self, qty):

        if qty > self.stock:
            print("Not Enough Stock")
            return

        self.stock -= qty

    def value(self):

        return self.price * self.stock

    def display(self):

        print(self.id, self.name, self.price, self.stock)


inventory = []


def add_product():

    id = input("ID : ")
    name = input("Name : ")
    price = float(input("Price : "))
    stock = int(input("Stock : "))

    product = Product(id, name, price, stock)

    inventory.append(product)


def display():

    if not inventory:
        print("Inventory Empty")
        return

    for p in inventory:
        p.display()


def search(id):

    for p in inventory:

        if p.id == id:
            return p

    return None


def expensive():

    if not inventory:
        return None

    high = inventory[0]

    for p in inventory:

        if p.price > high.price:
            high = p

    return high


def cheapest():

    if not inventory:
        return None

    low = inventory[0]

    for p in inventory:

        if p.price < low.price:
            low = p

    return low


def total_value():

    total = 0

    for p in inventory:
        total += p.value()

    return total


def save():

    data = []

    for p in inventory:

        data.append({
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "stock": p.stock
        })

    with open("inventory.json", "w") as file:
        json.dump(data, file)


def load():

    try:

        with open("inventory.json", "r") as file:
            data = json.load(file)

        inventory.clear()

        for item in data:

            inventory.append(
                Product(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"]
                )
            )

    except FileNotFoundError:
        print("inventory.json not found")


while True:

    print("\n1 Add Product")
    print("2 Display")
    print("3 Search")
    print("4 Expensive")
    print("5 Cheapest")
    print("6 Total Value")
    print("7 Save")
    print("8 Load")
    print("9 Random Discount")
    print("10 Exit")

    choice = input("Choice : ")

    if choice == "1":

        add_product()

    elif choice == "2":

        display()

    elif choice == "3":

        id = input("Enter ID : ")

        product = search(id)

        if product:
            product.display()
        else:
            print("Product Not Found")

    elif choice == "4":

        p = expensive()

        if p:
            p.display()

    elif choice == "5":

        p = cheapest()

        if p:
            p.display()

    elif choice == "6":

        print("Total Value :", total_value())

    elif choice == "7":

        save()

    elif choice == "8":

        load()

    elif choice == "9":

        if inventory:

            p = random.choice(inventory)

            p.price -= 100

            print(p.name, "got ₹100 discount")

        else:

            print("Inventory Empty")

    elif choice == "10":

        break

    else:

        print("Wrong Choice")

print("Program Finished")