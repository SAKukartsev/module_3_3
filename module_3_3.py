# 1.Функция с параметрами по умолчанию
print('1.Функция с параметрами по умолчанию')
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(a = 57.98,b= 'Привет', c = (True, False, 'Bool'))
print_params(b = 25)
print_params(c = [1,2,3])
# 2.Распаковка параметров
print('2.Распаковка параметров')
values_list = [25, 'hi_fi', False]
values_dict = dict( a=values_list[1], b=values_list[2], c=values_list[0])
print_params(*values_list)
print_params(**values_dict)
# 3.Распаковка + отдельные параметры
print('3.Распаковка + отдельные параметры')
values_list_2 = [675.8273645, False]
print_params(*values_list_2, 42) #Работает
