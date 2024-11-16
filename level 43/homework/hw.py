#2) შექმენით 5 dictionary (თქვენ რაზეც გინდათ) და ყველას მინიმუმ ჰქონდეს 5 key:value pair
keyboard = {
    "light": "colorfull",
    "color": "rainbow",
    "type": "input",
    "pad": "red",
    "size": "75%"
}
mouse = {
    "light": "red",
    "color": "blue",
    "pad": "rainbow",
    "pad size": "65%",
    "switches": "colorfull"
}
camera = {
    "color": "black",
    "size": "little",
    "type": "input",

}
Pc = {
    "color":"colorfull",
    "button1": "turn on Pc",
    "button2":"change colors",
    "button3": "USB",
    "case color": "black"
}
printer = {
    "color1": "black",
    "color2": "also black",
    "power1": "multiple colors",
    "power2": "printing images",
    "size": "big"
}






#3) გამოიტანეთ ამ 5'ივე dictionary'ს key list'ები
for i in keyboard.keys():
    print(i)

for i in mouse.keys():
    print(i)

for i in camera.keys():
    print(i)

for i in Pc.keys():
    print(i)

for i in printer.keys():
    print(i)

#4) გამოიტანეთ ამ 5'ივე dictionary'ს value list'ები
for i in keyboard.values():
    print(i)


for i in mouse.values():
    print(i)


for i in camera.values():
    print(i)


for i in Pc.values():
    print(i)

for i in printer.values():
    print(i)



#5) გამოიტანეთ ამ 5'ივე dictionary'ს key:value pair list'ები
for i in keyboard.items():
    print(i)

for i in mouse.items():
    print(i)

for i in camera.items():
    print(i)

for i in Pc.items():
    print(i)

for i in printer.items():
    print(i)
