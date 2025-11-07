array = []
value = []
f = open("sport.txt", mode = "r", encoding = "cp1251")
for line in f:
    string = line.split('\t')[3].lower().split(",")
    for word in string:
        word = word.strip()
        if word == ' ' or word == '':
            continue
        if word not in array:
            array.append(word)
            value.append(1)
        else:
            index = array.index(word)
            value[index] = value[index] + 1
for i in range(3):
    k = max(value)
    firstind = value.index(k)
    first = array[firstind]
    array.pop(firstind)
    value.pop(firstind)
    print(f"{first}  {k}")
f.close()