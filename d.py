import sys
l1={"mumbai":"maharashtra","ranchi":"Jharkhand","ahemdabad":"gujarat"}

#st=str(raw_input("Enter a city:"))

print(l1[str(raw_input("Enter a city:"))])

#s=str(raw_input("Enter a state:"))

print l1.keys()[l1.values().index(str(raw_input("Enter a state:")))]