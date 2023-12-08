# Criar vetores 
idades = []
alturas = []

# Pedir para usuario inserir a informação
for _ in range(5):
    idade = int(input("Insira sua idade: "))
    altura = float(input("Insira sua altura (em metros): "))

# Inserir informações nos respectivos vetores
    idades.extend([idade])

    alturas.extend([altura])

# Imprimir listar na ordem inversa
print(idades[::-1])
print(alturas[::-1])