# MAgPy Pedro

Neste repositório você encontra a descrição de uso da API de versionamento de 
pacotes usados em projetos Python, ela é últil para orientar o versionamento
das bibliotecas usadas na criação de um projeto.

## Caso de uso

Imagine que uma equipe de programadores usa vários módulos na criação de projeto!
É bem provável que durante o desenvolvimento um ou mais desenvolvedor sinta
a necessidade de verificar se os pacotes usados são válidos ou não de acordo com
a API do [PyPI](https://pypi.org/) ou qual a versão ultilizar.

## Como usar

Acesse: 
Você deve desenvolver a MagPy, uma API REST que gerencia uma coleção de 
projetos. Cada projeto tem um nome e uma lista de pacotes. Cada pacote tem um 
nome e uma versão.

O cadastro de um projeto recebe o nome e a lista de pacotes. Cada pacote da 
lista precisa obrigatoriamente especificar um nome, mas a versão é opcional.

Sua API deve validar o projeto cadastrado: todos os pacotes informados devem
estar cadastrados no [PyPI](https://pypi.org/). Portanto você deve verificar o
nome e a versão do pacote.

Quando o pacote vem apenas com o nome, sua API deve assumir que é preciso usar
a última versão publicada no [PyPI](https://pypi.org/).

Abaixo, alguns exemplos de chamadas que serão feitas nessa API:

```
POST /api/projects
{
    "name": "titan"
    "packages": [
        {"name": "Django"},
        {"name": "graphene", "version": "2.0"}
    ]
}
```
O código HTTP de retorno deve ser 201 e o corpo esperado na resposta é:
```
{
    "name": "titan"
    "packages": [
        {"name": "Django", "version": "3.2.5" },  // Usou a versão mais recente
        {"name": "graphene", "version": "2.0" }   // Manteve a versão especificada
    ]
}
```

Se um dos pacotes informados não existir, ou uma das versões especificadas for
inválida, um erro deve ser retornado.

Para uma chamada semelhante ao exemplo abaixo:
```
POST /api/projects
{
    "name": "titan"
    "packages": [
        {"name": "pypypypypypypypypypypy"},
        {"name": "graphene", "version": "1900"}
    ]
}
```
O código HTTP de retorno deve ser 400 e o corpo esperado na resposta é:
```
{
    "error": "One or more packages doesn't exist"
}
```

Também deve ser possível visitar projetos previamente cadastrados, usando o
nome na URL:
```
GET /api/projects/titan
{
    "name": "titan"
    "packages": [
        {"name": "Django", "version": "3.2.5" },
        {"name": "graphene", "version": "2.0" }
    ]
}
```

E deletar projetos pelo nome:
```
DELETE /api/projects/titan
```

| ⚠️ | Sua solução deve usar a [API pública do PyPI](https://warehouse.readthedocs.io/api-reference/json.html). Não use outro caminho pra buscar as informações necessárias |
| --- | --- |


## Esqueleto

Este repositório vem com um esqueleto para iniciar o projeto. Ele já tem 
algumas partes implementadas e está pronto para o deploy na [Heroku](https://www.heroku.com/).

Conforme detalhado na próxima seção deste README, nós iremos avaliar a sua API
publicada nessa plataforma, então é recomendado que você use este esqueleto 
como base para a sua solução. 

Usando esta base, você precisará:

1. Fazer uma cópia deste repositório
2. Implementar sua solução
3. Criar uma conta gratuita no Heroku
4. Criar um novo app
5. Seguir as instruções da seção _Deploy using Heroku Git_
6. Adicionar o usuário `jobs@instruct.com.br` como colaborador do app

Fique à vontade para fazer as alterações que julgar necessárias no código
disponibilizado.

## Avaliação

Num primeiro momento não olharemos o seu código. O projeto será testado de 
forma automatizada pra checar se implementa a API especificada acima.

Você deve codificar seu projeto em Python e fazer deploy usando os recursos 
disponibilizados nos _Frees Tiers_ da [Heroku](https://www.heroku.com/).

Quando finalizar a implementação, adicione o usuário com e-mail
`jobs@instruct.com.br` como colaborador do app publicado até o fim do prazo
estipulado. Isso nos garante acesso ao endereço em que sua API está publicada,
para seguir com os testes automatizados.

| ⚠️ | Você deve adicionar o usuário com e-mail `jobs@instruct.com.br` no app publicado no Heroku! Não é necessário adicionar acesso ao código fonte num repositório do GitHub. |
| --- | --- |

Nós executaremos dois conjuntos de testes na sua API:

1. Testes básicos (abertos)
2. Testes avançados (fechados)

Se a API não passar nos testes básicos, faremos mais duas tentativas. Se
mesmo assim ela não passar nos testes básicos nós encerramos os testes.

Se a API passar nos testes básicos e não passar nos testes avançados, faremos
mais duas tentativas. Se mesmo assim ela não passar nos testes avançados nós
encerramos os testes.

Se a API passar pelos testes avançados nós conferimos superficialmente o seu 
código para identificar problemas; no entanto você provavelmente já garantiu a 
sua participação na próxima etapa.

Os testes básicos estão disponíveis neste repositório no arquivo
`tests-open.js`. Use-os durante o desenvolvimento para avaliar se a sua API 
está correta. Como explicado acima, você **não passará** para a próxima etapa 
se a sua solução não atender todos os testes desse arquivo. 
**Use os testes para guiar o desenvolvimento da solução.**

Você pode executar esses testes com o [k6](https://k6.io/). Para instalar o k6
basta [baixar o binário](https://github.com/loadimpact/k6/releases) para o seu
sistema operacional (Windows, Linux ou Mac).

Para rodar os testes abertos, especifique a variável de ambiente "API_BASE"
com o endereço base da API testada.

Exemplo de aplicação rodando no localhost na porta 8080:
```
k6 run -e API_BASE='http://localhost:8080/' tests-open.js
```

## Recomendações finais

- Não deixe para fazer na última hora
- Atente-se para boas práticas da linguagem, siga a PEP 8
- Considere escrever testes automatizados
- Escreva documentação
    - Mude este README. Descreva sua aplicação, explique o que ela faz e porque é útil.
    - Explique como testar a aplicação
    - Considere documentar sua API com Swagger UI ou ReDoc
- [Não teste apenas o _Happy Path_](https://cucumber.io/blog/test-automation/happy-unhappy-paths-why-you-need-to-test-both/)

---

**Boa sorte!**
