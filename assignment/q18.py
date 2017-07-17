class listview:
        def __init__(self,n):
                self.n = n
        def app(self,a):
                self.n.append(a)
                print(self.n)
        def dell(self,a):
                self.n.remove(b)
                print(self.n)
n = [1,2,3]
cl = listview(n)
a = int(input("enter number to be added : "))
cl.app(a)
b = int(input("enter number to be deleted : "))
cl.dell(b)

                
                
                
