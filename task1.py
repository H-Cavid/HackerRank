"""If  is odd, print Weird#
If  is even and in the inclusive range of  2 to 5 , print Not Weird
If  is even and in the inclusive range of  6 to 20, print Weird
If  is even and greater than 20 , print Not Weird"""
#1<=n<=100
n=100
if n%2==0:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
         print("Weird")
    else:
         print("Not Weird")
else:
    print("Weird")