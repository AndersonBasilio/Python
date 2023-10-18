import os
# Criando arquivos com Python
# Usamos a função open para abrir 
# um arquivo em python (ele pode ou não existir)
# Modos:
# r (leitura), w(escrita), x(para criação)
# a (escreve ao final), b (binario)
# t (modo texto), +(leitura e escrita)
# Context Manager - with (abre e fecha)
# Métodos úteis
# write, read, (escrever e ler)
# writelines (escrever varias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre os módulos json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = r'C:\\Users\\Anderson\\OneDrive\\Documentos\\python_github\\Python\\'
caminho_arquivo += 'pratica117.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Atenção\n')
#     arquivo.write('Linha 1\n')
#     arquivo.write('Linha 2\n')
#     arquivo.writelines(
#         ('Linha 3\n', 'Linha 4\n')
#     )
#     arquivo.seek(0, 0)
#     print(arquivo.read())
#     print('Lendo Arquivo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip()) 

#     print('\nReadlines')
#     arquivo.seek(0, 0)
#     for linhas in arquivo.readlines():
#         print(linhas.strip())


# print('==' * 12)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

# os.unlink(caminho_arquivo) ou remove
# os.rename(caminho_arquivo, 'aula120_2.txt')