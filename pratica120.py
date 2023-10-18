# Exercicio - Lista de tarefas com desfazer e refazer
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adiciona fazer café
# todo = ['fazer café', 'caminhar'] Adiciona caminhar
# desfazer = ['fazer café',] -> Refazer ['Caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café]
# refazer = todo ['fazer café', 'caminhar']
import os
import json

def listar(tarefas):
    contador = 1
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar.')
        print()
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{contador} - {tarefa}')
        contador += 1
    print()

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer.')
        return
    tarefa = tarefas.pop()
    print(f'{tarefa} desfeita com sucesso.')
    tarefas_refazer.append(tarefa)
    print()
    listar(tarefas)

def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer.')
        return
    tarefa = tarefas_refazer.pop()
    print(f'{tarefa} refeita com sucesso.')
    tarefas.append(tarefa)
    print() 
    listar(tarefas)   

def adicionar(tarefa, tarefas):
    tarefa = tarefa.strip() 
    if not tarefa:
        print('Você não digitou nenhuma tarefa.')
    tarefas.append(tarefa)
    print()
    listar(tarefas)

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
    return dados
    

CAMINHO_ARQUIVO = 'aula123.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

print('Comandos: ')
print('\tListar - Para listar')
print('\tDesfazer - Para desfazer')
print('\tRefazer - Para refazer')
print('\tClear - Para limpar o terminal')
print('\tSair - Para sair')

while True:
    tarefa = input('Digite um comando ou uma tarefa: ').lower()

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    if tarefa == 'sair':
        break

    salvar(tarefas, CAMINHO_ARQUIVO)



    # if tarefa == 'listar':
    #     listar(tarefas)
    #     continue

    # elif tarefa == 'desfazer':
    #     desfazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue
        
    # elif tarefa == 'refazer':
    #     refazer(tarefas, tarefas_refazer)
    #     listar(tarefas)
    #     continue  

    # elif tarefa == 'clear':
    #     os.system('cls')

    # elif tarefa == 'sair':
    #     os.system('cls')
    #     listar(tarefas)
    #     break

    # else: 
    #     adicionar(tarefa, tarefas)
    #     listar(tarefas)
    # 