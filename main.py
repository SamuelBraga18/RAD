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

precos = [8000]

with open('precos_de_roupas.txt', 'a') as arquivo:
    for preco in precos:
        arquivo.write(str(preco), '\n')
    
print(arquivo.closed)
