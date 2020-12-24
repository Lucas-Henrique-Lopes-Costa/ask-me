from googlesearch import search

query = input('Faça sua pergunta: ')

for i in search(query, tld='com', num=1, stop=1, pause=1):
    print(i)