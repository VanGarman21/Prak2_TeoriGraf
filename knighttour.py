import os
import sys
import curses
from typing import List, Tuple
from colorama import init, Fore
from time import sleep
from heapq import heappush, heappop
from utils.cursor import Cursor
from utils.input import print_papan_dummy, clear, validate
from utils.papan import print_papan, update_papan

# Algoritma Warnsdorff sebagai berikut:
def algorithm(stdscr, cursor: Cursor, papan: List[List[int]], krow: int, kcol: int) -> None:
    '''
    Implementasi algoritma Warnsdorff
    '''
    # Kemungkinan langkah yang dapat dilakukan oleh kuda
    dx: List[int] = [1, 2, 2, 1, -1, -2, -2, -1]  # langkahnya ke kanan dan ke kiri sebanyak 2 langkah dan ke atas dan ke bawah sebanyak 1 langkah
    dy: List[int] = [-2, -1, 1, 2, 2, 1, -1, -2]

    langkah = 0
    for _ in range(64):
        langkah += 1
        papan[krow][kcol] = langkah
        pq: List[Tuple[int, int]] = []  # priority queue of available neighbors

        # Derajat tetangga
        for i in range(8):
            nrow: int = krow + dx[i]
            ncol: int = kcol + dy[i]

            if 0 <= nrow <= 7 and 0 <= ncol <= 7 and papan[nrow][ncol] == 0:
                # Hitung tetangga yang tersedia dari tetangga tersebut
                count = 0
                for j in range(8):
                    nnrow: int = nrow + dx[j]
                    nncol: int = ncol + dy[j]

                    if 0 <= nnrow <= 7 and 0 <= nncol <= 7 and papan[nnrow][nncol] == 0:
                        count += 1
                heappush(pq, (count, i))

        if len(pq) > 0:
            (p, m) = heappop(pq)  # posisi selanjutnya dari kuda
            krow += dx[m]
            kcol += dy[m]
            papan[krow][kcol] = 0
            update_papan(stdscr, cursor, papan)
        else:
            papan[krow][kcol] = langkah
            update_papan(stdscr, cursor, papan)


def visualize(stdscr, pos: Tuple[int, int]) -> None:
    # Bersihkan layar
    stdscr.clear()

    # Sembunyikan kursor
    curses.curs_set(0)

    # Warna
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # batas
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # sel yang telah dikunjungi
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)  # sel kuda
    curses.init_pair(4, curses.COLOR_WHITE, curses.COLOR_BLACK)  # sel yang belum dikunjungi
    curses.init_pair(5, curses.COLOR_MAGENTA, curses.COLOR_BLACK)  # progress bar

    # Dapatkan koordinat x dan y maksimum dari jendela
    max_y, max_x = stdscr.getmaxyx()

    # Papan catur 8 x 8
    papan: List[List[int]] = [[0] * 8 for _ in range(8)]

    # Inisialisasi kursor
    cursor: Cursor = Cursor(max_x, max_y)

    # Letakkan kuda di papan
    papan[pos[0]][pos[1]] = 2

    # Cetak papan catur
    print_papan(stdscr, cursor, papan, sleep_value=2.0, initialize=True)

    # Mulai algoritma Warnsdorff
    algorithm(stdscr, cursor, papan, pos[0], pos[1])

    sleep(5.0)


def main() -> None:
    # Inisialisasi colorama
    init(autoreset=True)

    while True:
        clear()

        # Cetak papan catur palsu untuk membantu pengguna menentukan posisi kuda
        print_papan_dummy()

        pos = input('Posisi kuda (baris, kolom): ')

        # Periksa input pengguna
        if validate(pos):
            break
        else:
            print(Fore.RED + 'Invalid, Coba Lagi.')
            sleep(1)

    # Mulai visualisasi
    curses.wrapper(visualize, tuple(map(int, pos.split(','))))

    clear()


if __name__ == '__main__':
    # Dapatkan ukuran terminal
    size = os.get_terminal_size()

    if size[0] < 55 or size[1] < 25:
        sys.exit('Maksimalkan jendela terminal Anda. (Req: kolom=55, baris=25)')

    main()
