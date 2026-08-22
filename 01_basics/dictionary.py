chai_types = {
  "Adrak": "zeaty",
  "chilly": "Hot",
  "Green": "Mild",
  "Lemon": "Good"
}
#print(chai_types);
#print(chai_types.get("Green"))

for chai in chai_types:
  print(chai, chai_types)

for key, values in chai_types.items():
    print(key, values)

if "Green" in chai_types:
  print("I have Lemon tea")
  
print(len(chai_types))  

chai_types["Earl Grey"] = "Citrus"
print(chai_types)
chai_types.popitem()
print(chai_types)
del chai_types["Green"]
print(chai_types)
squared_num = {x:x**2 for x in range(6)}
print(squared_num);
squared_num.clear()
print(squared_num)

data = {1:'Navin', 2:'rohan', 3:'sachin', 4 :'harsh'}

print(data.get(3));








