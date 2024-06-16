def mid(string):
    if len(string) % 2 == 0:
        result =""
        return result
    else:
        result = len(string)//2
        return string[result]
        
print(mid("abc"))
print(mid("aaaa"))