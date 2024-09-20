# Função para verificar se o número pertence à sequência de Fibonacci
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False

# Solicita o número ao usuário
numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verifica se o número pertence à sequência de Fibonacci
if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
