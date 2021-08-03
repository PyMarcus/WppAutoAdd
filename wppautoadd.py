# WppAddAuto:
from selenium import webdriver
from colorama import init
from colorama import Fore
import time
import getpass
import os

# introdução
def inicio():
    init()
    try:
        time.sleep(2)
        print()
        print(Fore.GREEN + 'WppAddAuto')
        print(Fore.LIGHTGREEN_EX + """
     ____________
    |            |
    |    BEM     |
    |    VINDO!  |
    |            |
    |____________|
    (\__/) ||
    (o  o) |/
    / 　 \/
    """)
        time.sleep(60)
        print()
        time.sleep(3)
        print(
            Fore.LIGHTRED_EX + '* Por favor, não se esqueça de arquivar as conversas de grupos, pois, o WppAddAuto trabalha com as últimas conversas...')
        time.sleep(3)
        print()
        print(Fore.LIGHTRED_EX + '* Por favor, não se esqueça de se conectar ao whatsapp web.')
        time.sleep(3)
        print()
        time.sleep(2)
        print("Loading…")
        print("█▒▒▒▒▒▒▒▒▒")
        time.sleep(2)
        print("10%")
        print("███▒▒▒▒▒▒▒")
        time.sleep(2)
        print("30%")
        print("█████▒▒▒▒▒")
        time.sleep(2)
        print("50%")
        print("███████▒▒▒")
        time.sleep(2)
        print("100%")
        print("██████████")
        print("Aguarde...")
        time.sleep(60)
        print()
        print(Fore.LIGHTRED_EX + f'CONECTADO COM SUCESSO...')
    except KeyboardInterrupt:
        print(Fore.BLUE + 'Finalizado.')
        pass

# armazena numeros
def codigo_contatos(lista_num):
    init()
    numeros_paracontatos: list = []
    lista_de_nomes: list = []
    try:
        try:
            nome_contato: str = str(
                input(Fore.LIGHTCYAN_EX + '* Por favor, informe o código para anexar aos contatos: '))
            for num in range(1, 5000):
                numeros_paracontatos.append(num)
            tamanho_lista = len(lista_num)
            for elementos in numeros_paracontatos[:tamanho_lista]:
                nome_gerado = nome_contato + f'{elementos}'
                lista_de_nomes.append(nome_gerado)
            gera_arquivo(lista_num, lista_de_nomes)
            return lista_de_nomes
        except ValueError or TypeError:
            print(Fore.RED + '✞ RIP ✞')
            print(Fore.RED + 'Código não permitido')
    except KeyboardInterrupt:
        print(Fore.BLUE + 'Finalizado.')
        pass

# pega os contatos da web
def whatsapp_peganum():
    init()
    armazena_num: list = []
    driver = webdriver.Firefox()
    driver.get('https://web.whatsapp.com/')
    time.sleep(3)
    inicio()
    time.sleep(30)
    try:
        encontra_num = driver.find_elements_by_xpath("//*[contains(text(), '+55')]")
        tamanho_agora = len(armazena_num)
        for encontrado in encontra_num:
            if encontrado.text in armazena_num:
                pass
            else:
                try:
                    if encontrado.text.index('-'):
                        armazena_num.append(encontrado.text)
                except ValueError:
                    pass
            tamanho_depois = len(armazena_num)
            for numero in armazena_num:
                if tamanho_agora < tamanho_depois:
                    pass
        adicionar_contatos_googledrive(codigo_contatos(armazena_num))
        return armazena_num
    except KeyboardInterrupt:
        print(Fore.BLUE + 'Finalizado.')
        pass

# exibe os contatos a serem salvos
def adicionar_contatos_googledrive(funcao):
    try:
        init()
        print()
        print(Fore.YELLOW + 'Os nomes serão adicionados como :')
        for nomes in funcao:
            print(nomes + ', ', end='')
        print()
        print(Fore.LIGHTGREEN_EX + f'Agora relaxe, o bot do WppAddAuto fará todo o trabalho duro!')
        print()
        print(Fore.MAGENTA + 'Aguarde...')
        time.sleep(2)
        print()
        print('Adicionando os contatos identificados ao arquivo...')
        time.sleep(2)
        print()
        print()
        print(Fore.LIGHTGREEN_EX + 'CONCLUÍDO!')
        print()
    except KeyboardInterrupt:
        print(Fore.BLUE + 'Finalizado.')
        pass

# salva na pasta em csv
def gera_arquivo(lista, lista_de_nomes):
    try:
        init()
        user: str = getpass.getuser()
        os.chdir(f'C:\\Users\\{user}\\Documents\\')
        caminho: str = f'C:\\Users\\{user}\\Documents\\'
        if 'contatos_csv' in os.listdir(caminho):
            with open(f'{caminho}\\contatos_csv\\arquivo.csv', 'w', newline='') as file:
                arquivo = file.write('Nome' + ',' + 'Telefone' + '\n')
                i = 0
                for n in range(len(lista)):
                    arquivo = file.write(str(lista_de_nomes[n]) + ',' + str(lista[n]))
                    i += 1
                    arquivo = file.write('\n')
        else:
            os.mkdir(f'{caminho}contatos_csv')
            time.sleep(2)
            with open(f'{caminho}\\contatos_csv\\arquivo.csv', 'w', newline='') as file:
                arquivo = file.write('Nome' + ',' + 'Telefone' + '\n')
                i = 0
                for n in range(len(lista)):
                    arquivo = file.write(str(lista_de_nomes[n]) + ',' + str(lista[n]))
                    i += 1
                    arquivo = file.write('\n')
    except KeyboardInterrupt:
        print(Fore.BLUE + 'Finalizado.')
        pass


if __name__ == '__main__':
    usuario_do_pc = getpass.getuser()
    print(f'usuário: {usuario_do_pc} identificado')
    whatsapp_peganum()  # created by: Marcus V
