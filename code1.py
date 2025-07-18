print("hello world welcome to 10k coders")
n=11
count=0
print("factors are ",end=" ")
for i in range(1,n+1):
    if n%i==0:
        count+=1
        print(i,end=" ")
if count>2:
    print("not prime number")
else:
    print("prime number")
    