#mutableDJ 
fruits = ['bhushan', 'rahul', 'rushi']
fruits[2] = ['shivi']
print(fruits);

#immutalbe relation
friend = "Gopal"
print(id(friend))

friend = "Rushi"
print(id(friend))

"""you cannot change string character
name1 = "Bhushan"
name1[0] = "R"
print(name1)"""  
#assign multiple values 
x, y, z = 10, 20, 40
print(x)
print(y)
print(z)

#same value multiple variables
a = b = c = 40
print(c)
print(b)


username = "Bhushan"
print(len(username))
print(username[-0])
print(dir(username))

myList = [123, "bhushan", 3.442]
print(myList)
#dictionary
myD = {'one':'Lemon tea', 'two':'ginger tea', 'three':'black tea'}
print(myD)
l1 = [ 1, 2, 3, 4]
l2 = l1
print(l2)
l1[0] = 838
print(l2)

h2 = l1[:]
print(h2)

#import copy 
#h2 = copy.deepcopy(h1)
