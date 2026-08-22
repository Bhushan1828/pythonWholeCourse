tea_types = ("black", "Green", "Oolang", "black")
print(tea_types);
print(tea_types[1])
#tea_types[0] = "lemon"
#tuple object does not support item assignment beacuse of tuple is immutable we cannot change it
print(len(tea_types)) 

if "Green" in tea_types:
  print("I have a green tea")

print(tea_types.count)
new_tea = ("lemon","adark","ilaichi", "lemon")
all_tea = tea_types + new_tea
print(all_tea)
print(tea_types.count("Green"))
print(new_tea.count("lemon"))
print(tea_types)
print(type(tea_types))