n=int(input("Enter the number"))
arr=[]
for i in range(1,n+1):
    if(i%3==0 and i%5!=0):
        arr.append("Fizz")
    elif(i%5==0 and i%3!=0):
        arr.append("Buzz")
    elif(i%15==0):
        arr.append("FizzBuzz")
    else:
        arr.append(i)


print(arr)

