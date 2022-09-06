# project 1


def convertmetres(rods):
    metres = rods * 5.0292
    return metres


def convertfurlong(rods):
    furlong = rods / 40
    return furlong


def convertmile(metres):
    mile = metres / 1609.34
    return mile


def convertfoot(metres):
    foot = metres / 0.3048
    return foot


def converttime(mile):
    time = mile / (3.1 / 60)
    return time


def run():
    rods = float(input("Input rods"))
    print(rods)

    metres = convertmetres(rods)
    furlong = convertfurlong(rods)
    mile = convertmile(metres)
    foot = convertfoot(metres)
    time = converttime(mile)

    print(f"")
    print(f"conversions")
    print(f"metres: {metres}")
    print(f"feet: {foot}")
    print(f"miles: {mile}")
    print(f"furlongs: {furlong}")
    print(f"minutes to walk: {time}")


if __name__ == "__main__":
    run()
