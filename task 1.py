age = int(input('Введите Ваш возраст '))
def occupation(age):
 	if age<=6:
 		return('kindergarten')
 	elif age>6 and age<=18:
 		return('school')
 	elif age>18 and age<=22:
 		return('university')

 	else:
 		return('work')

print(occupation(age))
 