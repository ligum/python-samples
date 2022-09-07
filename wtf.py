from tkinter import N


answer = input("Enter yes or no: ") 
if answer == "yes": 
    print("wtf")
elif answer == "no": 
    print("ftw") 
else: 
    print("Please enter yes or no.")
###############################################    
answer = " "
while answer not in ["Yes", "yes", "Y", "y", "No", "no", "N", "n"]: 
    answer = input("Let's play an israeli Loto?\n") 
    if answer=="Yes" or answer=="yes" or answer=="Y" or answer=="y": 
        print("Good for you!! Proceed\n")
        import random
        print("let's play israeli LOTO" )
        randomlist = random.sample(range(1, 38), 6)
        a = random.sample(range(1,9), 1)
        print(randomlist + a)
        x = random.randint(111111,999999)
        print(x) 
    elif answer=="No" or answer=="no" or answer=="N" or answer=="n": 
        print("Do not proceed\n") 
    else: 
        print("Please type Yes or No\n")
        
