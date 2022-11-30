from playwright.sync_api import sync_playwright
import time
import re

class liberarForn():

    lista_matrizes = []
    lista_filiais = []

    def abrir_arquivo(self):
        with open('mil.txt') as file:
            arquivo = file.read().replace(",", ' ').split()
        return arquivo

    def autenticar(self):
        time.sleep(0.5)
        usuario = 'COLOCAR USUARIO'
        senha = 'COLOCAR SENHA'
        site.fill('xpath=//*[@id="frmLogin:username"]', usuario)
        site.fill('xpath=//*[@id="frmLogin:password"]', senha)
        site.locator('xpath=//*[@id="frmLogin:loginButton"]').click()
        time.sleep(0.2)

    def validar_se_da_para_ver_elemento(self, caminho_elemento_xpath):
        da_para_ver = False
        while da_para_ver == False:
            try:
                da_para_ver = site.locator(f'xpath={caminho_elemento_xpath}').is_visible()
                if da_para_ver == False:
                    time.sleep(0.5)
                if da_para_ver == True:
                    break
            except Exception as e:
                continue
        return da_para_ver

    def validar_listas(self, cliente):
        matriz = cliente in self.lista_matrizes
        filial = cliente in self.lista_filiais
        if matriz == True:
            return True
        if filial == True:
            return True
        else:
            return False

    def get_filiais(self):
        site.locator('xpath=//*[@id="administrarCliente:tabFiliais_cell"]').click()  # clicar na aba filiais
        for i in range(0, 11): #10 tentativas para ver se é falso ou nao
            eh_visivel_contar_filiais = site.locator(
                'xpath=/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table[1]/tbody/tr[1]/td/form'
                '/table/tbody/tr[2]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div'
                '/div/table/tbody/tr[1]').is_visible()
            if eh_visivel_contar_filiais == True:
                break
            if eh_visivel_contar_filiais == False:
                time.sleep(0.2)

        contar_filiais = site.locator(
            'xpath=/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table[1]/tbody/tr[1]/td/form'
            '/table/tbody/tr[2]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div'
            '/div/table/tbody/tr').count()

        if contar_filiais != 0:
            for numero in range(1, contar_filiais + 1): # range usado para usar um for na quantidade de filiais
                try:
                    filial = site.locator(
                        f'xpath=/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table[1]/tbody/tr[1]/td/form'
                        '/table/tbody/tr[2]/td/div/div/table/tbody/tr[2]/td/table/tbody/tr/td/table/tbody/tr[1]/td/div'
                        f'/div/table/tbody/tr[{numero}]').text_content()
                    validacao_filial = self.validar_listas(int(filial)) #validar se a filial ja esta na lista das filiais
                    if validacao_filial == False:
                        filial = filial.split()[0]
                        filial = self.remover_string(filial)
                        self.lista_filiais.append(int(filial))
                    if validacao_filial == True:
                        continue
                except Exception as e:
                    continue
            return
        else:
            return

    def remover_string(self, valor):
        valor = re.sub('[^0-9]', '', valor)
        return int(valor)

    def resolver_zeros(self, numero):
        numero = str(numero)
        contador = 0
        for i in numero:
            contador += 1
        numero = int(numero)
        if contador != 14:
            zeros = 14 - contador
            if zeros == 1:
                numero = numero * 10
                return numero
            elif zeros == 2:
                numero = numero * 100
                return numero
            elif zeros == 3:
                numero = numero * 1000
                return numero
            elif zeros == 4:
                numero = numero * 10000
                return numero
            elif zeros == 5:
                numero = numero * 100000
                return numero
            elif zeros == 6:
                numero = numero * 1000000
                return numero
            elif zeros == 7:
                numero = numero * 10000000
                return numero
            elif zeros == 8:
                numero = numero * 100000000
                return numero
            elif zeros == 9:
                numero = numero * 1000000000
                return numero
            elif zeros == 10:
                numero = numero * 10000000000
                return numero
            elif zeros == 11:
                numero = numero * 100000000000
                return numero
        else:
            return numero

    def comparar_cliente_linha_cliente(self, cliente):
        while True:
            try:
                time.sleep(0.2)
                linha_cliente = site.locator('xpath=/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]'
                                             '/div/table[1]/tbody/tr[1]/td/form/table[2]/tbody/tr[3]/td/div'
                                             '/div[2]/div/div/table/tbody/tr').text_content()
                linha_cliente = linha_cliente.split()[0]
                linha_cliente = self.remover_string(linha_cliente)
                if int(cliente) == int(linha_cliente):
                    return True
            except:
                linha_cliente_err = site.locator('xpath=/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]'
                                             '/div/table[1]/tbody/tr[1]/td/form/table[2]/tbody/tr[3]/td/div'
                                             '/div[2]/div/div/table/tbody/tr').count()
                if linha_cliente_err != 1:
                    linha_cliente = site.locator('xpath=/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]'
                                                 '/div/table[1]/tbody/tr[1]/td/form/table[2]/tbody/tr[3]/td/div'
                                                 '/div[2]/div/div/table/tbody/tr[1]').text_content()
                    linha_cliente = linha_cliente.split()[0]
                    linha_cliente = self.remover_string(linha_cliente)
                    if int(cliente) == int(linha_cliente):
                        return True
                    else:
                        linha_cliente = self.resolver_zeros(linha_cliente)
                        cliente = self.resolver_zeros(cliente)
                        if cliente == linha_cliente:
                            return True

    def clicar_aba_inicio(self):
        caminho_imagem_aba_inicio = '/html/body/table/tbody/tr[1]/td/div/form[2]/ul/li[1]/a/img'
        caminho_conteudo_aba_inicio = '//*[@id="esConteudo"]'
        da_para_ver = self.validar_se_da_para_ver_elemento(caminho_imagem_aba_inicio)
        if da_para_ver == True: #validar se da pra ver imagem aba inicio
            site.locator('xpath=/html/body/table/tbody/tr[1]/td/div/form[2]/ul/li[1]').click() #clicar na aba inicio
            time.sleep(1)
            while True:
                da_para_ver = self.validar_se_da_para_ver_elemento(caminho_conteudo_aba_inicio)
                if da_para_ver == True:
                    return

    def clicar_aba_cliente(self):
        caminho_imagem_aba_clientes = '/html/body/table/tbody/tr[1]/td/div/form[2]/ul/li[2]/a/img'
        caminho_botao_liberacao_aba_cliente = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table[1]/tbody/tr[1]/td/form/table[1]/tbody/tr/td[1]/input'
        da_para_ver = self.validar_se_da_para_ver_elemento(caminho_imagem_aba_clientes)
        if da_para_ver == True: #validar se da pra ver imagem aba clientes
            site.locator('xpath=/html/body/table/tbody/tr[1]/td/div/form[2]/ul/li[2]').click() #clicar na aba clientes
            time.sleep(0.5)
            da_para_ver1 = self.validar_se_da_para_ver_elemento(caminho_botao_liberacao_aba_cliente)
            if da_para_ver1 == True:
                return

    def reiniciar_a_tela(self):
        self.clicar_aba_inicio()
        self.clicar_aba_cliente()
        return

    def validar_se_da_pra_ver_loading(self):
        text_carregando = '//*[@id="loadMessageContainer"]'
        da_pra_ver = site.locator(f'xpath={text_carregando}').get_attribute('style')
        while True:
            da_pra_ver = da_pra_ver.split()[-1]
            if da_pra_ver == 'inherit;':
                time.sleep(0.2)
                da_pra_ver = site.locator(f'xpath={text_carregando}').get_attribute('style')
            if da_pra_ver == 'none;':
                return False

    def validar_se_da_pra_ver_erro(self, caminho_elemento_xpath):
        time.sleep(0.5)
        da_para_ver = site.locator(f'xpath={caminho_elemento_xpath}').is_visible()
        if da_para_ver == False:
            time.sleep(0.5)
            return da_para_ver
        if da_para_ver == True:
            return da_para_ver

    def dentro_aba_cliente(self, cliente):
        caminho_eh_cliente = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table[1]/tbody/tr[1]' \
                             '/td/form/table[2]/tbody/tr[3]/td/div/div[2]/div/div/table/tbody/tr'
        caminho_do_input = '//*[@id="pesquisarClientes:cnpj"]'
        caminho_erro = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table[1]/tbody/tr[1]/td/form/span/div/div/table/tbody/tr/td/table/tbody/tr/td[2]/table'
        da_pra_ver = self.validar_se_da_para_ver_elemento(caminho_do_input)
        while True:
            if da_pra_ver == True:
                time.sleep(1)
                site.locator(
                    'xpath=//*[@id="pesquisarClientes:mostrarFiliais"]').click()  # checar a box "mostrar filiais"
                site.fill('xpath=//*[@id="pesquisarClientes:cnpj"]', cliente)
                site.locator('xpath=//*[@id="pesquisarClientes:btnPesquisar"]').click()  # clicar em pesquisar
                time.sleep(1)
                deu_erro = self.validar_se_da_pra_ver_erro(caminho_erro)
                if deu_erro == True:
                    self.reiniciar_a_tela()
                    time.sleep(0.5)
                    self.dentro_aba_cliente(cliente)
                    return

                comparacao = self.comparar_cliente_linha_cliente(cliente)
                if comparacao == True:
                    load = self.validar_se_da_pra_ver_loading() #validar se da pra ver o loading
                    if load == False:
                        try:
                            site.locator('xpath=/html/body/table/tbody/tr[2]/td/table/tbody'
                                     '/tr/td[2]/div/table[1]/tbody/tr[1]/td/form/table[2]'
                                     '/tbody/tr[3]/td/div/div[2]/div/div/table/tbody/tr'
                                     '/td[4]/input').click()  # clicar no editar
                            time.sleep(0.5)
                            return
                        except:
                            site.locator('/html/body/table/tbody/tr[2]/td/table/tbody'
                                         '/tr/td[2]/div/table[1]/tbody/tr[1]/td/form/table[2]'
                                         '/tbody/tr[3]/td/div/div[2]/div/div/table/tbody/tr[1]'
                                         '/td[4]/input').click()  # clicar no editar
            #/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table[1]/tbody/tr[1]/td/form/table[2]/tbody/tr[3]/td/div/div[2]/div/div/table/tbody/tr[1]/td[4]/input
                        time.sleep(0.5)
                        return

    def organizar_listas(self):
        self.autenticar()
        arquivo = self.abrir_arquivo() #abrir arquivo
        caminho_botao_ativar_inativar = '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table[1]' \
                                        '/tbody/tr[1]/td/form/table/tbody/tr[2]/td/div/div/table/tbody/tr[2]' \
                                        '/td/table/tbody/tr/td/input'
        for cliente in arquivo: #percorrer a lista de clientes (arquivo)
            validacao = self.validar_listas(int(cliente))
            if validacao == False:
                self.clicar_aba_cliente()
                self.dentro_aba_cliente(cliente)
                da_para_ver_botao_ativar_inativar = self.validar_se_da_para_ver_elemento(caminho_botao_ativar_inativar)
                if da_para_ver_botao_ativar_inativar == True:
                    input_matriz = site.locator('xpath=/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table[1]'
                                          '/tbody/tr[1]/td/form/table/tbody/tr[2]/td/div/div/table/tbody/tr[2]/td'
                                          '/table/tbody/tr/td/div/div[2]/table/tbody/tr[2]/td[2]/input').input_value() #pegar o valor do campo "cnpj matriz"
                    if not input_matriz:
                        validacao_matriz_1 = self.validar_listas(int(cliente))
                        if validacao_matriz_1 == False:
                            self.lista_matrizes.append(int(cliente)) #validou que o cnpj não possui matriz setada (logo é uma matriz)
                        self.get_filiais()
                        self.reiniciar_a_tela()
                    else:
                        self.lista_filiais.append(int(cliente)) #colocando a filial na lista filiais
                        validacao_matriz_2 = self.validar_listas(int(input_matriz))
                        if validacao_matriz_2 == False:
                            self.lista_matrizes.append(
                                int(input_matriz))  # validou que o cnpj possui matriz setada (logo é uma filial), estou colocando o input da matriz na lista matrizes
                            self.reiniciar_a_tela()
                            time.sleep(0.5)
                            self.dentro_aba_cliente(input_matriz)
                            self.get_filiais()
                            self.reiniciar_a_tela()
            if validacao == True:
                continue
        a = 'saiu do for'

liberar_forn = liberarForn()
with sync_playwright() as p:
    ##### VARIAVEIS DO PLAYWRIGHT #####
    navegador = p.firefox.launch(headless=False)  # por padrão esse modo é headless = True (não mostra o navegador abrindo)
    ###################################
    site = navegador.new_page()
    site.goto('https://sistemas.cotefacil.com/CTFLLogan-webapp/login.jsf')

    try:
        liberar_forn.organizar_listas()
    except Exception as e:
        print("Error")
