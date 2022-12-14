#   X_O_game

playing_field = [[" "] * 3 for i in range(3)]

print(playing_field)
def show_field():
    print("  | 0 | 1 | 2 |")
    print("  -------------")
    for i in range(3):
        print(f"{i} | {playing_field[i][0]} | {playing_field[i][1]} | {playing_field[i][2]} | ")
        print("  -------------")

show_field()

