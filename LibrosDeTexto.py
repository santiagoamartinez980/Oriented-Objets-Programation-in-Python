from Libros import Libros

class LibrosDeTexto (Libros):
    def __init__(self, titulo, autor, precio, libro_curso):
        super().__init__ (titulo, autor, precio)
        self._libro_curso = libro_curso

#getters
    def getCurso(self):
        return self._libro_curso
    
#setters
    def setCurso(self, libro_curso):
        self._libro_curso = libro_curso

    def calcularDescuento(self):
        descuento = self._precio * 0.4
        total = self._precio - descuento
        return total
    
    def mostrarInfo(self):
        return "titulo = "+ self._titulo + ", autor = " + self._autor + ", curso = "+ self._libro_curso + ", precio = " + str(self._precio) + ", total = " + str(self.calcularDescuento())