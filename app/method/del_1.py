def sp_tan(a):

    b = str.maketrans('', '', '('')'','"'")

    x = a.translate(b)

    return x


def sp_tan2(a):


    b = str.maketrans('\\r\\n', '<br>', '('')'','"'")

    x = a.translate(b)


    return x


