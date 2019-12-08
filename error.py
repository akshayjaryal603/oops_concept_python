'''a=int(input("enter 1st number: "))
b=int(input("enter 2nd number: "))

c=a/b
print("vaue of c is : %0.1f"%c)'''
import re
p1 = re.compile(r'[\w\.-]+@[\w\.-]+')
#print(p1.match("steve@apple.com").group(0))


print(p1.search("this is abc.123@pec.edu.in and xyz.567@pec.in").group(0))
#print(r1.group(0))
print(p1.match("abc@gmail.com").group(0))
#re.findall(r'[\w\.-]+@[\w\.-]+', abc)
print(p1.findall("this is abc.123@pec.edu.in and xyz.pqr134@pec.com.in"))
print(p1.findall("Email steve@apple.com and bill@msft.com now."))

p2 = re.compile(r"[.?!$#&]+\s+")

print(p2.split("Tired? Go$ to# bed!  is& Now!! "))




