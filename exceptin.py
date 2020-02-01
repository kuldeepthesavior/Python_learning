class Error(Exception):
    '''used for exception'''
    pass
class ValueSmallError(Error):
    '''used for small value exception'''


class ValueLargeError(Error):
    ''' used for large value error '''


number =20
while True:
    try:
        in_num = int(input("enter a number "))
        if in_num > number:
            raise ValueLargeError
        elif in_num < number:
            raise ValueSmallError
        break

    except ValueSmallError:
        print("enterd value is too small \n")
    except ValueLargeError:
        print("entered value is too Large")
print("this was a exceptional case practice ")
