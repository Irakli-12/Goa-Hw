# შექმენით list'ი და გამოიყენეთ ყველა თვისება თუ ფუნქცია რაც შეიძლება list'ებთან გამოვიყენოთ
list1 = ["str", "str1", "str2"]
for i in list1:
    if i == "str":
        print(i)

# შექმენით tuple'ი და გამოიყენეთ ყველა თვისება თუ ფუნქცია რაც შეიძლება tuple'ებთან გამოვიყენოთ
tuple1 = ("hi", "hello")

for i in tuple1:
    if i == "hi":
        print(i)

# 4) შექმენით set'ი და გამოიყენეთ ყველა თვისება თუ ფუნქცია რაც შეიძლება set'ებთან გამოვიყენოთ
set1 = {"asra", "asraw", "asdwq", "asdqi"}
function1 = set1.pop()
print(set1)