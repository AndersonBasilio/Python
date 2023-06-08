"""
Closure e funções que retornam outras funções.
"""

def criar_saudacão(saudacao):# Tiramos o nome desse parametro 
    def saudar(nome):# Colocamos o nome, ou seja adiamos.
        return f'{saudacao}, {nome}!'
    return saudar #Se retirar os parenteses irá retorna a função que esta na memoria nao executa o que esta dentro da função.

falar_bom_dia = criar_saudacão('Bom dia')
falar_boa_tarde = criar_saudacão('Boa Tarde')

print(falar_bom_dia('Anderson'))# Para retornar um valor precisa fechar ou seja precisa salvar as coisas na memoria e entragar o valor.
print(falar_boa_tarde('James Hetefield'))# Para retornar um valor precisa fechar ou seja precisa salvar as coisas na memoria e entragar o valor.

#Podemos criar um for.
for nome in ['Anderson','Helena', 'Amanda']:
    print(falar_bom_dia(nome))# Para retornar um valor precisa fechar ou seja precisa salvar as coisas na memoria e entragar o valor.
    print(falar_boa_tarde(nome))# Para retornar um valor precisa fechar ou seja precisa salvar as coisas na memoria e entragar o valor.