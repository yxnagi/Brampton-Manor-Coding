import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def teamlistmaker(csv_contents):
    teamlist = []
    for currentrow in csv_contents:
        x = currentrow[1]
        if x not in teamlist:
            teamlist.append(x)
    return teamlist

def whowon(row):
    if row[5] == "H":
        winningteam = row[1]
    elif row[5] == "A":
        winningteam = row[2]
    else:
        winningteam = "draw"
    return winningteam

def gdcalculator(row):
    gd = int(row[3]) - int(row[4])
    return gd

def gdcalculatoraway(row):
    gdaway = int(row[4]) - int(row[3])
    return gdaway
    
def goaltable(teamlist, file_contents):
    goaltable = []
    for x in teamlist:
        goaltable.append([x,0,0])
    for row in file_contents:
        winningteam = whowon(row)
        if winningteam == "draw":
            drawteam1 = row[1]
            drawteam2 = row[2]
            for y in goaltable:
                if y[0] == drawteam1:
                    y[1] = y[1] + 1
                if y[0] == drawteam2:
                    y[1] = y[1] + 1
        else:
            for y in goaltable:
                if y[0] == winningteam:
                    y[1] = y[1] + 3
        gd = gdcalculator(row)
        gdaway = gdcalculatoraway(row)
        for y in goaltable:
            if y[0] == row[1]:
                y[2] = y[2] + gd
        for y2 in goaltable:
            if y2[0] == row[2]:
                y2[2] = y2[2] + gdaway
    return goaltable

if __name__ == "__main__":
    file_contents = read_csv(csv_file)
    teamlist = teamlistmaker(file_contents)
    goaltable = goaltable(teamlist, file_contents)
    goaltable.sort(key=lambda x: x[1], reverse=True)
    x = 0
    for row in goaltable:
        if x == 0:
            x = x + 1
            savedrow = row
            pass
        else:
            if savedrow[1] == row[1]:
                if savedrow[2] < row[2]:
                    temprow = savedrow.copy()
                    savedrow[0],savedrow[1],savedrow[2] = row[0],row[1],row[2]
                    row[0],row[1],row[2] = temprow[0],temprow[1],temprow[2]
                    savedrow = row
            else:
                savedrow = row
    print(f"{'Team':26}{'Points':10}{'Goal Difference':20}")
    print("-----------------------------------------------------")
    for x in goaltable:
        print(f'{x[0]:20}{x[1]:10}{x[2]:>15}')

    
