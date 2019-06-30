ip=int(input())
w,n=0,1
while(ip>0):
  print(n,end=" ")
  w,n=n,w+n
  ip-=1
