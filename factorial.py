n=int(input("a: "))
sum=1
for i in range(n,0,-1):
    sum=sum*i
print(sum)


f=1
n=int(input("Enter no. for factorial="))
for x in range(1,1+n):
      f=f*x
print("factorial of a no.",f)


n=int(input("c="))
def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print("factorial of a number=",f)
