from error import DimensionError

class Foto:
    MAX = 2500

    def __init__(self, alto: int, ancho: int, ruta: str):
        self._alto = alto
        self._ancho = ancho
        self.ruta = ruta

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, valor):
        if valor < 1 or valor > self.MAX:
            try:
                DimensionError("El valor del alto es invalido", dimension="alto", maximo=self.MAX)
            except DimensionError as a:
                print(a)
        else:
            self._alto = valor

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, valor):
        if valor < 1 or valor > self.MAX:
            try:
                DimensionError("El valor del ancho es invalido", dimension="ancho", maximo=self.MAX)
            except DimensionError as b:
                print(b) 
        self._ancho = valor
        
        
        
if __name__ == "__main__":
    Foto(0,100, "C:\Users\ztyle\Dropbox\BootCamp\Desarrollo\Modulo_4\Desafio4\image0.jpeg")