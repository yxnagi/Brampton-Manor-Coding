# project 1
rods = float(input("Input rods"))
print(rods)
global metres


def convertmetres(rods):
    metres = rods * 5.0292
    print("metres: ", metres)
    return metres


def convertfurlong(rods):
    furlong = rods / 40
    print("furlongs: ", furlong)
    return furlong

def convertmile(metres):
    mile = metres / 1609.34
    print("miles: ", mile)
    return mile


convertmetres(rods)
convertfurlong(rods)
convertmile(metres)

furlong = rods / 40
mile = metres / 1609.34
foot = metres / 0.3048
time = mile / (3.1 / 60)

print("")
print("conversions")
print("metres: ", metres)
print("feet: ", foot)
print("miles: ", mile)
print("furlongs: ", furlong)
print("minutes to walk: ", time)
