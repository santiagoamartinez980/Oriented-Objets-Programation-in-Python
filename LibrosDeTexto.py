from Libros import Libros

class LibrosDeTexto (Libros):
    def __init__(self, titulo, autor, precio, curso):
        super().__init__ (titulo, autor, precio)
        self._curso = curso

#getters
    def getFacultad(self):
        return self._curso
    
#setters
    def setTipo(self, curso):
        self._curso = curso

    def calcularDescuento(self):
        descuento = self._precio * 0.4
        total = self._precio - descuento
        return total
    
    def mostrarInfo(self):
        return "titulo = "+ self._titulo + ", autor = " + self._autor + ", curso = "+ self._curso + ", precio = " + str(self._precio) + ", total = " + str(self.calcularDescuento())