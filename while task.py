# while task
#  تشخیص اعداد بخش‌پذیر
number = input("Enter a number:")
number = int(number)
while True:
    if number % 15 == 0:
        print("Fizzbuzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("Fizz")
    else:
        print(number)
    break

#2
#نظرسنجی نام و کتاب
book ={}
while True:
    name = input("Enter a name:")
    bookk = input("\nEnter a book name:")
    book[name] = bookk
    pr = input("\n is there anyone else? \n if there is no one send 'stop'")
    if pr == 'stop':
        break
for i , g in book.items():
    print(f"{i} loves reading {g}")

#3
#shopping_cart
shopping_cart = ['milk', 'bread', 'eggs', 'apple']
purchased_items= []
while shopping_cart:
    a = shopping_cart.pop()
    b = purchased_items.append(a)
for item in purchased_items:
    print(f"purchased: {item}".title())
print(purchased_items)

#4
#users
users = ['admin', 'john', 'sara', 'mike']
user_info = {}
while users:
    d = input("Enter a user name:")
    if d in users:
        f = input("enter your age please")
        ff = input("enter your city please")
        user_info[f] = ff
    if d == 'stop':
        break
    else:
        print("User not found!")
for k, v in user_info.items():
        print(f"information :{k},{v}")
