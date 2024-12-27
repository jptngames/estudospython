import requests

def get():
	requisicao = requests.get("https://aprendendo-cb333-default-rtdb.firebaseio.com/.json")
	print(requisicao)
	print(requisicao.json())

def post():
	informacoes = '{"Nome": "Amanda"}'
	requisicao = requests.post("https://aprendendo-cb333-default-rtdb.firebaseio.com/.json", data=informacoes)
	print(requisicao)
	print(requisicao.json())

def patch():
	informacoes = '{"Nome": "Daniel", "Sobrenome": "Candiotto", "Idade": "29"}'
	requisicao = requests.patch("https://aprendendo-cb333-default-rtdb.firebaseio.com/-OF98QDzOecI6o9pB_oD.json", data=informacoes)
	print(requisicao)
	print(requisicao.json())

def delete():
	requisicao = requests.delete("https://aprendendo-cb333-default-rtdb.firebaseio.com/-OF98QDzOecI6o9pB_oD.json")
print(requisicao)
print(requisicao.json())