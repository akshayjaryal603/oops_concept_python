def fun(a):
    letters=['a','e','i','o','u']
    if a in letters:
        return True
    else:
        return False

seq = ['a','k','s','h','a','y','e','i']
filtered = list(filter(fun,seq))
print(filtered)

result = dict()	# returns an empty dictionary  
result2 = dict(a=1,b=2)
# Displaying result  
print(result)
print(result2)

numList = [4,5, 6]
strList = ['four', 'five', 'six']

# Two iterables are passed  
result = zip(numList, strList)
# Converting itertor to set  
resultSet = set(result)
print(resultSet)
