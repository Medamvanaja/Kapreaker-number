n=int(input())
count=0
temp=n
sq=n*n
while n>0:
    r=n%10
    n=n//10
    count=count+1
p=10**count

q=sq%p
rem=sq//p
sum=q+rem
if(sum==temp):
    print("Kaprekar Number")
else:
    print("Not a Kaprekar Number")
