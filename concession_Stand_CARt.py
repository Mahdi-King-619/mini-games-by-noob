menu={"popcorn":5.99,
      "50 Cent chicken":0.50,
      "Ice-cream":1.99,
      "Coke":0.99,
      "Pizza":3.99,
      "Chocolate Cupcake":2.09,
      "Chicken":1.69,
      "Mini Burger":2.51,
      "Medium Burger":3.99,
      "Large Burger":4.99,
      "Extra Large Burger":5.99,
      "nachos":1.99,
      "Lemonade": 4.25,
      "Pretzels":3.50,
      "Fries":2.50,
      "Chips":1.00
      }
cart=[]
total=0
print("------------MENU------------")
for key,value in menu.items():
    print(f"{key:20}: ${value:.2f}")
print("-----------------------------")

while True:
    choice=input("Enter your choice of food(q to quit): ")
    if choice.lower()=='q':
        break
    elif menu.get(choice) is not None:
        cart.append(choice)
print("--------------Your cart---------------")
for food in cart:
    total=total+menu.get(food)
    print(food,end=" ")

print()
print(f"Total is: ${total:.2f}")

