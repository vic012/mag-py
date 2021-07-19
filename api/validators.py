import requests

class ValidaDados:

	def __init__(self, dados):
		self._dados = dados
		self._resultado = "error"

	@property
	def resultado(self):
		return self._resultado

	def validacao(self):
		#Se a versão for preenchida
		if ('version' in self._dados):
			#Pega o nome do pacote
			nome_do_pacote = self._dados['name']
			#pega a versão do pacote
			versao_do_pacote = self._dados['version']

			#Verifica primeiro se o nome do pacote é válido
			api_nome = requests.get('https://pypi.org/pypi/{}/json'.format(nome_do_pacote))
			if (api_nome.status_code == 200):
				#Verifica se a versão é válida
				api_versao = requests.get('https://pypi.org/pypi/{}/{}/json'.format(nome_do_pacote, versao_do_pacote))
				if (api_versao.status_code == 200):
					self._resultado = {"nome": api_nome.json()['info']['name'], "versao": versao_do_pacote}
					return True
				else:
					return False
			else:
				return False
		#Se a versão não for preenchida
		else:
			#Pega o nome do pacote
			nome_do_pacote = self._dados['name']

			#Verifica primeiro se o nome do pacote é válido
			api_nome = requests.get('https://pypi.org/pypi/{}/json'.format(nome_do_pacote))
			if (api_nome.status_code == 200):
				self._resultado = {"nome": api_nome.json()['info']['name'], "versao": api_nome.json()['info']['version']}
				return True
			else:
				return False