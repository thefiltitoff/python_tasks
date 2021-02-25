def f23(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j] == matrix[i][j-1]:
                del matrix[i][j]
                j -= 1
            j += 1
        if len(matrix[i]) == 0:
            del matrix[i]
            i -= 1
        i += 1
    i = 0
    while i < len(matrix):
        j = 0
        while j < len(matrix[i]):
            if matrix[i][j] is None:
                del matrix[i][j]
                j -= 1
            j += 1
        if len(matrix[i]) == 0:
            del matrix[i]
            i -= 1
        i += 1

    for row in matrix:
        st = row[2].split('#')
        row[2] = st[0]
        row.insert(3, st[1])

    for i in range(len(matrix)):
        buffer = matrix[i][0]
        buffer = "(" + buffer[0] + buffer[1] + buffer[2] + ") " + buffer[3] + buffer[4] + buffer[5] + "-" + buffer[6] + \
                 buffer[7] + "-" + buffer[8] + buffer[9]
        matrix[i][0] = buffer

    for i in range(len(matrix)):
        st = matrix[i][1].split(' ', 1)
        matrix[i][1] = st[0][0] + '.' + st[1]

    for row in matrix:
        arr = row[3].split(".")
        arr.reverse()
        row[3] = "/".join(arr)

    for i in range(len(matrix)):
        newmail = matrix[i][2].replace("@", "[at]")
        matrix[i][2] = newmail

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    result = []
    for j in range(num_cols):
        rowresult = []
        for i in range(num_rows):
            rowresult.append(matrix[i][j])
        result.append(rowresult)

    return result

print(f23([
    ["3110905311", "Николай Р. Дозий", "Николай Р. Дозий", "nikolaj71@rambler.ru#04.04.00"],
    ["4880298973", "Даниил З. Сомевов", "Даниил З. Сомевов", "somevov1@gmail.com#11.09.02"],
    [None, None, None, None],
    ["9473963551", "Арсен Е. Тугянц", "Арсен Е. Тугянц", "tuganz85@rambler.ru#23.02.99"],
    ["9770681108", "Евгений Ш. Цачошин", "Евгений Ш. Цачошин", "evgenij29@gmail.com#09.02.00"]
]))

print(f23([
    ["5103006150", "Ростислав У. Мудин", "Ростислав У. Мудин", "rostislav99@yandex.ru#28.06.04"],
    ["4237686713", "Мирон И. Вусифяк", "Мирон И. Вусифяк", "vusifak27@gmail.com#24.12.02"],
    [None, None, None, None],
    ["2798321040", "Глеб Р. Гериско", "Глеб Р. Гериско", "gerisko70@rambler.ru#12.06.99"]
]))
