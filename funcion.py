def sumar(a, b, c):
    return a + b + c
if __name__ == "__main__":
    num1 = int(input("Ingresá el primer número: "))
    num2 = int(input("Ingresá el segundo número: "))
    num3 = int(input("Ingresá el tercer número: "))
    resultado = sumar(num1, num2, num3)
    print(f"La suma es: {resultado}")
