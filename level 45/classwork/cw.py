# 1) შექმენით 3 dictionary 3-3 key:value pair'ებით
headphones = {
    "color" : "rainbow",
    "light" : "Blue",
    "type" : "input and output",
}

keyboard = {
    "color" : "red",
    "light" : "green",
    "type" : "input",
}

mouse = {
    "color" : "yellow",
    "light" : "pink",
    "type" : "input",
}




# 2) გამოიტანეთ for loop'ის და .items() მეთოდის მეშვეობით ყველა dictionary'ის key'ები
for i in mouse.items():
    print(i)





# 3) გამოიტანეთ for loop'ის და .items() მეთოდის მეშვეობით ყველა dictionary'ის value'ები


for i in mouse.values():
    print(i)



#4) გამოიყენეთ list comprehension და შექმენით list'ი რომელშიც იქნება რიცხვები 1'დან 1000'მდე
list1 = [x for x in range(1, 1000)]
print(list1)






#5) გამოიყენეთ list comprehension და შექმენით list'ი რომელშიც იქნება რიცხვები 1'დან 100'მდე და ყველა რიცხვი იქნება გამრავლებული 2'ზე 
list2 = [x*2 for x in range(1, 100)]
print(list2)
