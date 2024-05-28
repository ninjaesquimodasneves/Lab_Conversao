# Integrantes
Augusto Koshiyama Bento RA: 10389981

Gabriel Moreira Cabral RA: 10332634

# Projeto Lab Conversão PDF
Este tutorial possui um conjunto de serviços que fazem a manipulação de arquivos em PDF. Esses serviços incluem Logs, redução de resolução para PDF e o ponto principal que é a conversão de PDF para TXT. Os serviços são implementados em um contêiner Docker e posteriormente separado para ajudar o processo.

# Serviços a Serem Utilizados

## 1. Logs
O Logs tem a função de registrar as operações realizadas pelos serviços PDF Redutor e PDF para TEXT. Além disso, ele tem um registro dessas operações e pode emitir relatórios que forem precisos.

## 2. 

# Configurações Antes de Executar
## Docker

Certifique-se de que você tem o Docker instalado na sua máquina. Você pode fazer o download e instalar o Docker a partir do [site oficial do Docker](https://www.docker.com/get-started).

## Docker Compose

Se o seu projeto utiliza o Docker Compose, você também precisará instalá-lo. O Docker Compose geralmente é incluído com o Docker Desktop. Mais informações sobre a instalação podem ser encontradas na [documentação oficial do Docker Compose](https://docs.docker.com/compose/install/).

# Executando o Projeto

Para executar o projeto, siga estes passos:

1. Clone o repositório para a sua máquina local:

   ```bash
   git clone https://github.com/ninjaesquimodasneves/Lab_Conversao.git
   ```

1. Navegue até o diretório do projeto:

   ```bash
   cd pdf-converter
   ```

1. Construa e execute os containers:

   ```bash
   docker-compose up --build
   ```

## Testando os Serviços

Você pode testar os serviços utilizando ferramentas como `curl`, Postman ou até mesmo um browser.

### Usando o PDF to TEXT

```bash
curl -X POST -H "Authorization: your_pdftotxt_token" -F "file=@/caminho/para/seu/arquivo.pdf" http://localhost:5001/upload
```

### Usando o PDF Reducer

```bash
curl -X POST -H "Authorization: your_pdftotxt_token" -F "file=@/caminho/para/seu/arquivo.pdf" -F "resolution=default" http://localhost:5002/upload
```

### Baixando os logs

```bash
curl http://localhost:5003/
```

# Contribuições

**Augusto Koshiyama Bento**: leitura dos artigos; auxílio na implementação do código e das rotas dos produtos; criação e composição do tutorial

**Gabriel Moreira Cabral**: leitura dos artigos; implementação do código e das estratégias de cache.
