from ClaseFigura import Cuadrado, FiguraGeometrica
from ClaseGato import*
from ClaseFraccion import*
from ClasePersona import*

""" Ejemplo Gato """

gato1 = Gato("Pelusa", 1)

gato1.raza = "Siames"  # Cree un nuevo atributo SOLO para este objeto

gato1.alimentos.append("pescado")
gato1.alimentos.append("leche")

gato1.verEtapaDeVida()

gato1.alimentos = ["croquetas", "pescado"]  # Reemplaza la lista anterior

gato1.esAlimentoFavorito("pescado")  # Devuelve True

Gato.verEtapaDeVida(gato1)  # Si utilizo un metodo llamandolo a travez de la clase me pide un objeto como parametro self

print(gato1)

gato2 = Gato("Chocolate", 4, "FishCats", "Pescado", "Lasagna")

gato2.edad = 9

print(gato2.edad)  # Como se uso property no hicieron falta los '()'

print(gato2)

gato2.especie = "Ovniboro"  # Aunque se quiera cambiar no se puede ya que es un atributo de clase

gato3 = Gato("Coco", 11, "Pescado", "Pasto")

print(gato3.especie)

print("Le queda poco tiempo" if gato3.edadCritica(gato3.edad) else "Le queda tiempo")  # Condicion ternaria

del gato2  # Se llama al metodo '__del__'


""" Ejemplo Fraccion """

miFraccion = Fraccion(3, 5)
f1 = Fraccion(1, 2)
f2 = Fraccion(1, 2)
f3 = f1 + f2  # Esta es la notacion estandar para f1.__add__(f2)

print("Comi", miFraccion, "de la pizza")
print(f3)

print(f1 == f2)
print(f1 == f3)

""" Ejemplo Herencia """

numero = Decimal(1, 4)

print(numero.decimal())


""" Ejemplo Pérsona """

empleado1 = Empleado("Agustin", 24, 20000)

print(empleado1)


""" Ejemplo Cuadrado """

cuad = Cuadrado(10, 10, "Rojo")


print(cuad)
print(f"Area del cuadrado: {cuad.calcularArea()}")
