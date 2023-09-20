"""
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de 
inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com erros de indices inexistente na lista.
"""
import os

os.system('cls')
lista = []
indice_apagado = 0

while True:   
    
    print('Selecione uma opção:')
    opcao = input('[i]nserir/ [a]pagar/ [l]istar: ').lower()
        
    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'l':
        os.system('cls')
        if lista == []:
            print('Nada para listar.')
            continue
        else:
            for indice, valor in enumerate(lista):
                print(indice, valor)
                continue


    elif opcao == 'a':

            indice_str = input('Escolha o índice para apagar: ')

            try:
                indice = int(indice_str)
                indice_apagado = valor
                del lista[indice]
                print('Lista atualizada:')
                for indice, valor in enumerate(lista):
                    print(indice, valor)

            except ValueError:
                print('Por favor digite um número.')
            except IndexError:
                print('Índice não existe na lista.')
            except Exception:
                print('Erro desconhecido.') 
    
            

    else:
        print('Voce escolheu uma opção que não existe.') 

        sair = input('Quer sair? [Sim]/ [Nao]: ').lower().startswith('s')
        if sair is True:
            print('Obrigado por participar.')
            break
        else:
            continue