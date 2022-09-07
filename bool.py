name = input("What's your name?")
print ("Hello")
if name == "Vova":
    print ("Vova")
else:
     print ("dudu")

a = int(input("type A "))
b = int(input("type B "))
c = int(input("type C "))
if b == a and b > c and a > c:
    print("a and b are equal and greater than c")
elif b == a and b < c and a < c:
    print("a and b are equal and smaller than c")
elif b == c and b > a and c > a:
    print("b and c are equal and greater than a")
elif b == c and b < a and c < a:
    print("b and c are equal and smaller than a")
elif a == c and a > b and c > b:
    print("a and c are equal and greater than b")
elif a == c and a < b and c < b:
    print("a and c are equal and smaller than b")
elif b > a and b < c:
    print("b is greater than a but not than c")
elif b > a and b > c:
    print("b is greater than a and c altogether") 
elif a > b and a < c:
    print("a is greater than b but not than c")
elif a > b and a > c:
    print("a is greater than b and c altogether")
elif c > a and c < b:
    print("c is greater than a but not than b")
elif c > a and c > b:
    print("c is greater than a and b altogether")
else:
    print("A=B=C")
print('Thank you very much')
import time
time.sleep(5)