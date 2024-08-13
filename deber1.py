intentos:
    intento = int(input("Adivina el número: "))
        intentos += 1

        if intento == NumeroSecreto:
            print(f"¡Felicidades! Adivinaste el número {intentos} intentos.")
            break
        else:
            distancia = abs(NumeroSecreto - intento)
            if distancia <= 5:
                print("¡caliente!")
            elif distancia <= 15:
                print("tivio.")
            else:
                print("frio.")
            
            if intento < NumeroSecreto:
                print("El número es mayor.")
            else:
                print("El número es menor.")
    
    if intentos == max_intentos:
        print(f"Lo siento, has alcanzado el número máximo de intentos. El número secreto era {NumeroSecreto}.")

adivina_numero()import random

def adivina_numero():
    NumeroSecreto = random.randint(1, 80)
    intentos = 0
    max_intentos = 10
    print("¡Bienvenido adivina el número!")
    print("Estoy pensando en un número entre 1 y 80.")

    while intentos < max_i