
uppercase = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


while True:
    letter = input("enter letter")
    letter = letter.upper()
    print(letter)
    if letter in uppercase:
        position = (uppercase.index(letter)+1)
        break
    else:
        print("thats not a letter ")

if position == 1:
    print(f"{position}st")
elif position == 2:
    print(f"{position}nd")
elif position == 3:
    print(f"{position}rd")
else:
    print(f"{position}th")
