## CDC MySQL 

Requirements:
Python 3.8+

## Introdução
Através da técnica Change Data Capture é possível trafegar e replicar informações oriundas de bancos de dados em tempo real.
Utilizando um canal de comunicação aberto permanentemente, o banco de dados é capaz de disparar Logs de eventos ocorridos 
que podem ser tracionados de acordo com a necessidade da ocasião, seja replicar o dado em outra base, seja para construir
um datalake, por exemplo.

## Lógica de funcionamento
O canal banco de dados->Aplicação é mantido aberto permanentemente através de um loop do tipo While True, dessa forma,
enquanto a aplicação estiver de pé esta é capaz de consumir a stream de dados publicada pelo banco.
A lógica principal é iniciada através do arquivo __main__ e sua arquitetura lógica está contida na pasta 'services'

## A estruturação de tabelas
Para cada transação realizada no banco, a aplicação recebe um Log do evento e o reestrutura  baseado em um mapa de tabelas 
com uma relação DE-PARA. Ou seja, para cada tabela de um Schema supervisionado pela aplicação existe um objeto ORM
reponsável por traduzir e dirir para nova base de dados.

Foi utilizado a bibliotera ORM SQLAlchemy
Os modelos estão descritos na pasta 'models'

## Logs e Erros CornerCase
A aplicação também conta com um (pseudo)sistema de logs dirigido para um servidor Elasticsearch, reponsável por armazenar
as informações de execução da aplicação.

A aplicação foi estruturada para ser capaz de (pseudo)enviar notificações para canais de suporte específicos caso aconteça
algum erro oriundo de algum CornerCase não amparado pela lógica inicial estabelecida em seu desenvolvimento. Dessa forma
a equipe de suporte/RunTheBusiness/Desenvolvedor responsável pode atuar mais rapidamente na manutenção e evolução do código,
diminuindo o agrave de problemas.

## Deployment
A aplicação foi construida com o intuito de ser encapsulada em um container Docker, dessa forma, pode ser gerenciada por
servidores Kubernetes e afins. as configurações estão no arquivo Dockerfile.

As dependencias necessárias estão no arquivo requirements.txt
Para instalá-las, execute o comando pip instal -r requirements.txt

# Tabelas Dimensão, Tabelas Fato, StarSchema
- Para a resolução do problema proposto, foi considerado que os datasets incrementais estariam em um banco de dados relacional MySQL.
Cada uma das tabelas do foi considerada como uma tabela dimensão para a formação de um novo datalake, onde, a partir 
dessas tabelas dimensão foi possível construir tabelas fato, originando assim um datalake no padrão StarSchema.
- As informações das tabelas fato foram agregadas de forma ampla o suficiente para que o analista consiga sumarizar
  os dados da forma que melhor lhe agrade. Vale ressaltar que as agregações podem variar de acordo com o direcionamento do viés da pesquisa.
  Exemplos em imagem na raiz do projeto.
- As tabelas fato foram resolvidas no lado do banco de dados através de Views advindas dos relacionamentos das tabelas dimensão.
A depender do volume das tabelas dimensão e pensando na performance das consultas dos analistas de dados que irão consumir
informações dessas tabelas, é possível adicionar Index às tabela e, também, criar-se Materialized Views, otimizando assim
a performance das queries.

Caso seja necessário adicionar mais Schemas para serem gerenciados pela aplicação, é possivel realizar o processamento
em processamentos paralelos através de Threads.

## Pontos Importantes
Foram achados dados Homonimos de cidades no dataset de geolocation. Considerando que é uma base de dados incremental,
a fonte de dados deveria, na melhor das opções, ser normalizada na entrada para evitar problemas dos dados 
no datalake. Devido a estratégia utilizada é inviável tratar tais situações no momento do tráfego do dado. Entretanto, 
outras estratégias podem ser utilizadas em conjunto para o tratamento dos dados. Pode-se utilizar da tecnica Levenstein
para normalização de strings homonimas. Tal tecnica pode ser utilizada antes que o dado chegue no datalake com a implementação de
um middleware que trate dessas transformações pontuais. Este middleware pode ser uma API rest triggada por um adapter
que consuma mensagens publicadas por esta aplicação em um tópico/fila. Pode-se também aplicar rotinas de normalização
através dos chamados CronJobs.

