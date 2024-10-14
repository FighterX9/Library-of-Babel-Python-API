import requests
from bs4 import BeautifulSoup
import re

def browse(hex,wall,shelf,volume,page): #Returns text contained from a specific location
    data = {"hex":hex,"wall":wall,"shelf":shelf,"volume":volume,"page":page}

    if int(volume) > 32 or int(volume) < 1:
        raise Exception("volume value must be between 1 and 32")

    if int(page) > 410 or int(page) < 1:
        raise Exception("page value must be between 1 and 410")

    URL = "https://libraryofbabel.info/book.cgi"
    webpage = requests.post(URL, data=data)
    soup = BeautifulSoup(webpage.content, "html.parser")
    results = soup.find(id="real")

    return results.text.strip()

def search(field,method): #Searches for location containing exact text- returns it as list
    data = {"find":field,"method":method}
    
    URL = "https://libraryofbabel.info/search.cgi"
    webpage = requests.post(URL, data=data)
    soup = BeautifulSoup(webpage.content, "html.parser")
    match_text = soup.find(
        "h3", string="exact match:"
    )
    results = match_text.parent.find("a", class_="intext") 

    # parsing out string brackets
    res1 = re.findall(r'\(.*\)', str(results))
    res2 = re.sub("\[|]", "", str(res1))
    res2 = re.sub("\'", "", str(res2))
    res3 = (res2 [2:-2])

    res4 = re.split(",",res3)
    res4[3] = int(res4[3])

    return res4

l = search("the cure to cancer is to sacrifice all million of alis debted balls ",1)

print (browse(l[0],l[1],l[2],l[3],l[4]))