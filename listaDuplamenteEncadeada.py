class Node:

	# Funnção inicializadora
	def __init__(self, data):
		self.data = data 
		self.next = None 


#A classe ListaEncadeada contem um objeto Node
class ListaEncadeada:

	#Função que inicializa a "cabeça" da lista
	def __init__(self):
		self.cabeca = None

	#Função para realizar o print da lista
	def printList(self):
		temp = self.cabeca
		while (temp):
			print (temp.data)
			temp = temp.next


if __name__=='__main__':

	#Começa com uma lista vazia
	llist = ListaEncadeada()

	llist.cabeca = Node(1)
	segundo = Node(2)
	terceiro = Node(3)

	llist.cabeca.next = segundo; # Linka o primeiro nó com o segundo
	segundo.next = terceiro; # Linka o segundo nó com o  terceiro

	llist.printList()
