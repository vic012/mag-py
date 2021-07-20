# MAgPy Pedro

Neste repositório você encontra a descrição de uso da API de versionamento de 
pacotes usados em projetos Python, ela é últil para orientar o versionamento
das bibliotecas usadas na criação de um projeto.

## Caso de uso

Imagine que uma equipe de programadores usa vários módulos na criação de um projeto!
É bem provável que durante o desenvolvimento um ou mais desenvolvedor sentirá
a necessidade de verificar se os pacotes usados são válidos ou não de acordo com
a API do [PyPI](https://pypi.org/) ou qual a versão ultilizar.

## Como usar

Acesse: [MagPy-Pedro](https://magpy-pedro.herokuapp.com/api/projects/)
Aqui você encontrará o Project List.
Onde é posível efetuar requisições dos seus projeto no formato JSON
Exemplo de requisição POST:
POST https://magpy-pedro.herokuapp.com/api/projects/
```
{
    "name": "Auditor-contabil" // Você deve especificar o nome do projeto
    "packages": [
        {"name": "Pandas", "version": "1.3.0" },  // Você deve especificar o nome do pacote
        {"name": "PyAutoGui"},
	{"name": "Django", "version": "3.2.5"}   // Mas a versão é opcional
    ]
}
```
Se você informar um projeto com um nome de pacote ou versão inválidos os seus dados não
serão gravados, mas será retornado um erro, por exemplo:

```
{
    "name": "Auditor-contabil"
    "packages": [
        {"name": "Pandas", "version": "1.3.0" },  
        {"name": "PyAutoGui"},
	{"name": "Django", "version": "19058"}   // VERSÃO INVÁLIDA
    ]
}
```
Ou
```
{
    "name": "Auditor-contabil"
    "packages": [
        {"name": "Pandas", "version": "1.3.0" },  
        {"name": "pypypypyvixe"}, // NOME INVÁLIDO
	{"name": "Django", "version": "3.2.5"}
    ]
}
```
O erro será: Um ou mais pacotes não existe.

```
{
    "error": "One or more packages doesn't exist"
}

```
Você também pode listar um projeto específica pelo nome do projeto
GET https://magpy-pedro.herokuapp.com/api/projects/Auditor-contabil/

Da mesma forma, deletar um projeto pelo nome
DELETE https://magpy-pedro.herokuapp.com/api/projects/Auditor-contabil/

## MagPy-Pedro Documentação
[MagPy-Pedro-swagger](https://magpy-pedro.herokuapp.com/doc-sw/)
[MagPy-Pedro-redoc](https://magpy-pedro.herokuapp.com/doc-re/)

## Como funciona os testes
Clone o repositório para o seu computador, depois disto execute:
```
..> python -m pipenv install

```
Feito isso, você terá instalados todos os pacotes listados no arquivo Pipfile.lock
Em seguida, você deve ativar o ambiente virtual e depois fazer as migrações
do banco de dados com os comandos:
```
..> python -m pipenv shell
(nomeDoAmbiente)..> python manage.py migrate
```
Muito bem, dessa forma o MagPy-Pedro já está inplantado, agora você pode rodar os testes:
```
(nomeDoAmbiente)..> python manage.py test
```
{
    "name": "titan"
    "packages": [
        {"name": "Django", "version": "3.2.5" },  // Usou a versão mais recente
        {"name": "graphene", "version": "2.0" }   // Manteve a versão especificada
    ]
}
```
