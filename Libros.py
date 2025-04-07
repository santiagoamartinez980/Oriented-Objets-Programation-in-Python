
class Libros:

    def __init__(self, titulo, autor, precio):
        self._titulo = titulo
        self._autor = autor
        self._precio = precio
#getters
    
    def getTitulo(self):    
        return self._titulo

    def getAutor(self):
        return self._autor
    
    def getPrecio(self):  
        return self._precio
    
#setters    
    def setPrecio(self,precio):
        self._precio= precio

    def setTitulo(self,titulo):
        self._titulo= titulo

    def setAutor(self,autor):
        self._autor= autor

    def calcularDescuento(self):
        pass

    def corregirDato(self):
        print("\ncorregir \n 1. titulo \n 2. autor \n 3. precio \n 4. tipo ")
        opc=int(input("ingrese el numeral de opcion a corregir "))
        if opc== 1:
            nuevo =input("ingrese el valor nuevo ")
            self.setTitulo(nuevo)
        
        elif opc== 2:
            nuevo =input("ingrese el valor nuevo ")
            self.setAutor(nuevo)
        
        elif opc== 3:
            nuevo =int(input("ingrese el valor nuevo "))
            self.setPrecio(nuevo)
        else:
            print("numeral no valido")
    