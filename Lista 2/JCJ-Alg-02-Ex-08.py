# Aluno: Jairo Caetano Junior
# Curso: Algoritmo - BCC - 1º Fase - 2024/01
number = int(input("Digite um número de até 3 dígitos: "))
hundred = number // 100
ten = (number % 100) // 10
unit = number % 10
M = (unit * 100) + (ten * 10) + hundred
print(M)
