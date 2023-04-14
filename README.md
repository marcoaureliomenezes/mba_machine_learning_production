# Repósitório de trabalho do MBA Machine Learning Production

Esse repositório tem por objetivo armazenar de forma pública atividades desenvolvidas durante os estudos do MBA Machine Learning Production.

## 1 - ESBD1 Entregável 1

Texto sobre entregável 1 do módulo 1. Exploração de estruturas de dados e análise de performance destas em relação a complexidade para realização de certas operações.

<hr>

## 2 - ESBD1 Entregável 2

Texto sobre entregável 2 do módulo 1. Busca em grafo e analise de passos para encontrar número médio de conexões entre uma rede de pessoas como relacionamento entre si.

<hr>

## 3 - ESBD2 Entregável 1

Atividade a ser entregue até a data de 15-04-2023, referente ao tema Design Patterns e os padrões Singleton e Strategy.

### 3.1 - Descrição do problema

Suponha um sistema de geração de rotas seguras. O App deve gerar uma rota que se classifica em “altamente segura”, “segura” e “aceitável”. Como a rota deve/pode ser alterada à medida que o pedestre caminha, o sistema deve ser capaz de trocar o nível
de segurança da rota em tempo de execução. Assim, ora a rota se caracteriza como “altamente segura”, ora como “segura” e ora como “aceitável”.

- Elabore um projeto que reflita essa dinamicidade do sistema.
- Como a memória do dispositivo é limitada, deve-se cuidar para que não haja sobrecarga de objetos desnecessários em memória.

Forma de resolução:

- Diagrama de classe UML
- Trechos de código (pseudo-código) das partes importantes

### 3.2 - Análise do problema

O problema de geração de rotas apresentado acima pressupõe que existam rotas armazenadas em algum lugar. Em uma modelagem para esses tipos de problema é comum utilizar-se de modelagem em grafos.
Em uma das modelagens possíveis é possivel atribuir aos vertices localidades específicas e dizer que há conexão entre eles por meio de arestas. Como o problema trabalha com rota de pedestres é plausível considerar que as conexões são bidirecionais.

Assim sendo, na implementação de uma simulação do problema e sua solução levantou-se a hipótese das seguintes entidades:

- Para um problema modelado em grafos, nada mais natural do que a criação de uma classe que represente os grafos. Neste trabalho, essa classe foi denominada **Graph** e está inserida no módulo graph_generator.py.

- Para modelagem do grafo como proposto na descrição do problema, faz sentido atribuir aos vértices uma entidade que representa uma localização. Essa localização é composta pelos atributos uid e is_safe, representando o id de uma localidade e se ela é segua ou não. Essa entidade está implementada na atividade por meio da classe **Location**, inserida do módulo graph_generator.py.

- A aplicação principal foi denominada neste trabalho como assistente de caminhadas está implementada na classe **WalkAssistent**,inserida no módulo **walk_assistent.py**. Em suas atribuições está guardar posições atual e desejada, e traçar uma rota que liga as posições conforme diferentes estratégias. A forma como essas estratégias são implementadas, afim de atender ao requisito de dinamicidade do sistema é com o emprego do padrão de projeto strategy. Esse padrão tem por finalidade aplicar diferentes estratégias para implementar determinada funcionalidade e essas estratégias são implementadas fora da classe.

- Para suportar a implementação de diferentes estratégias, que pelo padrão estrategy estarão implementados em diferentes 3 classes concretas (**HighlySafetyRouter**, **SafetyRouter** e **AcceptableRouter**) e herdam a mesma classe abstrata (Router). estão implementadas no módulo **router.py**. Cada uma das classes concretas possui o método **logic_trace_route** que implementa a lógica que define como os 3 diferentes tipos de roteamento se comportam. Essas 3 lógicas serão exporadas mais a seguir.

- Para atender ao requisito de não sobrecarregar a memória com objetos desnecessários, foi analisado no problema que objetos que correm o risco de serem instanciados várias vezes tem maior probabilidade de vir das classes que definem estratégia. Dessa forma elas foram definidas como singleton.

### 3.3 - Estratégias levantadas que correspondem a rotas “altamente segura”, “segura” e “aceitável”

Como não foi definido o que distingui essas 3 classificações de rota, foi necessário que se estipulasse estratégias que se encaixassem nos termos e pudessem ser implementadas com os recursos disponíveis. Dessa forma foram definidas as seguintes estratégias:

- **Rota Altamente Segura**: Uma rota altamente segura remete a um caminho entre a origem e o destino, onde todos os nós 
estão marcados como não seguros (atributo is_safe marcado como True).

- **Rota Segura**: A rota segura aqui considera algum nível de imprecisão na aferição de se um ponto é seguro ou não. Na implementação foi considerada a seguinte lógica. Na busca por um caminho, tem a probabilidade de 70% de o roteador analisar aquele ponto. Caso o ponto seja analisado, serão considerados validos apenas caminhos seguros. Caso não seja analisado, o caminho pode ser roteado sendo seguro ou inseguro.

- **Rota Aceitável**: Implementa a mesma lógica da rota segura. Porém a chance de verificar a segurança de uma localização no momento que o gerador de rotas está traçando uma rota é de 40%.

