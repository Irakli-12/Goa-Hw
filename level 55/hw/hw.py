# 1) დაპრინტეთ Hello world
print("hellow world")

# 2) შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი ჯამი.
num = 2
num1 = 3
print(num + num1)

# 3) შექმენით 2 str ტიპის ცვლადი და გამოიტანეთ მათი შეერთებული ვერსია.
str1 = "hello"
str2 = "world"
print(str1 + str2) #კონკატენაცია

# 4) შექმენით 2 int ტიპის ცვლადი და გამოიტანეთ მათი განაყოფი, შემდეგ კი ახსენით რატომ გამოიტანა floatი და რა ქვია ამ convert'ს (implicit or explicit)

int1 = 8
int2 = 4
print(int1 / int2) #პას: implict

# 5) გაიხსენეთ ყველა შედარების ოპერატორი და ჩამოწერეთ ყველაზე 1 მაგალითი
# 1 - <
# 2 - >
# 3 - ==
# 4 - !=
# 5 - <=
# 6 - >=

num3 = 10
num4 = 30
print(num3 > num4)
print(num3 < num4)
print(num3 != num4)
print(num3 == num4)
print(num3 >= num4)
print(num3 <= num4)
# 6) შეურიეთ შედარების ოპერატორები და მათემატიკური ოპერაციები (მაგ: 5 + 5 == 8  + 2)
print(8 + 2 <= 30 - 20) #True
print(49 + 28 == 67)
print(3 + 6 > 3 + 3)
print(3 + 3 != 3 + 4)

# 7) გაიხსენეთ ლოგიკური ოპერატორი და ჩამოწერეთ ყველა კომბინაცია რაც საჭიროა .
print(True or False)
print(False or True)
print(True and False)
print(False and True)

# 8) შეურიეთ ერთმანეთს ლოგიკური და შედარების ოპერატორები და მოიყვანეთ 5 მაგალითი
print(True and False > True)
print(True and False == True)
print(True and False != True)

# 9) შექმენით for loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.
for i in range(10):
    print(i)

# 10) შექმენით რიცხვების list'ი, შექმენით for loop'ი list'ის რიცხვების ჯამის გამოსათვლელად.
numbers = [1, 2, 3, 4, 5]
total = 0
for number in numbers:
    total += number

print(total)

# 11) შექმენით for loop'ი თითოეული სიმბოლოს დასაბეჭდად სტრინგში -> "Hello, World!".
text = "Hello, World!"
for i in text:
    print(i)

# 12) შექმენით while loop'ი 1-დან 10-მდე რიცხვების დასაბეჭდად.

b = 1
while b <= 10:
    print(b)
    b += 1
# 13) შექმენით while loop'ი რომელიც დათვლის რიცხვებს 1დან 100მდე თუმცა გამოტოვებს რიცხვებს 50დან 60მდე.
#gasaketebeli

# 14) შექმენით while loop'ი, რომელიც დაიწყებს რიცხვების შეკრებას 1-დან, სანამ ჯამი არ გაუტოლდება 50-ს.
#gasaketebeli

# 15) შექმენით ფუნქცია რომელიც მომხმარებელს შემოატანინებს რიცხვს და დაპრინტავს ეს რიცხვი თუ იყოფა 3ზე ან 5ზე ან ორივეზე
hi123 = int(input("Enter your number: "))
print(hi123 / 3)


# 16) შექმენით ფუნქცია რომელსაც გადაეცემა რიცხვების სია,თქვენი მოვალეობააა გამოითვალე ამ სიის საშუალო არითმეტიკული. test case: [1,3,4,5,2] | output: 3
#gasaketebeli
# 17) შექმენით ფუნქცია რომელსაც გადაეცემა რაიმე string,თქვენი მოვალეობაა ყოველ მეორე ინდექსზე მყოფი ასო გახადოს დიდი (upper). test case: hello | output: HeLlO
#GASAKETEBELI 
# 18) შექმენით ფუნქცია რომელსაც გადაეცემა  რიცხვების სია,თქვენი მოვალეობააა შექმნათ ახალი სია და ამ ახალ სიაში გამოიტანოთ ყოველი რიცხვის კვადრატი (append) და შემდეგ დააბრუნეთ ახალი სია.
# test case: [3,12,5,2,6] | output: [9,144,25,4,36]
#GASAKETEBELIIIIIIII
# 19) გაიხსენეთ ყველა list'ის და string'ის მეთოდები და გამოიყენეთ თავისი მაგალითებით
list1 = ["hi", "hello", "bye"]
result = list1.append("hi1")
print(list1)
#-------------------------------#
result = list1.pop(2)
print(list1)