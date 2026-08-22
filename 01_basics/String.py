name = "Bhushan Ingle"
print(name[1:9])
slice_name = name[0:7]
print(slice_name)
num_list = "0123456789"
print(num_list[3:])
print(num_list[:7])
print(num_list[0:7:3])
print(name.upper());
#strip is use to remove spaces between strings
name1 = "     Bhushan    "
print(name1)
print(name1.strip())
mobile = "Samsung Galaxy"
print(mobile.replace("Samsung Galaxy", "Iphone17"))
print(mobile)
#use a split keyword for doing operation
friends = "Gopal, Rushi, shubham, shubham, Tejas, Adarsh"
print(friends.split(" , "))
#we use find for serarching string where it is
print(friends.find("Tejas"))
print(friends.count("shubham"))
phone_type = "Samsung Galaxy"
quantity = 2
ordered = "I ordered {} top model of {} phones"
print(ordered.format(quantity, phone_type))

#join
chai_variety = ["Lemon", "masala", "Ginger"]
print("-".join(chai_variety));
chai = "masala chai"
print(len(chai));
for letter in chai:
  print(letter)
  chai = "he said, \"Your Friends are so real and humbel\" "
path = "c:\\user\\pwd"
print(path)