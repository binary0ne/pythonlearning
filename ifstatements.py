car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == "subaru")

car = 'subaru'
print("Is car == 'audi'? I predict false.")
print(car == "audi")

str_a = "a"
str_b = "b"

print(str_a == str_b)
print(str_a != str_b)

name_a = "Johnny"
name_b = "johnny"

print(name_a == name_b)
print(name_a.lower() == name_b)

num_a = 10
num_b = 20

print(num_a > num_b)
print(num_a < num_b)
print(num_a <= num_b)
print(num_a >= num_b)

check_list = range(0,11)

print(num_a in check_list)
print(num_a not in check_list)

print(num_a in check_list and num_b in check_list)
print(num_a in check_list or num_b in check_list)