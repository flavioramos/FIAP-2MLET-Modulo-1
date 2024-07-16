# API para consumo de dados da Vitivinicultura brasileira

API para disponiblizar dados extraídos de CSV do site da Embrapa.

## Instalação

1. **Clonar o repositório:**

   git clone git@github.com:flavioramos/FIAP-WineScrapperAPI.git

2. **Instalar dependências:**

   Recomenda-se criar um ambiente virtual antes de instalar as dependências.

   pip install -r requirements.txt

## Uso

1. **Realizar download e cache dos dados:**

   Execute o seguinte comando:

   flask build-cache

   Realizará o download dos CSVs, caso já não estejam disponíveis no diretório /cache.
   
1. **Inicialize o banco de dados:**

   Execute o seguinte comando:

   flask init-db

   Com isso o usuário padrão será criado (admin@example.com), e os dados serão estraídos do CSV para o SQLite.

1. **Iniciar a API:**

   flask run

   Isso iniciará o servidor localmente em `http://localhost:5000`.

2. **Endpoints e documentação:**

  Swagger: 'http://localhost:5000/apidocs'
  Postman: '/postman/FIAP - WineScapper.postman_collection.json'
  

## Contribuição

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/licenses/MIT).
