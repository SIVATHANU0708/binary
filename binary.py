a=raw_input()
b=len(a)
p=0
for i in range(0,b):
 if(a[i]=='0' and a[i]=='1'):
  p+=1
if(n==b):
  print ("yes")
else:
  print("no")
