from Arrays2D import Array2D

class LaberintoADT:
    """
    0 pasillo, 1 pared, S salida y E entrada
    pasillos es una tupla ({2,1},{2,2},{2,4},{2,4},{3,2},{4.2})
    """
    def __init__(self, rens, cols, pasillos):
        self.__laberinto=Array2D(rens, cols, '1')
        for pasillo in pasillos:
            self.__laberinto.set_item(pasillo[0], pasillo[1],'0')

    def to_string(self):
        self.__laberinto.to_string
    """
    Establece la entrada 'E' en la matriz, verfica a ren y col
    para establecer los limites
    """

    def set_entrada(self, ren, col):
        self.__laberinto.set_item(ren, col, 'E')
    """
    Establece salida deentro de los limites perifericos de la matriz
    """

    def set_salida(self, ren, col):
        self.__laberinto.set_item(ren, col, 'S')
