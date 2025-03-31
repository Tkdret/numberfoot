from random import randint
from os import system
from time import sleep

def main():
    # Sorteia um número aleatorio entre 1 e 10.
    numero = randint(1, 10)
    # While True para o programa nunca finalizar.
    while True:

        print("Chute um número entre 1 a 10")
        inputuser = int(input(">"))
        print(" ")

        if (inputuser > 10) or (inputuser <= 0):
            # Se o número que o usuario digitar for maior que 10 ou menor e igual a zero o programa não deixa ele proseguir
            print("Apenas números entre 1 a 10")
            sleep(3)
            system("cls")
    
        else:
            if (numero < inputuser):
                # A cada tentativa se o numero for abaixo do valor, o programa vai falar para o usuario e informar os possiveis números.
                    print("Tente novamente, o chute foi abaixo do valor.")
                    print("Tente algo entre: {}, {} e {} ".format(inputuser - 1, inputuser - 2, inputuser - 3))
                    print(" ")
                    
            if (numero > inputuser):
                # A cada tentativa se o numero for maior que o valor, o programa vai falar para o usuario e informar os possiveis números.
                   
                    print("Tente novamente, o chute foi acima do valor.")
                    print("Tente algo entre: {}, {} e {}".format(inputuser + 1,inputuser + 2, inputuser + 3))
                    print(" ")

            if (inputuser == numero):
                # Se o número digitado for igual ao numero sorteado o usuario ganha o jogo.
                    print("Você acertou o número é {}".format(numero))
                    print(" ")

                    print("Deseja jogar novamente?")
                   
                    print("""
                    ======OPÇÕES====

                        SIM (1)
                        NÃO (2)

                    =================
                    """)

                    inputuser = int(input(">"))
                    # Menu de opções, se o numero for diferente de 1, o programa acaba, se não o programa reinicia.
                    if (inputuser == 1):
                        sleep(3)
                        system("cls")
                        main()
                        
                    else:
                        # Caindo no else, o programa quebra o laço While com break e encerra o programa.
                        print("Obrigado por ter jogado até mais")
                        sleep(3)
                        system("cls")
                        break

main()