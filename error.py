class DimensionError(Exception):
    def __init__(self, mensaje="", dimension="", maximo=""):
        super().__init__(mensaje)
        self.dimension = dimension
        self.maximo = maximo

    def __str__(self):
        if self.dimension or self.maximo:
            return f"Error: {self.dimension} la imagen creada en su (ancho/alto) debe ser mayor o igual a 1 y menor o igual a {self.maximo}."
        else:
            return super().__str__()