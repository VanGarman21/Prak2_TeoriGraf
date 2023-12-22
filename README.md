# Knight's Tour Problem

Kelompok 12:

| Nama               |  NRP        | 
|--------------------|-------------|
| M. Armand Giovani  | 5025211054  |
| Irsyad Fikriansyah R. | 5025211149  |
| Immanuel Pascanov S | 5025211257  |

## Problem
Jika sebuah bidak kuda diletakkan pada sebarang kotak untuk kemudian melakukan perjalanan (dengan cara pergerakan kuda) mengunjungi ke semua (8 x 8) kotak papan catur.

Jika diinginkan situasi bahwa kuda tsb dapat:
Mengakhiri perjalanan pada attacking square (closed tour);
Mengakhiri perjalanan di sebarang kotak (open tour);

Maka aplikasikan algoritma untuk menyelesaikan masalah di atas ke dalam sebuah program dengan menunjukkan rute perjalanan seperti gambar kanan bawah.

![image](https://github.com/VanGarman21/Prak2_TeoriGraf/assets/100523471/efb9d968-5953-4d9e-8b53-6e0962b68fd0)


## Alur Program

- Bikin Fungsi Membuat Papan Catur
```python
import curses
from .cursor import Cursor
from typing import List
from time import sleep

def horizontal_line(stdscr, cursor: Cursor) -> None:
    '''
    Mencetak garis batas horizontal.
    '''
    cursor.set_x(1) # Mengatur posisi kursor ke kolom pertama
    stdscr.addstr(cursor.get_y(), cursor.get_x(), '-' * 30, curses.color_pair(1))   # Mencetak garis batas
    cursor.set_y(1) # Mengatur posisi kursor ke baris berikutnya

def vertical_line(stdscr, cursor: Cursor, side: str) -> None:
    '''
    Mencetak garis batas vertikal di sisi kiri atau kanan.
    '''
    if side == 'L': # Mencetak garis batas di sisi kiri
        stdscr.addstr(cursor.get_y(), cursor.get_x(), '|', curses.color_pair(1))    
        cursor.set_x(1) 
    elif side == 'R':   # Mencetak garis batas di sisi kanan
        stdscr.addstr(cursor.get_y(), cursor.get_x() -2 , '|', curses.color_pair(1))    # Mengatur posisi kursor ke kolom sebelumnya lalu mencetak garis batas di sisi kanan
        cursor.set_y(1) 
    else:
        raise ValueError('Invalid value for argument \'side\'') # Jika argumen side tidak valid maka akan mengembalikan ValueError

def get_progress(papan) -> str:
    '''
    Mengembalikan kemajuan algoritma dalam bentuk persentase.
    '''
    visited_cell_count = 0   # Menghitung jumlah sel yang sudah dikunjungi
    total_cell_count = 64   # Jumlah sel pada papan
    
    for row in range(8):
        visited_cell_count += 8 - papan[row].count(0)
    progress = (visited_cell_count / total_cell_count) * 100    # Menghitung persentase kemajuan
    return f'{progress}%'

def update_papan(stdscr, cursor: Cursor, papan: List[List[int]]) -> None:
    '''
    Memperbarui tampilan papan di jendela.
    '''
    cursor.reset_x()    # Mengatur posisi kursor ke kolom pertama
    cursor.reset_y()    # Mengatur posisi kursor ke baris pertama
    print_papan(stdscr, cursor, papan, progress=True)   # Mencetak papan dengan progress bar di jendela

def print_progress_bar(stdscr, cursor: Cursor, papan: List[List[int]]) -> None:
    '''
    Mencetak progress bar di jendela.
    '''
    cursor.set_x(-cursor.get_x())   # Mengatur posisi kursor ke kolom pertama
    cursor.set_y(-cursor.get_y())   # Mengatur posisi kursor ke baris pertama
    stdscr.addstr(cursor.get_y(), cursor.get_x(), 'completed: ')    # Mencetak teks 'completed: '
    stdscr.addstr(cursor.get_y(), cursor.get_x() + 11, ' ' * cursor.max_x)  # Mencetak spasi sebanyak lebar jendela
    stdscr.addstr(cursor.get_y(), cursor.get_x() + 11, get_progress(papan), curses.color_pair(5))   # Mencetak persentase kemajuan

def print_papan(stdscr,
                cursor: Cursor,
                papan: List[List[int]],
                progress: bool = False,
                sleep_value: float = 0.5,
                initialize: bool = False,
                current_step: int = 0
                ) -> None:
    '''
    Mencetak papan di jendela.
    '''
    horizontal_line(stdscr, cursor) # Mencetak garis batas horizontal
    for row in range(8):    # Mencetak seluruh baris pada papan
        cursor.reset_x()    

        # Mencetak baris kosong
        if 0 < row <= 7: # Jika baris bukan baris pertama atau terakhir maka akan mencetak baris kosong di antara baris
            stdscr.addstr(cursor.get_y(), cursor.get_x(), '|' + ' ' * 30 + '|', curses.color_pair(1))   # Mencetak baris kosong di antara baris pertama dan terakhir
            cursor.set_y(1) 

        # Mencetak batas kiri
        vertical_line(stdscr, cursor, side='L') 

        # Mencetak seluruh kolom pada papan
        for col in range(8):
            if papan[row][col] == current_step: 
                stdscr.addstr(cursor.get_y(), cursor.get_x(), str(papan[row][col]), curses.color_pair(4))
            else:
                stdscr.addstr(cursor.get_y(), cursor.get_x(), str(papan[row][col]), curses.color_pair(2))
            cursor.set_x(1)

            if col != 8:
                cursor.set_x(3)

        # Mencetak batas kanan
        vertical_line(stdscr, cursor, side='R')

    cursor.reset_x()    # Mengatur posisi kursor ke kolom pertama
    horizontal_line(stdscr, cursor) # Mencetak garis batas horizontal

    if progress:
        # Mencetak progress bar
        print_progress_bar(stdscr, cursor, papan)
    
    if initialize:
        cursor.set_x(-cursor.get_x())
        cursor.set_y(-cursor.get_y())
        stdscr.addstr(cursor.get_y(), cursor.get_x(), 'initializing......', curses.color_pair(2))

    stdscr.refresh()
    sleep(sleep_value)
```

Penjelesan:
- Fungsi horizontal_line() digunakan untuk membuat garis horizontal pada papan catur.
- Fungsi vertical_line() digunakan untuk membuat garis vertikal pada papan catur.
- Fungsi get_progress() digunakan untuk menghitung kemajuan algoritma dalam bentuk persentase.
- Fungsi update_papan() digunakan untuk memperbarui tampilan papan di jendela.
- Fungsi print_progress_bar() digunakan untuk mencetak progress bar di jendela.
- Fungsi print_papan() digunakan untuk mencetak papan di jendela.

- Bikin Class Cursor
```python   
class Cursor(object):
    x: int
    y: int
    max_x: int
    max_y: int

    def __init__(self, max_x: int, max_y: int) -> None:
        '''
        Inisialisasi objek Cursor dengan posisi awal di tengah layar.
        '''
        self.max_x = max_x
        self.max_y = max_y
        self.x = self.max_x 
        self.y = self.max_y 

    def get_x(self) -> int:
        '''
        Mengembalikan posisi x saat ini.
        '''
        return self.x

    def get_y(self) -> int:
        '''
        Mengembalikan posisi y saat ini.
        '''
        return self.y

    def set_x(self, x: int) -> None:
        '''
        Menambahkan nilai x ke posisi x saat ini.
        '''
        self.x += x

    def set_y(self, y: int) -> None:
        '''
        Menambahkan nilai y ke posisi y saat ini.
        '''
        self.y += y

    def reset_x(self) -> None:
        '''
        Mengatur ulang posisi x ke nilai awal.
        '''
        self.x = self.max_x 

    def reset_y(self) -> None:
        '''
        Mengatur ulang posisi y ke nilai awal.
        '''
        self.y = self.max_y 
```

Penjelasan:
- Class Cursor digunakan untuk mengatur posisi kursor pada layar.   
- Fungsi __init__() digunakan untuk menginisialisasi objek Cursor dengan posisi awal di tengah layar.
- Fungsi get_x() digunakan untuk mengembalikan posisi x saat ini.
- Fungsi get_y() digunakan untuk mengembalikan posisi y saat ini.
- Fungsi set_x() digunakan untuk menambahkan nilai x ke posisi x saat ini.
- Fungsi set_y() digunakan untuk menambahkan nilai y ke posisi y saat ini.
- Fungsi reset_x() digunakan untuk mengatur ulang posisi x ke nilai awal.
- Fungsi reset_y() digunakan untuk mengatur ulang posisi y ke nilai awal.

- Bikin Fungsi Input
```python
from colorama import Fore
from os import system, name

def clear() -> None:
    '''
    Menghapus konsol
    '''
    # Untuk Windows
    if name == 'nt':
        _ = system('cls')
    # Untuk macOS dan Linux
    else:
        _ = system('clear')

def print_papan_dummy() -> None:
    '''
    Mencetak papan dummy dengan indeks untuk semua sel
    '''
    j: int = 0
    for i in range(9):
        if i != 0:
            # Mencetak baris dengan sel-sel dan pemisah
            print(
                str(j) + '   ' + Fore.YELLOW +
                '|   |   |   |   |   |   |   |   |')
            print('    ' + Fore.YELLOW + '---------------------------------')
            j += 1
        else:
            # Mencetak header kolom indeks
            print('      ' + '0   1   2   3   4   5   6   7\n')
            print('    ' + Fore.YELLOW + '---------------------------------')
    print('\n')

def validate(pos: str) -> bool:
    '''
    Memeriksa apakah input pengguna valid
    '''
    try:
        # Membagi input menjadi baris dan kolom, dan mengubahnya menjadi integer
        row, col = list(map(int, pos.split(',')))

        # Memeriksa apakah baris dan kolom berada dalam rentang 0-7
        if not 0 <= row <= 7 or not 0 <= col <= 7:
            raise ValueError()
    except:
        # Jika terjadi kesalahan saat parsing atau validasi, mengembalikan False
        return False
    return True
```

Penjelasan:
- Fungsi clear() digunakan untuk menghapus konsol pada layar.
- Fungsi print_papan_dummy() digunakan untuk mencetak papan dummy dengan indeks untuk semua sel.
- Fungsi validate() digunakan untuk memeriksa apakah input pengguna valid.

- Bikin Fungsi Untuk Menyelesaikan Masalah Knight's Tour
```python
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
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # batas
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)  # sel yang telah dikunjungi
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

    sleep(3600.0)


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

```

Penjelasan:
- Fungsi algorithm() digunakan untuk mengimplementasikan algoritma Warnsdorff.
- Fungsi visualize() digunakan untuk memvisualisasikan algoritma Warnsdorff.
- Fungsi main() digunakan untuk memulai program.

## Hasil Program


https://github.com/VanGarman21/Prak2_TeoriGraf/assets/100523471/e0e8e816-c3d8-4445-bdd1-2641a1eb4437




