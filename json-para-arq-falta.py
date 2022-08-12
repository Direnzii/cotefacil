import json
import sys

def pegar_arquivo(arquivo, novo_arquivo):
    with open(arquivo) as file:
        file = json.load(file)
    i = 0
    saida = ''

    clientes = file['clientes']
    cnpj_cliente = clientes[0]['cnpj_cliente']
    itens = clientes[0]['itens']

    saida += f'1;{cnpj_cliente};3.3\n'

    if len(clientes) == 1:

        while i < len(itens):
            ean = itens[i]['ean']
            codigo_produto = itens[i]['codigo_produto']
            descricao_produto = itens[i]['descricao_produto']
            quantidade_cotada = itens[i]['quantidade_cotada']

            saida += f'2;{ean};{quantidade_cotada};{codigo_produto};{descricao_produto};.\n'

            i += 1
    else:
        while i < len(clientes):
            clientes = file[i]['clientes']
            cnpj_cliente = clientes[0]['cnpj_cliente']
            saida += f'1;{cnpj_cliente};3.3\n'
            i += 1

            while i < len(itens):
                ean = itens[i]['ean']
                codigo_produto = itens[i]['codigo_produto']
                descricao_produto = itens[i]['descricao_produto']
                quantidade_cotada = itens[i]['quantidade_cotada']

                saida += f'2;{ean};{quantidade_cotada};{codigo_produto};{descricao_produto};.\n'
                i += 1
            saida += f'9;{len(itens)}\n'

    saida += f'9;{len(itens)}'

    with open(f'{novo_arquivo}', 'w') as arquivo_falta:
        arquivo_falta.write(saida)

def main():
    if len(sys.argv) == 3:
        arquivo = (str(sys.argv[1]))
        novo_arquivo = (str(sys.argv[2]))
        pegar_arquivo(arquivo=arquivo, novo_arquivo=novo_arquivo)
    else:
        print(f'\nVOCÊ PRECISA PASSAR 2 ARGUMENTOS:\n\nEx do comando: \n\npython {sys.argv[0]} <NOME DO ARQUIVO .JSON> <NOME PARA O ARQUIVO DE FALTA .TXT>\n\n')

if __name__ == "__main__":
    main()



