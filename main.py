# Игровое поле
field = [['-'] * 3 for _ in range(3)]

# Рисуем поле
def printField():
    print('  0 1 2')
    for ind, val in enumerate(field):
        print(f'{ind} {" ".join(val)}')

# Взиамодействие с игроками
def userInput(user):
    print(f'Ходит игрок {user}')
    ui = input('Введите координаты (через пробел): ')
    while True:
        ui = ui.split()
        if len(ui) != 2:
            ui = input(f'Введите две координаты через пробел: ')
            continue
        if not (ui[0].isdigit() and ui[1].isdigit()):
            ui = input(f'Это не числа. Введите числа: ')
            continue
        x, y = map(int, ui)
        if not all([0 <= x < 3, 0 <= y < 3]):
            ui = input(f'Введите координаты в диапазоне от 0 до 2: ')
            continue
        if field[x][y] != '-':
            ui = input(f'Эта клетка занята, введите свободные координаты: ')
            continue
        break
    return x, y

# Проверяем условие победы
def win(field):
    combo = [123, 456, 789, 159, 357, 147, 258, 369]
    for c in combo:
        c = list(map(int, str(c)))
        p1, p2, p3 = convert(c[0]), convert(c[1]), convert(c[2])
        if field[p1[0]][p1[1]] == '-':
            continue
        else:
            if (field[p1[0]][p1[1]] == field[p2[0]][p2[1]] == field[p3[0]][p3[1]]):
                return True
            else:
                continue
    return False

# Конвертация из деятичной в троичную (да-да, костыль)
def convert(num, to_base=3, from_base=10):
    num = int(num)
    if num == 1:
        return 0, 0
    else:
        num -= 1
    n = int(num, from_base) if isinstance(num, str) else num
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""
    while n > 0:
        n, m = divmod(n, to_base)
        res += alphabet[m]
    cxy = res[::-1]
    if len(cxy) != 2:
        cxy = "0"+cxy
    #print(cxy)
    cxy = list(map(int, cxy))
    return cxy[0], cxy[1]

# Основная функция игры
def game():
    count = 0
    while True:
        printField()
        if count == 9:
            print('Ничья. Никто не победил')
            break
        if count % 2 == 0:
            user = "X"
        else:
            user = "0"
        count += 1
        x, y = userInput(user)
        field[x][y] = user
        print(win(field))
        if win(field):
            printField()
            print(f'Выграл игрок {user}')
            print('Поздравляем! Игра окончена!')
            break

# Вызываем основную функцию игры
game()