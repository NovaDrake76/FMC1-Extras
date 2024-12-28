#GCD

def GCD(A, B):
    #verifica se o resto é 0
    if B == 0:
        print(f"como o resto da divisão é 0, o GCD é {A}.")
        return A
    
    print(f"calculando o GCD de {A} e {B}:")
    print(f" - dividimos {A} por {B}, o quociente é {A // B} e o resto é {A % B}")
    
    return GCD(B, A % B)

print("insira o valor de A:")
A = int(input())

print("insira o valor de B:")
B = int(input())

resultado = GCD(A, B)

print(f"o GCD de {A} e {B} é {resultado}.")
