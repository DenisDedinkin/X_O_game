#   X_O_game

playing_field = [[" "] * 3 for i in range(3)]

win = [
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2)),
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
    ((0, 0), (1, 1), (2, 2)),
]

def  print_field():
    print("  | 0 | 1 | 2 |")
    print("  -------------")
    for i in range(3):
        print(f"{i} | {playing_field[i][0]} | {playing_field[i][1]} | {playing_field[i][2]} | ")
        print("  -------------")

def request_x_y():
    x, y = map(int, input("Ваш ход:  ").split())

    if 0 > x or x > 2 or 0 > y or y > 2 or x == "" or y == "":
        print("Таких координат нет ")

    return x, y


def check_win():
    for i in win:
        cell_combination = []
        for j in i:
            cell_combination.append(playing_field[j[0]][j[1]])

        if cell_combination == ["X", "X", "X"]:
            print("Выиграл Игрок 1")
            return True
        if cell_combination == ["0", "0", "0"]:
            print("Выиграл Игрок 2")
            return True
    return False

n = 1

while True:
    if check_win():
        break

    print_field()

    if n == 1:
        print("Игрок 1")
        x, y = request_x_y()
        playing_field[x][y] = "X"
        n += 1
    else:
        print("Игрок 2")
        x, y = request_x_y()
        playing_field[x][y] = "0"
        n -= 1


