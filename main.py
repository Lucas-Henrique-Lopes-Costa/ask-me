import getpass
import os
import time
from googlesearch import search

os.system('clear') or None

# Conhecendo o Usuário
nome = input('Olá, será que você poderia me dizer o seu nome completo?\n')
primeiroNome = nome.split()[0]
print(f'Ok, {primeiroNome} prazer em te conhecer')

time.sleep(0.9)
os.system('clear') or None

# Pergunta
pergunta = input('Beleza! Então, qual a pergunta que você gostaria que eu respondesse ?\n')

os.system('clear') or None

# Senha
print('Para ter acesso, por favor digite a senha do Banco de Dados: ')
senha = getpass.getpass('')

if senha == "lucaslindo123":
    resposta = getpass.getpass('Confirme sua senha: ')

    if resposta == "Google":
        for i in search(pergunta, tld='com', num=1, stop=1, pause=1):
            # Formulando frase
            print('')
            print('PESQUISANDO...')
            time.sleep(0.9)
            print('         BUSCANDO NA INTERNET...')
            time.sleep(1.3)
            print('         CONFERINDO DADOS...')
            time.sleep(5)
            print('         CONSULTANDO IMB MACHINE LEARNING...')
            time.sleep(3)
            print('         TRATANDO DADOS...')
            time.sleep(2)
            print('         FORMULANDO FRASE...')
            time.sleep(1)
            print('PRONTO!')
            time.sleep(0.5)

            os.system('clear') or None
            
            print(f'Bom {nome}, pelas minhas pesquisas, esse é o melhor link que contém a sua resposta: {i}')
            
            time.sleep(100)
            quit()

    elif resposta == "Falha":
        print('')
        print('PESQUISANDO...')
        time.sleep(0.9)
        print('         BUSCANDO NA INTERNET...')
        time.sleep(1.3)
        print('Using legacy setup.py install for autopep8, since package wheel is not installed.')
        print('Using legacy setup.py install for autopep8, since package wheel is not installed.')
        print('Installing collected packages: pycodestyle, toml, autopep8')
        print('which is not on PATH.')
        print('WARNING: You are using pip version 20.2.3; however, version 20.3.3 is available.')

        print('         CONFERINDO DADOS...')
        time.sleep(5)
        print('         CONSULTANDO IMB MACHINE LEARNING...')
        time.sleep(3)
        print('         TRATANDO DADOS...')
        time.sleep(2)

        print('Machine Learning/legacy/scripts/classif_predict.py')
        print('Traceback (most recent call last):')
        print('     File "e:\Documents\Inteligência Artificial\Regual Machine Learning\legacy\scripts\classif_predict.py", line 1, in <module>')
        print('ModuleNotFoundError: No module find')

        print('         FORMULANDO FRASE...')
        time.sleep(1)

        os.system('clear') or None

        print('Falha :(')
        print('Não conseguimos encontrar nada, tente novamente mais tarde')
        time.sleep(0.5)
        quit()

    # Formulando frase
    print('')
    print('PESQUISANDO...')
    time.sleep(0.9)
    print('         BUSCANDO NA INTERNET...')
    time.sleep(1.3)
    print('         CONFERINDO DADOS...')
    time.sleep(5)
    print('         CONSULTANDO IMB MACHINE LEARNING...')
    time.sleep(3)
    print('         TRATANDO DADOS...')
    time.sleep(2)
    print('         FORMULANDO FRASE...')
    time.sleep(1)
    print('PRONTO!')
    time.sleep(0.5)

    os.system('clear') or None

    primeiroNome = nome.split()[0]
    print(f'Bom {primeiroNome}, pelas minhas pesquisas, ', end='')
    print(resposta)

    time.sleep(100)
else:
    print('Falha no login')
    quit()