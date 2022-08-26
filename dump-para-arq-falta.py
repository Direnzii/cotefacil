import sys


def criar_arquivo(arquivo):
    with open(arquivo, 'r') as arquivo:
        contador = 0
        saida = '1;<CNPJ_CLIENTE>;3.3\n'
        #try:
        for linha in arquivo:
            try:
                codigo_produto = linha.split()[0]
                ean = linha.split()[1]
            except:
                continue
            descricao_lista = linha.split()[2::]
            descricao = ' '.join(descricao_lista)
            contador += 1
            saida += f'2;{ean};1;{codigo_produto};{descricao};.;0\n'

        saida += f'9;{contador}'
        with open(f'novo-arquivo-de-falta-base.txt', 'w') as arquivo:
            arquivo.write(saida)

#criar_arquivo('dump-base-martins.txt')  --- testar

def main():
    if len(sys.argv) == 2:
        arquivo = (str(sys.argv[1]))
        criar_arquivo(arquivo=arquivo)
    else:
        arquivo = 'ol-dump.txt'
        criar_arquivo(arquivo=arquivo)
        print(f'\nVOCÊ PRECISA PASSAR 1 ARGUMENTOS:\n\nEx do comando: \n\npython {sys.argv[0]} <NOME DO ARQUIVO .txt>\n\n')
if __name__ == "__main__":
    main()
