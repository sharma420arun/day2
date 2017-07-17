list=[(2, 5), (1, 2), (4, 4),(2,3)]
output = sorted(list, key=lambda x: x[-1])
x=len(output)
while((x-1)!=-1):
    print(output[x-1]),
    x=x-1
