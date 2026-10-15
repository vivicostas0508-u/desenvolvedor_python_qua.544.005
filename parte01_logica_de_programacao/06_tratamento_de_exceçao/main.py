
# traatamento de exceção
try:
    nome = input ("informe seu nome").strip().title()
    idade = int(input("informe sua idade"))

    print(f"Nome do usuário: {nome}")
    print(f"Idade do usuário: {idade} anos.")
except Exception as e:
    print(f"Não foi possivel executar a ação! {e}")
finally:
    print("Programa finalizado com sucesso!")