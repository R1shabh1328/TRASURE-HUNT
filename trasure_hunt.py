print("trasure isalnd....try to win")

print("start")
print("2 ways in front of you...choose left or right")

ways = input("left or right\n")
lower_ways = ways.lower()

if lower_ways == "left":
    print("congrats ur at lvl 2")
else:
    print("fire..pooff!!! ur dead")

print("there is a lake in front of you")
print(" u gonna swim or wait for a boat")
    
lake = input("swim or wait\n")
lower_lake = lake.lower()

if lower_lake == "wait":
    print("congrats ur at lvl 3")
else:
    print("lol..u drowned...dead")
    
print("there are three doors red,blue,green...what do you choose??")

doors = input("red,blue or green\n")
lower_doors = doors.lower()

if lower_doors == "red":
    print("u mom just whooped ur ass..and ur dead")
elif lower_doors == "green":
    print("power cut..game over")
elif lower_doors == "blue":
    print("you win and ur prize is a PS5")
else:
    print("invalid entry...ur dead")
