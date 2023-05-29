Recomendação de Culturas na Agricultura de Precisão
Este projeto tem como objetivo desenvolver um modelo preditivo para recomendar as culturas mais adequadas para crescimento em uma determinada fazenda, utilizando técnicas de Agricultura de Precisão. O conjunto de dados utilizado foi obtido do Kaggle, disponível em Crop Recommendation Dataset.

Contexto
A agricultura de precisão está em tendência hoje. Ajuda os agricultores a tomarem decisões informadas sobre a estratégia agrícola. Aqui, apresento-lhe um conjunto de dados que permitiria aos usuários construir um modelo preditivo para recomendar as culturas mais adequadas para crescer em uma determinada fazenda com base em vários parâmetros. Este conjunto de dados foi construído aumentando os conjuntos de dados de chuvas, clima e fertilizantes disponíveis para a Índia.

Campos de Dados
Os campos de dados são:

N: relação de teor de nitrogênio no solo
P: proporção de conteúdo de fósforo no solo
K: relação do teor de potássio no solo
temperature: temperatura em graus Celsius
humidity: umidade relativa em %
ph: valor de pH do solo
Arquitetura do Projeto
O modelo de recomendação de culturas foi desenvolvido seguindo uma arquitetura distribuída, utilizando a biblioteca ZeroMQ para comunicação assíncrona entre os nós. A arquitetura consiste em dois nós principais: o nó de treinamento (train) e o nó de previsão (predict). A comunicação entre esses nós é realizada por meio do ZeroMQ, permitindo a troca de mensagens entre os processos distribuídos.

Além disso, os modelos treinados são armazenados no bucket "models" no MinIO, que é uma instância local do Amazon S3. Isso permite o armazenamento dos artefatos para acesso futuro.

Vantagens e Limitações
As vantagens da arquitetura escolhida são:

Escalabilidade: possibilita o treinamento de modelos com grandes volumes de dados (big data) e a realização de previsões em tempo real para um grande número de solicitações.
Paralelismo: distribui o trabalho em vários nós de treinamento, permitindo o treinamento de modelos em paralelo, desde que um não dependa da saída do outro.
Flexibilidade e Tolerância a falhas: a arquitetura distribuída permite adaptar o sistema a diferentes necessidades e é capaz de lidar com falhas em nós individuais.
No entanto, as limitações da arquitetura distribuída incluem a complexidade de gerenciamento de comunicação assíncrona entre os nós e a latência.

Licença
Este projeto é fornecido sob a licença MIT. Leia o arquivo LICENSE para obter mais informações.