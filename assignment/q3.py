def check():
        def __init__(self):
                self.n =[]
        def add(self,a):
                return self.n.append(a)
        def remove(self,b):
                self.n.remove(b)
        def dis(self):
                return (self.n)

obj = check()

choice =1
while choice!=0:
        print("0. Exit")
        print("1.add")
        print("2.delete")
        print("3.display")
        choice = int(raw_input("enter choice: "))
        if choice ==1:
                 n = int(raw_input("enter number to append :"))
                 obj.add(n)
                 print("List : ", obj.dis())
        elif choice ==2:
                n = int(raw_input("enter number to remove: "))
                obj.remove(n)
                print("list: ",obj.dis())
        elif choice ==3:
                print("list :",obj.dis())
        elif choice == 0 :
                print("exiting")
        else:
                print("invalid choice")

print()
                
                
                
