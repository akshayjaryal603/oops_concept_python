# remove duplicates from a list
def remove(l1):

    final = []
    for i in l1:
        if i not in final:
            final.append(i)

    return final
l1 = [10,20,10,30,45,68,68]
print(remove(l1))

# Tower of Hanoi problem using recurssion



















