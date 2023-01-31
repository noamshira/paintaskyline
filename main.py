print("enter a number")
num=int(input())
arr=[]
print("enter", num, "numbers into the array ")
for i in range(0,num):
    n=int(input())
    arr.append(n)
counter=arr[0]
for i in range(1,num):
    if arr[i]>arr[i-1]:
        counter=counter+(arr[i]-arr[i-1])
print(counter)





