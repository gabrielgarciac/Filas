class Node:

	#Função inicializadora
	def __init__(self, data):
		self.data = data
		self.next = None


#A classe ListaEncadeada contem um object Node
class ListaEncadeada:

	#Função para inicializar a "cabeça" da lista
	def __init__(self):
		self.cabeca = None


if __name__=='__main__':

	#Começa com a lista vazia
	llist = ListaEncadeada()

	llist.cabeca = Node(1)
	segundo = Node(2)
	terceiro = Node(3)

    #Os 3 nós de exemplo foram criados acima

	llist.cabeca.next = segundo; #Linka o primeiro nó com o segundo

	segundo.next = terceiro; #Linka segundo nó com o terceiro