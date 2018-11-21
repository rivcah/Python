##In Portuguese
##Em português
##Esse programinha faz um mini-diário de classe

def diario():
    cancel = False
    lista_de_classe = []
    while (True):
        nome = input("Digite o nome do(a) estudante: \n")
        dever_de_casa = [int(i) for i in input("Entre as notas do dever de casa, separadas por vírgulas. \n").split(', ')]
        testes = [int(i) for i in input("Digite as notas dos testes. \n").split(', ')]
        prova = [int(i) for i in input("Digite a nota da prova final. \n").split(', ')]
        lista_de_classe.append({
		"Nome" : nome,
		"Dever de casa" : dever_de_casa,
		"testes" : testes,
		"Prova final" : prova})
        cont = input("Você quer continuar?\n S/N \n")
        if cont == "N" or cont == "n":
            break

    print(lista_de_classe)
    
