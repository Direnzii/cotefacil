from playwright.sync_api import sync_playwright
import time

class liberarForn():

    def abrir_arquivo(self, arquivo):
        with open(arquivo) as file:
            arquivo = file.read().replace(",", ' ').split()
        return arquivo

    def autenticar(self):
        time.sleep(0.5)
        usuario = 'thiago.direnzi'
        senha = 'XLy489uP'
        site.fill('xpath=//*[@id="frmLogin:username"]', usuario)
        site.fill('xpath=//*[@id="frmLogin:password"]', senha)
        site.locator('xpath=//*[@id="frmLogin:loginButton"]').click()
        time.sleep(0.2)

    def liberar_fornecedor(self):
        self.autenticar()
        for cliente in arquivo:
            cliente = cliente.replace("'", "")
            site.fill('xpath=/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table[1]/tbody/tr[4]/td/form/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr[2]/td[2]/input'
                      , cliente)
            time.sleep(0.5)
            site.locator('xpath=//*[@id="pesquisarUsuarios:btnPesquisar"]').click() #clicar em pesquisar
            time.sleep(0.5)
            try:
                site.locator('xpath=/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table[1]/tbody/tr[4]/td/form/table/tbody/tr[3]' ######BREAK
                         '/td/div/div[2]/table/tbody/tr[1]/td[6]/a').click() #clica em editar
                time.sleep(1.5)
                site.locator(
                    'xpath=/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/div/table[1]/tbody/tr[1]/td/form/table/tbody/tr[2]'
                    '/td/div/div/table/tbody/tr[1]/td/table/tbody/tr/td[8]/table/tbody/tr/td[2]/table/tbody/tr/td/table/tbody/tr/td[2]').click() #clica na aba de fornecedores
                time.sleep(1.5)
                fornecedor = '04048469000151 - PRYMME PHARMA - SP'
                representante = '56625 - On-line - no-reply@cotefacil.com'
                site.fill(
                    'xpath=//*[@id="administrarCliente:fornecedor"]'
                    , fornecedor)
                site.fill(
                    'xpath=//*[@id="administrarCliente:sggRepresentante"]'
                    , representante)
                site.locator(      ######BREAK
                    'xpath=//*[@id="administrarCliente:j_id277"]').click() #clicar em adicionar
                print(f"Fornecedor liberado para o cliente: {cliente}")
            except: ######BREAK
                print(f"Erro para o cliente: {cliente}")
                continue

liberar_forn = liberarForn()
with sync_playwright() as p:
    ##### VARIAVEIS DO PLAYWRIGHT #####
    navegador = p.firefox.launch(
        headless=False)  # por padrão esse modo é headless = True (não mostra o navegador abrindo)
    ###################################
    site = navegador.new_page()
    site.goto('https://sistemas.cotefacil.com/CTFLLogan-webapp/login.jsf')
    arquivo = 'prymme.txt'
    arquivo = liberar_forn.abrir_arquivo(arquivo)

    liberar_forn.liberar_fornecedor()



#thiago.direnzi
#XLy489uP