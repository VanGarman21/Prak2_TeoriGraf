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
