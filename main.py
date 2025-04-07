from Novelas import Novelas
from Investigacion import Investigacion
from LibrosDeTexto import LibrosDeTexto

librosVendidos = []

while True:
    tit = input("ingrese el titulo ")
    aut = input("ingrese el autor ")
    pre = int(input("ingrese el precio "))
    
    opc = input("desea cambiar algun dato  ")

    if opc.lower() == "s":
        print("\n1. titulo: " + mi_libro.getTitulo())
        print("2. autor: " + mi_libro.getAutor())
        print("3. precio: " + str(mi_libro.getPrecio()))
        mi_libro.corregirDato()
    
    print ("\nSu libro es de caracter:  \n 1. Novela \n 2. Inevestigacion \n 3. Libro de texto ")
    tipo= int(input("ingrese el numero correcto "))

    if tipo==1:
        gen= input("ingrese el genero de su novela ")
        mi_libro = Novelas(tit, aut, pre, gen)
        mi_libro.calcularDescuento()
        print(mi_libro.mostrarInfo())

    if tipo==2:
        fac= input("ingrese la facultad del texto investigatvo ")
        mi_libro = Investigacion(tit, aut, pre, fac)
        mi_libro.calcularDescuento()
        print(mi_libro.mostrarInfo())
    
    if tipo==3:
        cur= input("ingrese eL curso del ibro De Texto ")
        mi_libro = LibrosDeTexto(tit, aut, pre, cur)
        mi_libro.calcularDescuento()
        print(mi_libro.mostrarInfo())
    else:
        print ("Indice no valido")

    if tipo<4: librosVendidos.append(mi_libro.mostrarInfo())

    seguir = input("\n¿Desea ingresar otro libro? (s/n): ")
    if seguir.lower() == "n":
        break

print("\nlibros vendidos hoy: ")
print("")
for i in librosVendidos:
    print(i)