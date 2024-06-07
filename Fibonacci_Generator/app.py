def fibonacci(n):
  if n==1 or n==0:
    return n
  else:
    return fibonacci(n-2)+fibonacci(n-1)
number = int(input("enter a number...:"))
if number<0:
  print("please enter a positive number...")
i=0
print("this is a fibonacci series :")
for i in range(0,number):
  print(fibonacci(i))