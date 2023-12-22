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

    cursor.reset_x()
    horizontal_line(stdscr, cursor)

    if progress:
        # Mencetak progress bar
        print_progress_bar(stdscr, cursor, papan)
    
    if initialize:
        cursor.set_x(-cursor.get_x())
        cursor.set_y(-cursor.get_y())
        stdscr.addstr(cursor.get_y(), cursor.get_x(), 'initializing......', curses.color_pair(2))

    stdscr.refresh()
    sleep(sleep_value)
