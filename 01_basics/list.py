l1 = [1, 2, 3, 4, 5]
l2 = l1[:]
#l1 = 'bhushan'

l1[1] = 99
print(l1)
print(l2); 
print(l1 is l2)
#0, 1 indexing
name = ['shilu', 'pradnya', 'mahadev', 'harshal']
print(name[1:1])
print('shilu' in name)
teas = ['black', 'lemon', 'white', 'green'];
teas[1:1] = ['black+lemon', 'black+lemon']
print(teas)
teas[1:3] = [  ]
print(teas)
for tea in teas:
  print(tea, end="_")
if "chai" in teas:
  print("I have a chai")
teas.append("chai")
print(teas)
if "chai" in teas:
  print("I have a chai")
#pop is use to remove last value from a given list  
teas.pop()
print(teas) 
#by using remove method we easily remove a particular value from a list
teas.remove('black');
print(teas)

squared = [x**2 for x in range(10)]
print(squared)

cube_num = [y**3 for y in range(5)];
print(cube_num)

marks = [3, 4, 5, "bhushan", True, 7, 8, 9, 10, 11, 12, 13, 14, 15, 46]

if "bhushan" in marks:
  print("Yess")
else:
  print("No")
  
print(marks[0:8])
#for jumping like 2 to 4 
print(marks[0:12:2]) 
  