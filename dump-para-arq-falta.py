import sys

def criar_arquivo(arquivo, novo_arquivo):
    with open(arquivo, 'r') as arquivo:
        contador = 0
        saida = ''
        saida += f'1;<CNPJ DO CLIENTE>;3.3\n'
        for linha in arquivo:
            separado = linha.split()
            ean = separado[5]
            descricao_listas = separado[6:2000]
            i = 0
            descricao_do_produto = ''
            while i < len(ean):
                try:
                    descricao_do_produto += descricao_listas[i] + ' '
                    i += 1
                    contador += 1
                except:
                    descricao = descricao_do_produto
                    saida += f'2;{ean};1;{ean};{descricao};.\n'
                    break
    saida += f'9;{contador}'
    with open(f'{novo_arquivo}', 'w') as arquivo_falta:
        arquivo_falta.write(saida)

def main():
    if len(sys.argv) == 3:
        arquivo = (str(sys.argv[1]))
        novo_arquivo = (str(sys.argv[2]))
        criar_arquivo(arquivo=arquivo, novo_arquivo=novo_arquivo)
    else:
        print(f'\nVOCÊ PRECISA PASSAR 2 ARGUMENTOS:\n\nEx do comando: \n\npython {sys.argv[0]} <NOME DO ARQUIVO .txt> <NOME PARA O ARQUIVO DE FALTA .TXT>\n\n')

if __name__ == "__main__":
    main()