import random

# Clase base para unidades
class Unidad:
    def __init__(self, nombre, salud, ataque, defensa):
        self.nombre = nombre
        self.salud = salud
        self.ataque = ataque
        self.defensa = defensa

    def esta_vivo(self):
        return self.salud > 0

# Clases para tipos específicos de unidades
class Arquero(Unidad):
    def __init__(self):
        super().__init__(nombre="Arquero", salud=100, ataque=10, defensa=5)

class Infanteria(Unidad):
    def __init__(self):
        super().__init__(nombre="Infantería", salud=150, ataque=15, defensa=10)

class Caballeria(Unidad):
    def __init__(self):
        super().__init__(nombre="Caballería", salud=200, ataque=20, defensa=15)

# Clase para el ejército
class Ejercito:
    def __init__(self, nombre):
        self.nombre = nombre
        self.unidades = []

    def reclutar_unidad(self, unidad):
        self.unidades.append(unidad)

    def tiene_unidades(self):
        return any(unidad.esta_vivo() for unidad in self.unidades)

# Funciones de combate y batalla
def combate(unidad1, unidad2, archivo):
    evento = f"{unidad1.nombre} ({unidad1.salud} HP) vs " \
             f"{unidad2.nombre} ({unidad2.salud} HP)\n"
    archivo.write(evento)
    print(evento.strip())

    # Unidad 1 ataca a unidad 2
    daño1 = max(0, unidad1.ataque - unidad2.defensa)
    unidad2.salud -= daño1
    evento = f"{unidad1.nombre} hace {daño1} de daño a {unidad2.nombre}\n"
    archivo.write(evento)
    print(evento.strip())

    if unidad2.esta_vivo():
        # Unidad 2 ataca a unidad 1
        daño2 = max(0, unidad2.ataque - unidad1.defensa)
        unidad1.salud -= daño2
        evento = f"{unidad2.nombre} hace {daño2} de daño a {unidad1.nombre}\n"
        archivo.write(evento)
        print(evento.strip())

        if not unidad1.esta_vivo():
            evento = f"{unidad1.nombre} ha muerto\n"
            archivo.write(evento)
            print(evento.strip())
    else:
        evento = f"{unidad2.nombre} ha muerto\n"
        archivo.write(evento)
        print(evento.strip())

def batalla(ejercito1, ejercito2, archivo):
    ronda = 1
    while ejercito1.tiene_unidades() and ejercito2.tiene_unidades():
        evento = f"Ronda {ronda}\n"
        archivo.write(evento)
        print(evento.strip())

        unidad1 = random.choice(
            [u for u in ejercito1.unidades if u.esta_vivo()])
        unidad2 = random.choice(
            [u for u in ejercito2.unidades if u.esta_vivo()])

        combate(unidad1, unidad2, archivo)
        ronda += 1

    if ejercito1.tiene_unidades():
        resultado = f"{ejercito1.nombre} ha ganado\n"
    else:
        resultado = f"{ejercito2.nombre} ha ganado\n"
    archivo.write(resultado)
    print(resultado.strip())

# Código principal
def main():
    # Crear ejércitos
    ejercito1 = Ejercito("Ejército Rojo")
    ejercito2 = Ejercito("Ejército Azul")

    # Reclutar unidades
    for _ in range(30):
        ejercito1.reclutar_unidad(Arquero())
        ejercito2.reclutar_unidad(Arquero())
    for _ in range(30):
        ejercito1.reclutar_unidad(Infanteria())
        ejercito2.reclutar_unidad(Infanteria())
    for _ in range(30):
        ejercito1.reclutar_unidad(Caballeria())
        ejercito2.reclutar_unidad(Caballeria())

    # Iniciar batalla y guardar resultados
    with open("resultados.txt", "w") as archivo:
        archivo.write("Resultados de la batalla\n")
        batalla(ejercito1, ejercito2, archivo)

        # Guardar estado final de los ejércitos
        archivo.write("\nEstado final de los ejércitos:\n")
        archivo.write(f"{ejercito1.nombre}:\n")
        for unidad in ejercito1.unidades:
            estado = f"{unidad.nombre} ({unidad.salud} HP)\n"
            archivo.write(estado)
        archivo.write("\n")
        archivo.write(f"{ejercito2.nombre}:\n")
        for unidad in ejercito2.unidades:
            estado = f"{unidad.nombre} ({unidad.salud} HP)\n"
            archivo.write(estado)

if __name__ == "__main__":
    main()