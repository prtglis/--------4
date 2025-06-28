# mystring = "123123123123"
# print(id(mystring))
# print(type(mystring)) 
# print(mystring)
# mystring1 = "hello world" 
# print(id(mystring1))
# name = "John"
# pos = "Admin"
# fullpos = name + ' ' + pos
# print(mystring.lower().startswith("hello"))
# print(mystring.count('l', 6, -1))
# # print(mystring.rfind('z'))
# print(mystring.isalnum())
# print(mystring.isalpha())
# print(mystring.isdigit())
# print("spr521".center(30,'*'))
# print(mystring1[::2])
# # newstr = mystring[0:5]
# sometitle = 'Python programming \'language\''
# name = input('enter your name: ')
# age = input('enter your age: ')
# print("Welcome to python {name} and you are {age} years old".format(name='tim', age=19))

# pi = 3.1456
# print('{0:4,2f}'.format(pi))
# Введення рядка з клавіатури
# *************************************************************
# завдання 1
# ryadok = input("input line of any characters: ")
# let = 0
# dig = 0
# for bykva in ryadok:
#     if bykva.isalpha():
#         let += 1
#     elif bykva.isdigit():
#         dig += 1
# print("letter count:", let)
# print("number count:", dig)
# # завдання 2
# ryadok1 = input("input line of any characters: ")
# shykane = input("input search symbol: ")
# print(f"symbol \"{shykane}\" count: ",ryadok1.count(f'{shykane}'))
# завдання 3
# ryadok2 = input("input line of any characters: ")
# print(ryadok2[::-1])
# завдання 4
# ryadok3 = input("input line of any characters: ")
# shykane = input("input search word: ")
# a = ryadok3.split()
# c = 0
# for b in a:
#     if b == shykane:
#         c += 1 
# print(f"word \"{shykane}\" count: {c}")
# завдання 5
# ryadok4 = input("input line of any characters: ")
# shykane = input("input search word: ")
# zamina = input("input replacement word: ")
# a = ryadok4.replace(shykane, zamina)
# print(f"word \"{shykane}\" reaplaced with \"{zamina}\":{a}")
# завдання 6
ryadok5 = input("input any sentence: ")
f = ryadok5.split()
d = ''
lenght = 0
for e in f:
    if len(e) > lenght:
        lenght = len(e)
        d =  e
print(f"the longest word is: {d}")