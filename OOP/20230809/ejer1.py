class Animales:
    rugidos="Grrrrrrrr!!!!"
    def __init__(self, patas, nombre, tamaño, peso):
        self.patas = patas
        self.nombre = nombre
        self.tamaño = tamaño
        self.peso = peso
    
    def sonido(self):
        print(f"El sonido del {self.nombre} haces así",self.rugidos)

    def describir(self):
        print(f"El nombre del animal {self.nombre}, tiene cantidad de {self.patas} patas, el tamaño es {self.tamaño}, tiene un peso de {self.peso}KG.")


animal = Animales(4,"Gato","Mediano", 4)

animal.sonido()
animal.describir()