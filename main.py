'''arquivo = open('texto.txt', 'r')
print(arquivo.read())
print(arquivo.readline())
print(arquivo.seek(0))
print('------------------------')
print('------------------------')
print(arquivo.name)
print(arquivo.mode)'''
'''print(arquivo.tell())
arquivo.close()
print(arquivo.closed)'''

'''arquivo = open('novo.txt', 'w')
arquivo.write('Arquivo de escrita')
arquivo.close()
print(arquivo.closed)'''

'''arquivo = open('frutas.txt', 'w')
arquivo.write('banana\nuva\nmamao\ngoiaba')
arquivo.close()
print(arquivo.closed)'''

'''precos = [200, 100, 500, 600]

with open('Precos_de_roupas.txt', 'w') as arquivo:
    for preco in precos:
        arquivo.write(str(preco) + '\n')

print(arquivo.closed)'''

"""precos = [8000]

with open('precos_de_roupas.txt', 'a') as arquivo:
    for preco in precos:
        arquivo.write(str(preco), '\n')
    
print(arquivo.closed)"""


'''disciplinas = ["Rad\n", "introdução a C\n", "programa"]
with open("disciplinas.txt", 'w') as file:
    file.write("Relação de disciplinas\n")
    file.writelines(disciplinas)


with open('disciplinas.txt', 'r') as file:
    print(file.read())'''


'''with open('texto.txt', 'r') as arquivo:
    print('Representação original da linha')

    for linha in arquivo:
        print(repr(linha))

with open('texto.txt', 'r') as arquivo:
    print("conteudo da linha")
    for linha in arquivo:
        linha_ = linha.strip()
        print(repr(linha_))'''

'''minha_lista = ['arroz', 'feijão', 'carne', 'macarrao']
lista_ = '.'.join(minha_lista)
with open('texto.txt', 'w') as arquivo:
    arquivo.write(lista_)'''

'''try:
    with open('arquivoteste.txt', 'r') as arquivo:
        print(arquivo.read)
except FileNotFoundError:
    print('arquivo inexistente')'''

'''import os

try:
    os.remove('teste.txt')
    print('arquivo deletado')
except FileNotFoundError as erro:
    print('arquivo inexistente')
    print(erro)'''

try:
    f = open('novo2.txt', 'r')
    f.write("Hello")
except IOError as erro:
    print("Erro:", erro)