def capital_indexes(string):
    list = []
    for index,letter in enumerate(string):
        if letter.isupper():
            list.append(index)
    return list
string="HeLlO"
print(capital_indexes(string))