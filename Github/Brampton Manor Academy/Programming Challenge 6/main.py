
def find_order_and_topleft():
    order = int(input(f"please input the order of the square "))
    top_left = int(input(f"please input the top left of the square "))
    return order, top_left

def make_square(order, top_left):
    temp = top_left
    main = []
    z = 0
    for x in range(order+1):
        if z == 0:
            pass
        else:
            main.append(row)
        row = []
        if z == 0:
            pass
        else:
            temp = temp + 1
        z = z + 1
        for y in range(order):
            if temp > order:
                temp = 1
            else:
                pass
            row.append(temp)
            if temp == order:
                temp = 1
            else:
                temp = temp + 1
    return main

if __name__ == "__main__":
    order, top_left = find_order_and_topleft()
    main = make_square(order, top_left)
    for row in main:
        row = [str(each) for each in row]
        print(" ".join(row))

