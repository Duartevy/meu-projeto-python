# Função para contar quantas vezes a letra 'a' aparece em uma string
def contar_a(string):
    # Conta a ocorrência de 'a' minúscula ou 'A' maiúscula
    return string.lower().count('a')

# Solicita uma string ao usuário
texto = input("Informe uma string: ")
quantidade = contar_a(texto)

# Exibe a quantidade de vezes que a letra 'a' aparece na string
if quantidade > 0:
    print(f"A letra 'a' aparece {quantidade} vezes na string informada.")
else:
    print("A letra 'a' não aparece na string informada.")
