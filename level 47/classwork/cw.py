# 1) ჩამოთვალეთ ყველა დღეს ნასწავლი error'ის ტიპი და ახსენით რა რა შემთხვევაში გამოდის

print("nameerror" + " " + "syntaxerror" + " " + "keyerror")
#Name Error მაშინ როცა ცვლადის სახელი პრინტში არასწორად დავწერეთ
#Syntax Error მაშინ როცა არასწორად ვწერთ რაიმეს კოდში (მაგ:პრინტის დაწერის შემდეგ პრჩხილები დაგვავიწყდა)
#Key Error მაშინ როცა შეცდომა არის Dictionary-ში


# 2) დაწერეთ ისეთი კოდი სადაც იქნება NameError და გაუმკლავდით try/except'ით

name = "irakli"
try:
    print(name1)
except:
    print("check variable name")

#3) დაწერეთ ისეთი კოდი სადაც იქნება IndexError და გაუმკლავდით try/except'ით

list1 = ["hello", "hi", "bye"]
try:
    print(list1[3])
except:
    print("check index which you typed in 'print'")

#4) კომენტარებით ახსენით რაში გვადგება try/except

#Try/exept შეგვილია გამოვიყენოთ კოდების გამოსასწორებლად