print("==> NUMEROS POR EXTENSO <==")
data = int(input("Digite um numero de 0 a 20: "))

numeros = ("zero", "um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

escrito = numeros[data]
print(f'Você digitou {escrito}!')

