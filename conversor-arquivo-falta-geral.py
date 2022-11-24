import json
import re

arquivo = 'teste.json'

saida = '1;<CNPJ CLIENTE>;3.3\n'

with open(arquivo, 'r') as file:
    arquivo_dict = json.load(file)
    clientes = arquivo_dict['clientes']

    contador = 0


    ean = item.get('ean')
    codigo_produto = item.get('ean')
    descricao = item.get('descricao_produto')
    saida += f'2;{ean};1;{codigo_produto};{descricao};.;0\n'
    contador += 1
    saida += f'9;{contador}'

print(saida)

with open("novo_arquivo.txt", 'w') as arquivo_falta:
    arquivo_falta.write(saida)