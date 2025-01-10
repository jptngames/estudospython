# Classe para clientes da netflix
class Cliente:
	def __init__(self, nome, email, plano):
		self.nome = nome
		self.email = email
		self.lista_planos = ["basic", "premuim"]
		if plano in self.lista_planos:
			self.plano = plano
		else:
			raise Exception('Plano Inválido')
			
	def mudar_plano(self, novo_plano):
		if novo_plano in self.lista_planos:
			self.plano = novo_plano
				
	def ver_filme(self, filme, plano_filme):
		if self.plano == plano_filme:
			print(f"Ver filme: {filme}")
		elif self.plano == "premium":
			print(f"Ver filme: {filme}")
		elif self.plano == "basic" and plano_filme == "premium":
			print("Faça upgrade para premuim")
		else:
			print("Plano Inválido")
	
	
	

cliente = Cliente("Lira", "lira@gmail.com", "basic")
print(cliente.plano)
cliente.ver_filme("Harry Potter", "premium")

# botão de mudar plano
cliente.mudar_plano("premuim")
print(cliente.plano)
cliente.ver_filme("Harry Potter", "premium")
