# Integrantes
Augusto Koshiyama Bento RA: 10389981

Gabriel Moreira Cabral RA: 10332634

# Projeto Lab Conversão PDF
Este tutorial possui um conjunto de serviços que fazem a manipulação de arquivos em PDF. Esses serviços incluem logs, redução de resolução para PDF e o ponto principal que é a conversão de PDF para TXT. Os serviços são implementados em um contêiner Docker e posteriormente separado para ajudar o processo.












## Executando o projeto

Para executar o projeto, siga estes passos:

1. Clone o repositório para a sua máquina local:

   ```bash
   git clone https://github.com/enzomazocorodrigues/pdf-converter.git
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

#### Usando o PDF to TEXT

```bash
curl -X POST -H "Authorization: your_pdftotxt_token" -F "file=@/caminho/para/seu/arquivo.pdf" http://localhost:5001/upload
```

#### Usando o PDF Reducer

```bash
curl -X POST -H "Authorization: your_pdftotxt_token" -F "file=@/caminho/para/seu/arquivo.pdf" -F "resolution=default" http://localhost:5002/upload
```

#### Baixando os logs

```bash
curl http://localhost:5003/
```
