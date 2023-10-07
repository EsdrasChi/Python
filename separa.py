# Inicialize as listas para os números pares e ímpares
numeros_pares = []
numeros_impares = []

# Solicite ao usuário que insira 10 valores
for i in range(10):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    
    # Verifique se o número é par ou ímpar e adicione-o à lista apropriada
    if valor % 2 == 0:
        numeros_pares.append(valor)
    else:
        numeros_impares.append(valor)

# Crie uma tupla com os números ímpares
tupla_impares = tuple(numeros_impares)

# Calcule a quantidade de números pares e ímpares
quantidade_pares = len(numeros_pares)
quantidade_impares = len(numeros_impares)

# Calcule a soma de todos os números pares e ímpares
soma_pares = sum(numeros_pares)
soma_impares = sum(numeros_impares)

# Exiba os resultados na tela
print("Números pares:", numeros_pares)
print("Números ímpares:", tupla_impares)
print("Quantidade de números pares:", quantidade_pares)
print("Quantidade de números ímpares:", quantidade_impares)
print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)
