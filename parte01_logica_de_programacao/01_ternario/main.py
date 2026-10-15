# declaração de variaveis 
nome = input ("informe seu nome").strip().title()
idade = int(input("informe sua idade"))

# operador ternario
print(f"{nome}{" é maior de idade" if idade >=18 else " é menor de idade"}.") 
