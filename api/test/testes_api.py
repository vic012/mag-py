from rest_framework.test import APITestCase
from api.serializers import ProjectSerializer
from django.urls import reverse
from rest_framework import status

class PackageTestCase(APITestCase):

	def setUp(self):
		#Pega a string informada no basename do urls.py
		self.list_url = reverse('Projects-list')

	def test_requisição_post_criar_projeto_sem_nome(self):
		"""Teste de requisição POST para criar um novo projeto sem nome de pacote"""
		dados = {
			"name": "titan",
			"packages": [
				{"version": "3.2.5"},
		        {"name": "graphene", "version": "2.0"}
		    ]
		}
		response = self.client.post(self.list_url, dados, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_requisição_post_criar_projeto_nome_invalido(self):
		"""Teste de requisição POST para criar um novo projeto com nome de pacote inválido"""
		dados = {
			"name": "titan",
			"packages": [
				{"name": "pypypypy", "version": "3.2.5"},
		        {"name": "graphene", "version": "2.0"}
		    ]
		}
		response = self.client.post(self.list_url, dados, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_requisição_post_criar_projeto_sem_versao(self):
		"""Teste de requisição POST para criar um novo projeto sem versão"""
		dados = {
			"name": "titan",
			"packages": [
				{"name": "django", "version": "3.2.5"},
		        {"name": "graphene"}
		    ]
		}
		response = self.client.post(self.list_url, dados, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_requisição_post_criar_projeto_com_versao_invalida(self):
		"""Teste de requisição POST para criar um novo projeto com versão inválida"""
		dados = {
			"name": "titan",
			"packages": [
				{"name": "django", "version": "3.2.5"},
		        {"name": "graphene", "version": "1900"}
		    ]
		}
		response = self.client.post(self.list_url, dados, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_cria_projeto_valido(self):
		"""Teste de requisição POST para criar um novo projeto Válido"""
		dados = {
			"name": "titan",
			"packages": [
				{"name": "Django", "version": "3.2.5"},
		        {"name": "graphene", "version": "2.0"}
		    ]
		}
		response = self.client.post(self.list_url, dados, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_requisicao_get_lista_projeto(self):
		"""Teste de requisição GET para listar os projeto"""
		response = self.client.get(self.list_url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)