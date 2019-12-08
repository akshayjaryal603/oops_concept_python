import re
'''
abc='a+b+c*'
xyz='ddddddaaaabbbcccff'
print(re.search(abc,'dddd abbbbccc dd is the string aaaabbbccc'),'\n')
#print()
print(re.match(abc,'abbbbccc dd is the string aaaabbbccc'))

pat2 = "(\w+)@((\w+\.)+(com|org|net|edu|in))"
r2 = re.search(pat2,"abc123@cs.pec.edu.in")

print(r2.group(0))
print(r2.group(1))

print(r2.group(2))
print(r2.group(3))
print(r2.group(4))
#print(r2.group(5))

print(r2.groups())
'''

pat3 ="(?P<name>\w+)@(?P<host>(\w+\.)+(com|org|net|edu))"
r3 = re.search(pat3,"xyz@cs.iit.edu")

print(r3.group('name'))
print(r3.group('host'))
#for spliting
print(re.split("\W+", "This123... is a test, short and sweet, of split()."))
#for substitution
print(re.sub('(blue|white|red)', 'yellow', 'blue socks and red shoes and white'))

print(re.findall("\D+","12 dogs,11 cats, 1 egg"))   #\D Non digit

print(re.findall("\d+","12 dogs,11 cats, 1 egg"))   #\d match digits

print(re.findall("\s+","12 dogs,11 cats, 1 egg"))   #\s check whitespace
print(re.findall("\S+","12 dogs,11 cats, 1 egg"))   #\S check non-whitespace

print(re.findall("^ the"," the 12 dogs,11 cats, 1 egg"))   #^ check element in the starting
print(re.findall("clock$","12 dogs,11 cats, 1 egg clock"))   #$ chcek element in the end






