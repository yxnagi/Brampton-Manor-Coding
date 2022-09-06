#programming challenge 2

richtervalues = [1, 5, 9.1, 9.2, 9.5]

def findenergy(richter):
    joules = 10 ** ((1.5 * richter)+ 4.8)
    return joules

def findtnt(joules):
    tnt = joules / 4184000000
    return tnt

def showlist(richtervalues):
    print(f"Richter          Joules                             TNT ")
    for x in richtervalues:
        richter = x
        joules = findenergy(richter)
        tnt = findtnt(joules)

        print(f"{richter}             {joules}            {tnt}")

def inputrichter():
    richter = int(input(f"please input a richter value: "))
    print(f"Richter Value: {richter}")
    joules = findenergy(richter)
    tnt = findtnt(joules)
    print(f"equivalence in joules: {joules}")
    print(f"equivalence in tnt: {tnt}")


if __name__ == "__main__":

    showlist(richtervalues)
    inputrichter()