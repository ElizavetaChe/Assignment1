str1=input('Введите строку: ')
str2=input('Введите другую строку: ')

def check_if_str(str1, str2) :
    if not type(str1) == str and type(str2) == str:
        return('0')

    if str1 == str2:
        return 1
    elif len(str1) > len(str2):
        return 2
    elif str2 == 'learn':
        return 3
    



print(check_if_str(str1, str2))