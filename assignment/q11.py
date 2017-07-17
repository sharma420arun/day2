numbers = raw_input("Enetr nos. with , ").split(",")
           
b = [int(x) for x in numbers]
flag=True
print len(b)
for i in range(1,len(b)):
   if i!=len(b)-2 and i!=len(b)-1:
       if (int(b[i])+int(b[i-1]))!=int(b[i+1]):
           flag=False
if flag==True:
   print "Yes"
else: print"NO"
