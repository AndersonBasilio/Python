"""
Jogo Palavra Secreta

Faça um jogo para o usuário adivinhar qual é a palavra secreta.
    -Você vai propor uma palavra secreta qualquer e vai da a possibilidade para o usuário digitar apenas uma letra
    -Quando o usuario digitar uma letra você vai conferir se a letra digitada esta na palavra secreta
    -Se a letra digitada estiver na palavra secreta; exiba a letra;
    -Se a letra digitada nao estiver na palavra secreta; exiba *.
Faça a contagem de tentativas do seu usuário.

"""
import os

os.system('cls')

palavra_secreta = 'METALLICA'
letras_acertadas = ''
tentativas = 0

print('Bem vindo ao Jogo')
print('Palavra Secreta')

while True:
    
    letra_digitada  = input('Digite uma letra: ').upper()
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Você digitou mais de uma ou número. Por favor digite uma letra!')
        continue

    if(letra_digitada in palavra_secreta):
        letras_acertadas += letra_digitada
        
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*' 

    print('Palavra Formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:

        os. system('cls')

        print('Você ganhou!!')
        print('PARABÉNS...')

        print(f'A palavra formada foi {palavra_formada.upper()}.')
        print(f'Tentativas: {tentativas}')
        letras_acertadas = 0

        continuar = input('Deseja continuar? [Sim]/[Nao]: ').lower().startswith('s')
        if continuar is True:
            continue

        else:
            break

os.system('cls')


print('Saindo')
print('Obrigado por participar!')