#FMC1 - Unidade 2 (atividade extra)

#cifra de Cesar, nós mudamos a posição das letras do alfabeto (26 letras) por um certo número N de casas.

def caesar(word, N):
  word = word.upper()
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  result = ""

  for char in word:
    #percorre cada letra da palavra, e adiciona a letra que está N posições a frente no alfabeto
    result += alphabet[(alphabet.index(char) + N) % 26]

  print(result)

print("insira a palavra: ")
word = input()
print("desencriptar por quantas casas? ")
N = int(input())

caesar(word, N)
