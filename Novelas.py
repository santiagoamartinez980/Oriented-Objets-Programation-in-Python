from Libros import Libros

class Novelas (Libros):
    def __init__(self, titulo, autor, precio, genero):
        super().__init__ (titulo, autor, precio)
        self._genero = genero
    
#getters
    def getGenero(self):
        return self._genero
    
#setters
    def setGenero(self, genero):
        self._tipo = genero
    
    def calcularDescuento(self):
        descuento = self._precio * 0.15
        total = self._precio - descuento
        return total
    
    def mostrarInfo(self):
        return "titulo = "+ self._titulo + ", autor = " + self._autor +", genero = "+ self._genero + ", precio = " + str(self._precio) + ", total = " + str(self.calcularDescuento())
    
