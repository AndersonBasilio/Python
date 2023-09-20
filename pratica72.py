# Exercício - Sistema de Perguntas e Respostas
import os
import emoji

while True:
        
        os.system('cls')

        print('--' * 16)
        print('🤘 QUIZ - ROCK N ROLL! ')
        print('--' * 16)

        perguntas = [
            {
                'Pergunta': 'Quem é o vocalista da banda Metallica?',
                'Opções': ['Brian May', 'Freddie Mercury', 'James Hetfield', 'Bruce Dickinson'],
                'Resposta': 'James Hetfield',
            },
            {
                'Pergunta': 'Em que ano baixista do Metallica Cliff Burton morreu?',
                'Opções': ['1962', '1989', '1986', '1989'],
                'Resposta': '1986',
            },
            {
             'Pergunta': 'Qual é o nome do pai de Freddie Mercury?',
                'Opções': ['Kash Bulsara', 'Fredderic Bulsara', 'Jer Mercury', 'Bomi Bulsara'],
                'Resposta':'Bomi Bulsara',
            },
            {
                'Pergunta': 'Em que ano o disco do Queen A Night at the Opera foi lançado? ',
                'Opções':['1986', '1985', '1975', '1995'],
                'Resposta':'1975',
            },
        ]

        quantidade_acertos = 0

        for pergunta in perguntas:
            print('Pergunta:', pergunta['Pergunta'])
            print()

            opcoes = pergunta['Opções']

            for i, opcao in enumerate(opcoes):
                print(f'{i}) - {opcao}')
            print()
  
            escolha = input('Escolha uma opção: ')

            acertou = False
            escolha_int = None
            quantidade_opcoes = len(opcoes)
            

            if escolha.isdigit():
                escolha_int = int(escolha)
    
            if escolha_int is not None:
                if escolha_int >= 0 and escolha_int < quantidade_opcoes:
                    if opcoes[escolha_int] == pergunta['Resposta']:
                        acertou = True
            print()
        
            if acertou:
                quantidade_acertos += 1
                print('👍 Acertou!')
            else:
                print('❌ Errou!')

            print()

        os.system('cls')

        print(f'Você acertou {quantidade_acertos} perguntas de {len(perguntas)}')
        if quantidade_acertos < 2:
            print('Seu conhecimento em Rock n Roll não esta bom, pesquise mais. 💻')
        else:
            print('Parabéns! Você é Roqueiro...🎸 ')

        jogar = input('Você deseja jogar Novamente? [Sim] / [Nao]: ').lower()

        if jogar != 'sim' and jogar != 's':
            os.system('cls')
            print('Volte Sempre!')
            print('Long Live Rock n Roll...\n')
            break