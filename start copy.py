import sys, time #importa o módulo sys e time
from src.banner import banner #importa o banner do programa
from src.cls import cls

cart =[]

def menu():
    option = 0 #variável que armazena a opção escolhida pelo usuário

    while option != "4": #enquanto a opção escolhida não for 4, o programa continua
        cls()
        banner() #imprime o banner do programa
        option = input("\n1 - Adicionar um produto ao carrinho \n2 - Remover um produto do carrinho \n3 - Visualizar carrinho \n4 - Finalizar compra\nDigite a opção desejada: ")
        if option == "1":
            
        elif option == "2":
            
        elif option == "3":
            
        elif option == "4":
            
        else:
            print("\nOpção inválida, tente novamente\n")
            time.sleep(2)

