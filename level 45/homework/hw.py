# 2) შექმენით dictionary 10 key:value pair'ით და გამოიტანეთ ყველა key .items() მეთოდის გამოყენებით
headphones = {
    "color1": "green",
    "color2": "red",
    "color3": "blue",
    "color4": "yellow",
    "color5":"orange",
    "color6": "aqua",
    "color7": "black",
    "type": "input",
    "all color": "rainbow",
    "light": "also rainbow"
}

for i in headphones.keys():
    print(i)

# 3) შექმენით dictionary 10 key:value pair'ით და გამოიტანეთ ყველა value .items() მეთოდის გამოყენებით

for i in headphones.values():
    print(i)

# 4) list comprehension'ის მეშვეობით შექმენით list'ი რომელშიც იქნება 2'ზე გაყოფილი და 1'ით მეტი რიცხვები 50'დან 100'მდე (მაგ: 50 --> 50 / 2 + 1 = 26) 

list1 = [x//2+1 for x in range(50, 100)]
print(list1)

# 5) list comprehension'ის მეშვეობით შექმენით list'ი რომელშიც იქნება 2'ზე გამრავლებული და 1'ით მეტი რიცხვები 50'დან 100'მდე (მაგ: 50 --> 50 * 2 + 1 = 101)

list2 = [x*2+1 for x in range(50, 100)]
print(list2)


