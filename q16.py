def permutate(seq):
    """permutate a sequence and return a list of the permutations"""
    if not seq:
        return [seq]  # is an empty sequence
    else:
        temp = []
        for i in range(len(seq)):
            part = seq[:i] + seq[i+1:]
            #print i, part  # test
            for k in permutate(part):
                temp.append(seq[i:i+1] + k)
                #print k, seq[i:i+1], temp  # test
        return temp

list1 = [1, 2, 3]
for list2 in permutate(list1):
	print list2
