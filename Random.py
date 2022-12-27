import random
import os

roll = input("Want to roll a dice? (yes / no): ")

while (roll.lower() == "yes"):
    number = random.randint(1,6)
    print("Your number is: ")
    print(number)
    print()   

    if number == 1:
        print("[         ]")
        print("[         ]")
        print("[    O    ]")
        print("[         ]")
        print("[         ]")

    if number == 2:
        print("[         ]")
        print("[         ]")
        print("[  O   O  ]")
        print("[         ]")
        print("[         ]")

    if number == 3:
        print("[         ]")
        print("[         ]")
        print("[  O O O  ]")
        print("[         ]")
        print("[         ]")

    if number == 4:
        print("[         ]")
        print("[  O   O  ]")
        print("[         ]")
        print("[  O   O  ]")
        print("[         ]")    

    if number == 5:
        print("[         ]")
        print("[  O   O  ]")
        print("[    O    ]")
        print("[  O   O  ]")
        print("[         ]")

    if number == 6:
        print("[         ]")
        print("[  O   O  ]")
        print("[  O   O  ]")
        print("[  O   O  ]")
        print("[         ]")   
        
    print()    
    roll = input("Wanna roll once more? (yes / no): ")

if roll.lower() == "no":
    print()
    print("Bye!")

print()
print("Thank you! Hope you got your number :)")

os.system("pause")