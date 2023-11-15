#   Python Maze Solver - Solves mazes inside text files.
#   Copyright (C) 2023  Kerem Biçen

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import time

with open(input("dosya: ")) as dosya:
    labirent = [list(line) for line in dosya.read().splitlines()]

pos = [len(labirent) - 2, labirent[len(labirent) - 2].index("S")]

def main():
    while True:
        print_board()

        time.sleep(0.1)

        if check_end():
            labirent[pos[0]][pos[1]] = "X"
            print_board()
            print("\nBaşarılı!")
            return

        if check_replace(" ", "X"):
            check_replace("X", "Y")

def print_board():
    os.system("clear")
    for line in labirent:
        print("".join(line))

def check_end():
    if labirent[pos[0] + 1][pos[1]] == "E":
        return True
    elif labirent[pos[0]][pos[1] + 1] == "E":
        return True
    elif labirent[pos[0] - 1][pos[1]] == "E":
        return True
    elif labirent[pos[0]][pos[1] - 1] == "E":
        return True
    else:
        return False

def check_replace(a, b):
    if labirent[pos[0] + 1][pos[1]] == a:
        labirent[pos[0]][pos[1]] = b
        pos[0] += 1
    elif labirent[pos[0]][pos[1] + 1] == a:
        labirent[pos[0]][pos[1]] = b
        pos[1] += 1
    elif labirent[pos[0] - 1][pos[1]] == a:
        labirent[pos[0]][pos[1]] = b
        pos[0] -= 1
    elif labirent[pos[0]][pos[1] - 1] == a:
        labirent[pos[0]][pos[1]] = b
        pos[1] -= 1
    else:
        return True

if __name__ == "__main__":
    main()
