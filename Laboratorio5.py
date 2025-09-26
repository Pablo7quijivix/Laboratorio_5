#Laboratorio 05 ejercicio torre de hanoi
import time
def torres_hanoi(n, origen, destino, auxiliar, movimientos=None):
    if movimientos is None:
        movimientos = []
    if n == 1:
        movimiento = f" Mover el disco 1 de {origen} a {destino}"
        movimientos.append(movimiento)
        print(movimiento)
    else:
        torres_hanoi(n - 1, origen, auxiliar, destino, movimientos)

        movimiento = f"Mover el dico {n} de {origen} a {destino}"
        movimientos.append(movimiento)
        print(movimiento)

        torres_hanoi(n - 1, auxiliar, destino, origen, movimientos)
    return movimientos
while True:
    try:
        print("Iniciando juego Torres de Hanoi...")
        print("---Para dejar de jugar ingrese 0---")
        time.sleep(2)
        discos = int(input("\nIngrese el numero de discos para resolver el juego :D :"))
        if discos ==0:
            print("Saliendo del juego, gracias por jugar...............")
            time.sleep(2)
            break
        if discos < 0:
            print("el numero de discos debe ser mayor a 0")
            time.sleep(2)
        else:
            disco = torres_hanoi(discos, "Torre A", "Torre C", "Torre B")
            formula= (2**discos)-1
            num_movimientos = len(disco)
            print()
            print(f"___________JUEGO RESUELTO__________")
            print(f"\nSe necesita {num_movimientos} para resolver el juego")
            time.sleep(1.5)
    except ValueError:
        print("Debe ingresr datos validos :(...")
    except Exception as e:
        print(f"Ocurrio un error inesperado {e}")
        time.sleep(2)

'''
2^n - 1

'''