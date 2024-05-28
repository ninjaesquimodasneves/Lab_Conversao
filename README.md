# Integrantes
Augusto Koshiyama Bento RA: 10389981

Gabriel Moreira Cabral RA: 10332634

# Projeto Lab Conversão PDF
Este tutorial possui um conjunto de serviços que fazem a manipulação de arquivos em PDF. Esses serviços incluem Logs, redução de resolução para PDF e o ponto principal que é a conversão de PDF para TXT. Os serviços são implementados em um contêiner Docker e posteriormente separado para ajudar o processo.

# Serviços a Serem Utilizados

## 1. Logs
Os Logs têm a função de registrar as operações realizadas pelos serviços PDF Redutor e PDF para TEXT. Além disso, eles mantêm um registro detalhado dessas atividades e podem emitir relatórios conforme necessário. Os Logs também ajudam a monitorar o desempenho e a resolver problemas rapidamente.

## 2. PDF Reducer
Serviço responsável pela redução da resolução de arquivos PDF. O usuário faz o upload do arquivo PDF, que é processado pelo software Ghostscript para ajustar a resolução conforme a preferência selecionada. Após a otimização, o arquivo é enviado de volta ao usuário. 

## 3. PDF to Txt
Transforma arquivos PDF em texto, o usuário carrega um arquivo PDF, que é processado para extrair o texto contido. O texto extraído é então enviado de volta ao usuário em um arquivo .txt.

# Executando o Projeto

A seguir terá um passo a passo de como executar o laboratório:

Abra um terminal e execute o comando abaixo para clonar o repositório do GitHub para a sua máquina local:

   ```bash
   git clone https://github.com/ninjaesquimodasneves/Lab_Conversao.git
   ```
Após a clonagem, navegue até o diretório do projeto:

   ```bash
   cd Lab_Conversao
   ```
Execute:

   ```bash
   docker-compose up --build
   ```

Vamos agora testar os dois serviços.

### PDF to TEXT

```bash
curl -X POST -H "Authorization: Bearer SEU_TOKEN" -F "file=@seuarquivo.pdf" http://localhost:5001/upload
```

### PDF Reducer

```bash
curl -X POST -H "Authorization: Bearer SEU_TOKEN" -F "file=@seuarquivo.pdf" -F "resolution=default" http://localhost:5002/upload
```

### Baixar Logs

```bash
curl http://localhost:5003/
```

# Contribuições

**Augusto Koshiyama Bento**: implementou o serviço de conversão de PDF para TXT, desenvolveu o webservice para dois tipos de serviços, configurou a autenticação com token, desenvolveu a estrutura de log e a página web para o serviço de conversão.

**Gabriel Moreira Cabral:**: implementou o serviço de redução de resolução de arquivos PDF, desenvolvou o webservice para os dois tipos de serviços, ajudou configurou a autenticação com token, desenvolveu a página web para o serviço de redução de resolução.
