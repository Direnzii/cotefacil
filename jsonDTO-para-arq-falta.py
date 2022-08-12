import json
import sys

def pegar_arquivo(arquivo, novo_arquivo):
    with open(arquivo, 'r') as file:
        i = 0
        json_dict = json.load(file)

        cnpj_cliente = json_dict['fornecedorDTO'].get('cnpj')
        lista_de_itens_geral = json_dict['fornecedorDTO'].get('itens', {})

        total_de_produtos = len(lista_de_itens_geral)  # numero_de_produtos

        saida = ''

        #### COMEÇO DO ARQUIVO DE FALTA ####
        saida += f'1;{cnpj_cliente};3.3\n'

        while total_de_produtos > i:
            codigo_de_barras = lista_de_itens_geral[i]['codigoDeBarras']
            descricao_do_produto = lista_de_itens_geral[i]['descricaoDoProduto']
            descricao_do_fabricante = lista_de_itens_geral[i]['descricaoDoFabricante']

            saida += f'2;{codigo_de_barras};1;{codigo_de_barras};{descricao_do_produto.upper()};{descricao_do_fabricante}\n' # 0000 é o codigo do produto, não encontrei no json
            i += 1

        saida += f'9;{total_de_produtos}'

        with open(f'{novo_arquivo}', 'w') as arquivo_falta:
            arquivo_falta.write(saida)

        return saida
        #### FINAL DO ARQUIVO DE FALTA ####

def main():
    if len(sys.argv) == 3:
        arquivo = (str(sys.argv[1]))
        novo_arquivo = (str(sys.argv[2]))
        pegar_arquivo(arquivo=arquivo, novo_arquivo=novo_arquivo)
    else:
        print(f'\nVOCÊ PRECISA PASSAR 2 ARGUMENTOS:\n\nEx do comando: \n\npython {sys.argv[0]} <NOME DO ARQUIVO .JSON> <NOME PARA O ARQUIVO DE FALTA .TXT>\n\n')

if __name__ == "__main__":
    main()

