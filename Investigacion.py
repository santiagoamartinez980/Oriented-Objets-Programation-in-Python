from Libros import Libros

class Investigacion (Libros):
    def __init__(self, titulo, autor, precio, facultad):
        super().__init__ (titulo, autor, precio)
        self._facultad = facultad

#getters
    def getFacultad(self):
        return self._facultad
    
#setters
    def setTipo(self, facultad):
        self._facultad = facultad

    def calcularDescuento(self):
        descuento = self._precio * 0.25
        total = self._precio - descuento
        return total
    
    def mostrarInfo(self):
        return "titulo = "+ self._titulo + ", autor = " + self._autor + ", facultad = "+ self._facultad + ", precio = " + str(self._precio) + ", total = " + str(self.calcularDescuento())