#1
n = input("Enter Number to calculate sum " )
n = int (n)
sum = 0
for num in range(0, n+1, 1):
    sum = sum+num
print("SUM of first ", n, "numbers is: ", sum )

#2
print(("type your number for execute a factorial!"))
x = int (input())
y = 0
for i in range(x+1):
    y += i
print (y)

#3
k = 0
l = 0
while l != -1:
    k += l
    l = int(input())
print(k)
exit 

