
answer = input("hello! would you like to play an israeli LOTO? Enter (Y)es or (N)o: ") 
if answer == "Y": 
    import random
    print("let's play israeli LOTO" )
    randomlist = random.sample(range(1, 38), 6)
    a = random.sample(range(1,9), 1)
    print(randomlist + a)
    x = random.randint(111111,999999)
    print(x)
elif answer == "N": 
    print("so what are you doing here?") 
else: 
    print("Please enter Y or N.")

  

