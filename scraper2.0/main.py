import requests

url = 'https://www.pravda.sk/'
r = requests.get(url)
data = r.text
status = True

def scraper(data:str):
    global status
    result =""
    for character in data:
        if character == "<":
            status = False
        elif character == ">":
            status = True
        else:
            if status:
                result += character
    return result

print(scraper(data))