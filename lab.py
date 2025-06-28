# завдання 1
ryadok = input("input line of any characters: ")
let = 0
dig = 0
for bykva in ryadok:
    if bykva.isalpha():
        let += 1
    elif bykva.isdigit():
        dig += 1
print("letter count:", let)
print("number count:", dig)

# завдання 2
ryadok1 = input("input line of any characters: ")
shykane = input("input search symbol: ")
print(f"symbol \"{shykane}\" count: ",ryadok1.count(f'{shykane}'))

# завдання 3
ryadok2 = input("input line of any characters: ")
rev = ""
for bykv in ryadok2:
    rev = bykv + rev
print(rev)

# завдання 4
ryadok3 = input("input line of any characters: ")
shykane = input("input search word: ")
a = ryadok3.split()
c = 0
for b in a:
    if b == shykane:
        c += 1 
print(f"word \"{shykane}\" count: {c}")

# завдання 5
ryadok4 = input("input line of any characters: ")
shykane = input("input search word: ")
zamina = input("input replacement word: ")
a = ryadok4.replace(shykane, zamina)
print(f"word \"{shykane}\" reaplaced with \"{zamina}\":{a}")

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