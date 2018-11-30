num_one=0
num_two=0
def get_summ(num_one, num_two):
    try:
        num_one = int(input("Введите первое число: "))
        num_two = int(input("Введите второе число: ")) 
        print (num_one + num_two)
    except ValueError:
        print('перехватили ошибку')
        pass

get_summ (num_one, num_two)