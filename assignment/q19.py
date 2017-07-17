class Demo:
    global x
    def accept(self):
	self.x=str(raw_input("enter a string:"))
    def display(self):
	print(self.x)
	

c=Demo()
c.accept()
c.display()
