import csv

def read_csv(path):
    csv_contents = []
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        next(reader)
        for row in reader:
            csv_contents.append(row)
    return csv_contents


def read_html(path):
    html = open(path)
    index = html.read()
    return index
    


def process(csv_contents, html):
    x = 1
    for row in csv_contents:
        html = html.replace("link"+str(x), row[0])
        html = html.replace("initials"+str(x), row[1])
        html = html.replace("name"+str(x), row[2])
        x = x + 1
    return html


def write_html(path, html):
    with open(path, "w") as newhtml:
        newhtml.write(html)
    return newhtml



if __name__ == "__main__":
    csv_contents = read_csv(path="south.csv")
    html = read_html(path="south.html")
    html = process(csv_contents=csv_contents, html=html)
    write_html(path="south_final.html", html=html)

