import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"

def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def find(lookingfor):
    open_tr = html.find('<tr>', i)
    close_tr = html.find("</tr>", open_tr)
        
    newstring = html[open_tr:close_tr]
    start = newstring.find(lookingfor)
    end = newstring.find('</', start)
    returnvalue = (newstring[start+len(lookingfor):end])
    if "title" in lookingfor:
        start = (returnvalue.find('/">'))
        returnvalue = returnvalue[start+3:]
    if "artist" in lookingfor:
        start = (returnvalue.find('/">'))
        returnvalue = returnvalue[start + 3:]

    return returnvalue, close_tr

def find_all_values():
    position, close_tr = find('"position">')
    title, close_tr = find('class="title">')
    artist, close_tr = find('class="artist')

    return position, title, artist, close_tr


    
if __name__ == "__main__":
    list = []
    i = 0
    x = 0
    html = scrape(url)
    while x < 10:
        position, title, artist, close_tr = find_all_values()
        print(position)
        templist = ([position, title, artist])
        list.append(templist)
        i = close_tr
        x = x + 1
    print(f"{'Position':15}{'Name':30}{'Artist':30}")
    print("-----------------------------------------------------")
    for x in list:
        print(f'{x[0]:5}{x[1]:^30}{x[2]:>30}')



