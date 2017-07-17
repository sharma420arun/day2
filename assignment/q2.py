my_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
rows=int(raw_input("Enter the no. of lines to print"))
a=0
print "yes"
for x in range(rows):
  for y in range(x+1):
      if y==x:
          print str(my_list[a])
          a=a+1
      else:
          print str(my_list[a]),
          a=a+1 
