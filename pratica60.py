"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.

O Código é executado de cima para baixo, da esquerda para direita
Execução do código(CIMA, PARA BAIXO, ESQUERDA PARA DIREITA).

Podemos acessar variaveis do escopo mais acima.
"""

#Nesse caso nao sera executado de CIMA, PARA BAIXO, ESQUERDA PARA DIREITA
x = 1
def escopo(): # Definimos a função
        global x # Aqui estou falando que x e igual o x de fora ou seja x = 1
        x = 10 #Esse x pode ser acessado, porque esta dentro da função escopo.

        def outra_funcao():# So fazer alguma coisa com y dentro da função outra_funcao.
            global x # Aqui estamos falando que x é igual o x de fora ou seja x = 1
            y = 2# Não posso acessar esse valor na função escopo
            x = 11# Este x é da função outra_função
            print(x, y)
        outra_funcao()
        print(x)

print(x)# Tudo que eu defino estive fora da função nao consigo acessar de fora da função.
escopo()# Mandamos executar a função, depois executa o que esta na função
print(x)

x = 30 #Definindo o x antes da da função posso usa-lo depois dará um erro "NameError: name 'x' is not defined"

#def testando_escopo():
    #print(x)

#testando_escopo()
