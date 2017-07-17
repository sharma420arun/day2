def main():
   import re
   lam=raw_input("Enter password")
   validate(lam)
       
def validate(lam):
   if len(lam)<6 or len(lam)>16:
      print("not Valid")
   else:
       if (bool(re.search(r'[a-z]',lam))) and (bool(re.search(r'[A-Z]',lam))) and (bool(re.search(r'[0-9]',lam))) and (bool(re.search(r'[$#@]',lam))):
           print("Valid")
       else:
           print("Not Valid")

main()
 
