"""OneTwo"""
def onetwo(s):
    """main function"""
    if s == 1:
        return '1'
    if s == 2:
        return '2'
    return onetwo(s - 1) + onetwo(s - 2)

print(onetwo(int(input())))
