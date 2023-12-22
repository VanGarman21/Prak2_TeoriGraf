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
