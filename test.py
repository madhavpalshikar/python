import math

print("Hello World")
print(math.gcd(3,6))

mystr = "string"
numb = 100
flt = 10.34234
mylist = [1,23,44,"string", 3.44]
mytuple = (1,23,44,"string", 3.44)
mydict = {"one":"1","two":"2","three":"3"}
#comment
'''
THis is multiline comment
'''
print(mylist)
print(mytuple)
print(mydict)

# type() to get the type of variable
print(type(mylist))

#variable conversions = Type casting
newint = int(flt)
print(newint)
print(str(numb)) 
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("r","--"))
print(mystr[0])
print(mystr[2:4])
print(mystr * 2)
print(mystr + mystr)
name1 = "ram"
name2 = "laxman"
temp = "This is a {0} and he is a good boy name {1}".format(name1, name2)
print(temp)
temp = "This is a {1} and he is a good boy name {0}".format(name1, name2)
print(temp)
temp = f"This is a {name1} and he is a good boy name {name2}"
print(temp)
print(3**2)
print(3//2)
print(3%2)
'''
Python Collections
1. List
2. Tuple
3. Set
4. Dictionary
'''

#List
lst = [1,2,3,4,5,6]
lst[2] = 45
print(lst[2], lst[2:5])
print(len(lst))
lst.append(100)
lst.insert(2,66)
lst.remove(66)
lst.pop()
del lst[2]
lst.clear()
var = lst
print(lst)

#Tuple
tpl = (1,2,3,4,5,6)

var = tpl[2:4]
var = tpl.count(3) #counts the number of appearence of item in tuple
#converting tuple to list
#var = list(tpl) 
print(var)

#Set
s1 = {1,2,3,4,3,2,4,55,2,2,2,2,3,4,444,3} #sets will not keep duplicates , only unique values
s1.add(100)
s1.update([22,33,44,55])
print(s1)
s1.remove(1)
s1.discard(2344) # it will not throw error if value is not present
#.pop .clear del union intersection
print(len(s1))

#dictionary
mydict = {
    "Name": "Harry",
    "age": 22,
    "class": "A"
}
#can use del pop clear  
print(mydict["age"])
print(len(mydict))

age = input("Enter your age")
age = int(age)
#conditional statements
if(age>18):
    print("You can drive a car")
elif(age==18):
    print("Awesome teen")
else:
    print("You can not drive a car")

#loops
for i in range(0,age):
    print(i)

for item in mylist:
    print(item)

i = 0
while(i<age):
    i = i + 1    
    if i==18:
        break
    if i < 5:
        continue
    print(i)

#functions
def greet():
    print("Good Morning")

greet()
greet()

def sum(a,b):
    return a+b

d = sum(44,34)
print(d)

