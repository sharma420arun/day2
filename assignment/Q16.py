fname = raw_input("enter file name :")
num_lines = 0
with open(fname,'r') as f:
    for line in f:
        num_lines +=1
print("number of lines:")
print(num_lines)

