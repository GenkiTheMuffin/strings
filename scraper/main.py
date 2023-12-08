status = True

def scraper(data:str):
    global status
    result =""
    for character in data:
        if character == "(":
            status = False
        elif character == ")":
            status = True
        else:
            if status:
                result += character
    return result

print(scraper("mor(sa)ho"))

        

