---
title: Método Kanban: um guia (quase) completo - Target Teal
author: Davi Zimmer
url: https://targetteal.com/blog/metodo-kanban/
hostname: targetteal.com
description: O método Kanban foi concebido como um caminho alternativo à agilidade organizacional. Ao invés de grandes mudanças, o Kanban propõe uma abordagem evolucionária, onde pequenas melhorias são integradas na prestação de um serviço ou desenvolvimento de um produto.
sitename: Target Teal
date: 2018-03-19
categories: ['Ágil']
---
O método Kanban foi concebido como um caminho alternativo à agilidade organizacional. Ao invés de grandes mudanças, o Kanban propõe uma abordagem evolucionária, onde pequenas melhorias são integradas na prestação de um serviço ou desenvolvimento de um produto.

Nascido dentro do Sistema Toyota de Produção (TPS), o kanban (com k minúsculo) era um cartão utilizado para sinalizar conclusão de etapas do processo e tornar o fluxo puxado. Mais tarde, David J. Anderson criou o método Kanban (com K maiúsculo) e popularizou o seu uso no desenvolvimento de produtos e serviços. Neste guia detalharemos o funcionamento deste segundo. ;)

- Entendendo um sistema Kanban
- Sistema empurrado
- Sistema puxado
- Os princípios básicos do método Kanban
- As 6 práticas gerais de um sistema Kanban
- Quando usar o método Kanban?
- Vantagens sobre o Scrum
- Como implementar um sistema Kanban
- Elementos de um sistema Kanban
- Métricas de um sistema Kanban
- As limitações do Kanban
- Método Kanban & Autogestão (O2)
- E tem muito mais que ainda não está aqui

## Entendendo um sistema Kanban

Um sistema Kanban é composto por um fluxo de valor, onde unidades de trabalho trafegam da esquerda para a direita. Cada etapa do processo adiciona mais valor ao item, sendo que quando ele chega ao final do processo, ele está “concluído”. Esse fluxo de valor pode ser o desenvolvimento de um software, a prestação de um serviço (como atendimento ao cliente) ou até a criação de um produto físico.

Vamos supor que fazemos parte de um time de desenvolvimento de um aplicativo. O nosso processo atual tem algumas etapas, que podemos mapear na forma de colunas “Backlog”, “Design”, “Desenvolvimento”, “Testes”, “Deploy” (implantação) e “Pronto”. Neste quadro Kanban, as unidades de trabalho representam coisas que geram algum benefício ao cliente/usuário final, como novas funcionalidades, correção de defeitos ou melhorias na interface do produto. O valor é gerado somente quando um item alcança a última etapa:

Apesar de conter etapas sequenciais e cartões, isso ainda não é um sistema Kanban. Vamos fazer mais duas mudanças para tornar o fluxo puxado:

- Dividir as colunas intermediárias em dois estágios: “fazendo” e “pronto”;
- Adicionar limites de trabalho em progresso

Feitas essas mudanças, o nosso quadro ficaria assim:

Vamos analisar como isso funcionaria na prática. Supondo que você é o especialista em Design do time e que você está trabalhando em uma funcionalidade. Após você concluir a sua atividade, você movimenta o cartão para a etapa “Pronto” da coluna “Design”. Se um desenvolvedor (que atua na etapa “Desenvolvimento”) está livre, ele pode perceber que você sinalizou a conclusão da sua parte e então “puxar” o cartão para a etapa “Fazendo” da coluna “Desenvolvimento”.

Repare que o limite “1” da coluna “Design” é válido tanto para “Fazendo” quanto “Pronto”. No caso acima, temos um item que foi concluído pelo Designer, mas ainda não foi puxado. O que o Designer faz nesse caso? Nada. Ele apenas aguarda alguém puxar o item para Desenvolvimento. Nesse caso o slot seria liberado e ele poderia trabalhar em outro item.

Claro que na prática se não houver slot disponível o membro do time não vai ficar simplesmente parado. Em um sistema Kanban, estimulamos as pessoas a olharem para o fluxo como um todo e buscarem formas de aumentar a vazão. Pode ser que o Designer possa ajudar alguém no Desenvolvimento. Pode ser que ele use esse tempo para pensar em melhorias. O que importa é não ficar simplesmente trabalhando na própria função, pois isso aumentaria o estoque e prejudicaria o fluxo.

Parece contra intuitivo, mas a teoria das filas comprova. A ociosidade no fluxo aumenta a vazão. Para entender os porquês, você vai precisar estudar um pouco de matemática (esse livro é um bom começo).

Como os itens são puxados apenas quando há capacidade disponível, raramente há sobrecarga. Isso é que o chamamos de sistema puxado. Ele é um contraste à forma tradicional de trabalhar, que chamamos de sistema empurrado. Vamos entender a diferença entre os dois para compreender melhor um sistema Kanban. ;)

## Sistema Empurrado

Um sistema empurrado é aquele em que a produção é baseada na demanda, sem respeito à capacidade do sistema. Em geral, no paradigma empurrado tenta-se produzir o máximo possível e em grandes lotes, sem considerar a real necessidade dos clientes. Neste tipo de abordagem, a estratégia de marketing e vendas também é focada em vender e “empurrar” os produtos para o cliente.

No nosso exemplo do time de desenvolvimento de um aplicativo, um gestor poderia atribuir diversas tarefas aos membros do time, exigindo que todos se mantivessem ocupados e trabalhando 100% do tempo, cada um na sua função. Além disso, é provável que esse time desenvolvesse um grande número de funcionalidades inúteis e que não gerassem valor para o cliente final. Afinal, todos estariam preocupados em fazer bem a sua função, e não em entregar valor para o cliente.

Os principais efeitos colaterais de um sistema empurrado são sobrecarga, demoras nas entregas, grandes lotes e burnout das pessoas.

## Sistema Puxado

Um sistema puxado é aquele em que os participantes “puxam” o trabalho quando há capacidade disponível para executá-lo. Isso é possível quando atribuímos limites para as unidades de trabalho em progresso. Um sistema puxado nunca irá sofrer com sobrecarga se os limites forem estabelecidos corretamente. Nesse paradigma busca-se atingir um passo sustentável, ou seja, um equilíbrio entre a capacidade do time e o que é demandado dele.

O método Kanban é apenas uma forma de construir um sistema puxado. Outras variações também existem, como CONWIP e DBR.

Agora que conhecemos a diferença entre empurrado e puxado, vamos entender um pouco mais sobre os princípios e propriedades básicas de um sistema Kanban.

## Os princípios básicos do método Kanban

Em seu livro *Kanban: successful evolutionary change for your technology business*, David J. Anderson descreve os princípios básicos do método Kanban:

**Comece com o que você tem hoje**. O método Kanban propõe uma abordagem evolucionária e incremental. Por mais que você esteja muito insatisfeito com a forma como as coisas são feitas no processo atual, não mude tudo logo no início. Fazer grandes mudanças pode aumentar a resistência das pessoas, além de ser muito arriscado para a organização.

**Busque mudanças incrementais e evolucionárias**. Depois de partir do seu processo atual, busque pequenas mudanças. Formule hipóteses com base na sua observação do comportamento do sistema. Seja curioso e faça experimentos.

Vamos supor que o seu sistema possui uma coluna onde um grande documento é produzido que detalha o que deve ser feito. Talvez você desconfie que o nível de detalhe seja grande demais e que isso é um provável desperdício. Formule a hipótese: *Se nós simplificarmos o documento, teremos uma redução do Lead Time do processo.* Você pode estar certo ou não. Faça um experimento, meça os resultados e compare.

**Respeite o processo atual, papéis, responsabilidades e títulos**. É provável que na organização em que você está implementando o método Kanban existam cargos e autoridades definidas. Talvez essa estrutura esteja atrapalhando o fluxo, na sua visão. Mas ao mesmo tempo, é também muito provável que boa parte dos processos atuais simplesmente funcione. Por isso é importante respeitar o que já está posto e perseguir a melhoria contínua a partir disso.

## As 6 práticas gerais de um sistema Kanban

David J. Anderson descreve 6 práticas gerais das implementações de sucesso do método Kanban. Podemos dizer que sem elas, você ainda não está fazendo “Kanban”. Por isso que dissemos que o quadro inicial (que não tinha limites de trabalho em progresso) ainda não poderia ser considerado um sistema Kanban: ele falhava em uma das 6 práticas gerais.

As 6 práticas são:

**Visualize o fluxo de trabalho**. Você não pode gerenciar o que não pode ver! E se tratando de trabalho do conhecimento, esta afirmação é ainda mais verdadeira. Na Toyota, o estoque excessivo de carros poderia ser facilmente visualizado, já que um carro é um produto físico. Mas e todas as funcionalidades de um sistema que foram começadas, mas não terminadas? Ou todos os tickets de atendimento que foram abertos, lidos, mas não respondidos? O trabalho do conhecimento é intangível. É por isso que precisamos estabelecer formas tangíveis de visualizar o fluxo e as unidades de trabalho.

**Limite o trabalho em progresso**. Se você não estabelecer limites para o trabalho em andamento, é muito provável que você ainda esteja operando um sistema empurrado. Em geral, todas as etapas em um fluxo são limitadas, com exceção da última. Estabelecer limites vai impedir o acúmulo de estoque e também vai manter o Lead Time estável. Em geral, quanto mais itens houverem em andamento, maior é o tempo de entrega.

**Gerencie o fluxo**. No Kanban, focamos os esforços na otimização do sistema como um todo. A gestão tradicional empurrada foca em manter todas as pessoas ocupadas e gerenciar o trabalho delas. Isso não é feito no método Kanban. Se tentarmos otimizar uma parte do sistema (o trabalho de um desenvolvedor), isso provavelmente levará a uma situação sub-ótima globalmente. Esse fenômeno chama-se otimização local. Leia mais sobre como isso acontece com as metas.

**Torne as políticas de processo explícitas**. Ao trabalhar com um fluxo Kanban, você vai perceber que muitas regras de processos, papéis e definições não são claras para os participantes do fluxo. Vai surgir muita confusão sobre o significado de uma determinada coluna do fluxo, por exemplo. É importante que você aproveite essas oportunidades para esclarecer as políticas do processo e torná-las explícitas. Isso significa registrá-las em algum local acessível para todos. Parte importante de jogar o jogo é conhecer as regras.

**Implemente ciclos de feedback**. Nenhum processo pode evoluir sem ciclos de feedback. David J. Anderson propõe alguns rituais específicos para retroalimentar o sistema e permitir com que os participantes se adaptem comparando a situação atual do processo com as expectativas das partes interessadas.

**Melhore colaborativamente**. No final, as limitações de trabalho em progresso irão introduzir desconfortos e iniciar conversas sobre o fluxo. O que se busca em um sistema Kanban é um fluxo suave e constante. No entanto, não é isso que vai acontecer no início. É importante estabelecer um processo de melhoria colaborativa, onde o grupo constrói um entendimento compartilhado sobre os problemas encontrados e a partir daí propõe experimentos para melhorar o fluxo.

## Quando usar o método Kanban?

Praticamente qualquer processo de desenvolvimento ou prestação de serviço pode ser melhorado com o método Kanban. No entanto, quanto maior e mais complexa a cadeia de valor desse produto/serviço, maior é o benefício em aplicá-lo.

Cadeias longas geralmente possuem muitas pessoas envolvidas, handovers e fontes de desperdício. Isso significa maiores oportunidades de melhoria. Por outro lado, se o processo for extremamente simples, provavelmente o esforço de aplicar o método é maior do que o benefício obtido.

## Vantagens sobre o Scrum

Na comunidade ágil, o Scrum é o principal “concorrente” do Kanban. A palavra concorrente está entre aspas, porque a comparação não é justa. Primeiro, porque são coisas diferentes. O Scrum é um *framework*, enquanto que o Kanban é um método. O primeiro é muito mais prescritivo e o segundo muito mais flexível.

Deixando essa diferença de lado, quando aplicados em desenvolvimento de produtos digitais, o Kanban tem as seguintes vantagens sobre o Scrum:

**Múltiplos focos**. O método Kanban permite múltiplos focos de atuação. Se o seu time dá manutenção em um produto legado, e ao mesmo tempo desenvolve um novo, isso não é problema para o Kanban. Já o Scrum exige um time dedicado para o desenvolvimento de um único produto, com um único Backlog.

**Entregas constantes**. O método Kanban trabalha com fluxo contínuo, enquanto que o Scrum usa Sprints com timebox. Ambas as abordagens permitem entregas constantes, mas o Kanban permite ciclos ainda menores que o Scrum.

**Mais evolutivo**. Por ser mais prescritivo, o Scrum pode exigir que a sua organização mude radicalmente. Por exemplo, um dos requisitos do time de desenvolvimento no Scrum é que ele seja pequeno, multidisciplinar e auto-organizado. Dependendo da sua estrutura organizacional, essa mudança pode exigir uma grande reengenharia. Já o método Kanban é bem enfático na melhoria incremental e diz: *comece onde você está*.

## Como implementar um sistema Kanban

Os princípios e as propriedades que vimos na seção anterior fornecem um caminho de implementação interessante. Segui-los em ordem já é um bom começo.

Por exemplo, o primeiro princípio é: **comece de onde você está**. Essa é uma boa dica. Não faça mudanças abruptas na implementação de um sistema Kanban logo de cara. Podemos ver também que a propriedade **limite o trabalho em progresso** vem depois de **visualize o fluxo de trabalho**. Isso também nos mostra que é importante primeiro enxergar o que está acontecendo na organização antes de sair aplicando as restrições, por mais que elas sejam “básicas”.

## Elementos de um sistema Kanban

Um sistema Kanban possui diversos elementos e práticas atreladas. Nesta seção, veremos os mais comuns. E o primeiro de todos é…

### Quadro Kanban

Sim, o quadro. Ele é uma forma simples de visualizar o andamento do fluxo e o progresso dos itens de trabalho, mas não a única. No seu livro, David J. Anderson descreve alguns exemplos de sistemas Kanban sem uso de um quadro

Atenção: ter um quadro Kanban não significa ter um sistema Kanban. Por exemplo, o uso de um quadro de tarefas (normalmente referido como quadro Kanban), é muito comum em times ágeis que praticam Scrum. Isso não implica necessariamente que há um fluxo puxado, com limites de trabalho em progresso e um processo de melhoria contínua estabelecido (o método Kanban).

### Cartões

Dentro do quadro, temos cartões que simbolizam unidades de trabalho. Ao usá-los em trabalhos do conhecimento, conseguimos tornar visível o “estoque”, que é normalmente intangível.

No método Kanban é importante visualizarmos o trabalho em progresso, porque ele é desperdício em potencial. Por exemplo, todas as telas que um designer desenhou, mas que ainda não foram implementadas no produto, podem se tornar “lixo” se a empresa mudar a sua estratégia de atuação e aquilo perder prioridade. Trabalho em andamento é dinheiro que já foi investido, mas que ainda não trouxe um retorno para a organização.

#### Atributos dos cartões

Normalmente um cartão em um quadro Kanban possui alguns atributos, além do nome ou número de identificação.

O atributo mais comum é o tipo do item, que é normalmente classificado como **valor**, **melhoria** ou **falha.** No desenvolvimento de software, podemos usar tipos como **nova funcionalidade**, **melhoria** **de interface **e **defeito**, por exemplo. Os tipos de item permitem analisarmos as métricas de forma segmentada, além de nos darem uma visão mais clara sobre a composição do fluxo.

Os tipos de item são frequentemente representados usando um código de cores. Veja esse vídeo de exemplo:

### Colunas do Quadro

Em um quadro Kanban, as colunas são normalmente utilizadas para representar as fases que um item de valor percorre, até ser concluído. Quanto mais a direita, mais valor e tempo foi investido.

Ao longo da sua jornada com o método Kanban, talvez você se depare com uma discussão se um cartão “deve voltar ou não” no fluxo. Imagine um cartão de uma funcionalidade X que está no fluxo acima. Vamos supor que ele está em “Testes”, mas o testador descobre que há um erro na funcionalidade que deve ser corrigido pelo desenvolvedor. Uma linha de pensamento defende que o item deve voltar para o estado que melhor representa. Outra diz que não, porque essas etapas não simbolizam “com quem está”, mas em qual estágio de valor o item se encontra.

Pessoalmente, prefiro a segunda opção por uma questão prática. Voltar o cartão tende a criar uma complicação no cálculo dos limites de trabalho em progresso. Veja esse vídeo do Buzon para mais detalhes.

### Raias do Quadro

Além das colunas, que são divisões horizontais, muitos quadros possuem “raias”, que são o equivalente vertical. As raias costumam ser usadas para destacar visualmente uma classe de serviço ou para alocar capacidade por tipo de item.

No exemplo acima, utilizamos uma raia especial para destacar a classe de serviço **urgente**.

### Limites de trabalho em progresso

Na introdução falamos sobre a importância dos limites de trabalho em progresso. Em termos de como montar o seu quadro, os limites podem ser estabelecidos por coluna, por subcoluna ou por raia. O quadro abaixo contém todos essas possibilidades.

A coluna “Design” possui um limite total de 1. Ou seja, podemos ter:

- 1 item em “Fazendo” e 0 itens em “Pronto”
- 0 itens em “Fazendo” e 1 item em “Pronto”

A coluna “Desenvolvimento” possui um limite total de 3 e um limite de 2 itens para a subcoluna “Fazendo”. A subcoluna “Pronto” não possui especificação de limite. Os seguintes cenários são permitidos:

- 2 itens em “Fazendo” e 1 item em “Pronto”
- 1 item em “Fazendo” e 2 itens em “Pronto”
- 0 itens em “Fazendo” e 3 itens em “Pronto”

Nessa forma de representação, tanto os limites para a coluna quanto a subcoluna devem ser respeitados simultaneamente. Ou seja, não poderíamos ter 3 itens em “Fazendo” (o limite da subcoluna é 2) e nem 2 em “Fazendo” e 2 em “Pronto” (o limite total é 3).

Note também que existe uma alocação por capacidade (falaremos mais abaixo), com limites especificados para as raias “Bugs” e “Features”. Nesse caso os limites se aplicam a toda a linha. Ou seja, não poderemos ter mais do que 7 itens em toda a linha de bugs (independentemente da coluna) e 5 itens em features. A soma dos limites das linhas (5 + 7 = 12) deve ser igual à soma dos limites das colunas (3 + 1+ 3 + 2 + 1 + 2 = 12).

### Políticas explícitas

Parte importante do processo de implementação de Kanban é tornar as regras do fluxo conhecidas por todos. Isso envolve explicitar muitas políticas que são normalmente implícitas nas organizações. Por explicitar, queremos dizer registrar (de forma escrita) e confirmar a compreensão com todos os envolvidos.

Esse processo dá a possibilidade da construção de um entendimento compartilhado sobre as restrições do sistema. Isso é muito importante, já que queremos envolver todos no processo de melhoria.

Não há um formato específico para escrita de políticas no Kanban, mas é possível trabalhar com os elementos papéis e restrições da O2 (mais informações na seção sobre autogestão).

Aqui vão alguns exemplos de políticas explícitas:

- Somente o Gerente de Produto pode promover um item de normal para urgente.
- Os limites das raias e das colunas devem ser respeitados simultaneamente.
- Se houverem itens urgentes, puxe-os antes dos normais.

### Classes de Serviço

Imagine a seguinte situação: o seu sistema Kanban está operando em capacidade máxima (todas as colunas atingindo os limites de trabalho em progresso) e de repente aparece um novo item com alto custo de oportunidade. Pode ser um defeito crítico, que se não for corrigido a tempo pode causar um grande prejuízo à organização. Ou pode ser uma nova funcionalidade, que se lançada antes do Natal (data de entrega), pode trazer um aumento de 20% na receita.

Se o seu fluxo está cheio, o que você faz? Mesmo que você coloque ele em primeiro lugar na sua fila de entrada, é provável que ele demore muito tempo para ser concluído. Você também não pode simplesmente aumentar os limites, porque isso iria contra as políticas já definidas.

Itens como os descritos acima normalmente aparecem nas piores horas, por isso ter uma forma de responder rapidamente é importante. É justamente essa a função das classes de serviço. Com elas, podemos oferecer tratativas diferentes a itens com essas características.

No quadro acima, temos uma marcação (a estrela) no item que define que ele possui a classe de serviço **urgente**. Como parte das políticas explícitas, poderíamos ter uma regra em que itens urgentes devem ser puxados primeiro e que podem exceder o limite de trabalho em progresso do sistema inteiro em 1. Poderíamos também incluir uma regra de que é possível ter no máximo 1 item urgente por vez, para não afetarmos muito o tempo de entrega dos outros itens.

Podemos também criar uma raia própria para as classes de serviço, para destacá-las visualmente:

Agora que já conhecemos os elementos básicos de um sistema Kanban, vamos falar de **métricas**.

## Métricas de um sistema Kanban

Na seção sobre as 6 práticas gerais do método Kanban, vimos que o foco deve ser em gerenciar o fluxo, não as pessoas. Só podemos melhorar continuamente se pudermos melhor observar o que acontece no processo atual. Para isso, utilizamos algumas métricas e diagramas. A seguir estão as mais comuns e importantes métricas de um sistema Kanban.

**Lead Time**. É o tempo decorrido desde que a demanda é registrada (item de trabalho) até a entrega final. No exemplo de desenvolvimento do aplicativo, o lead time de um item seria a diferença de tempo entre o momento que ele entra na coluna “Selecionados” e que ele chega na coluna de “Pronto” final. Onde é o “início” e o “fim” do seu fluxo varia de acordo com o contexto. Em desenvolvimento de produtos, geralmente é medido desde a concepção da ideia até o momento em que o cliente final pode usufruir do seu benefício.

Esta é uma das principais métricas de um sistema Kanban. Em geral, buscamos os menores Lead Times possíveis, para entregar rápido e obter feedback o quanto antes.

**Cycle Time e Reaction Time**. O tempo de reação e ciclo são complementos ao lead time. Perceba que no fluxo abaixo há uma fila de entrada chamada “Selecionados”. Ali são colocados um lote de itens a serem consumidos ao longo dos próximos dias. O tempo de reação é a diferença entre o momento que você começa a capturar o lead time (nesse fluxo, o momento em que entra em “Selecionados”) até o momento em que o item é puxado pela próxima coluna. Quanto maior o seu lote de reabastecimento (limite da coluna “Selecionados”), mais alto é o tempo de reação. É interessante acompanhar essa métrica para entender se os itens estão ficando muito tempo “parados” na fila de entrada. A diferença entre o tempo de reação e o lead time é tempo de ciclo. Veja abaixo:

Além disso, podemos medir o tempo de ciclo de um conjunto de colunas específicas, como indicado na figura (cycle time dev-testes).

**Vazão (throughput)**. Outra métrica importante é o throughput, ou vazão. Você pode colocar um limite de apenas um item por vez no seu fluxo. Isso tornaria o seu lead time muito pequeno, mas às custas dessa outra métrica importante, que chamamos de vazão. A vazão corresponde à quantidade de itens finalizados em um determinado período (como uma semana). Em geral, buscamos obter a maior vazão com o menor lead time possível. Por isso é importante acompanhar essa métrica juntamente com o lead time.

O método Kanban não possui um ciclo pré-definido (como o Scrum possui a Sprint), pois o fluxo corre continuamente. Ainda assim, é uma prática comum definir um período de coleta das métricas, onde você pode também medir a vazão. Por exemplo, vamos supor que você quer medir tudo a cada duas semanas. Ao final desse período, você poderia contabilizar a quantidade de itens na coluna “Pronto”, calcular o lead time médio do período e assim por diante.

**Composição do fluxo**. Como vimos nos elementos de um sistema Kanban, você pode designar diferentes “tipos” para os itens do seu quadro. O mais comum é analisar a quantidade de “novos itens de valor” (funcionalidades) vs a quantidade de “itens de defeito”. Esses diferentes perfis determinam a composição do fluxo, que você pode acompanhar ao longo do tempo:

**Diagrama de Fluxo Cumulativo (CFD)**. Outro diagrama fundamental para o seu fluxo é o CFD. Com ele você consegue identificar gargalos e olhar para a fluidez do seu processo. Leia esse post do Leonardo Campos sobre como ler e montar esse gráfico.

### Medindo o sistema, não as pessoas

Observe que nenhuma das métricas acima diz respeito ao trabalho dos indivíduos. O foco deve ser em melhorar o sistema como um todo, não as suas partes. Falando nisso, nem pense em utilizar essas métricas como parte de um sistema de avaliação de desempenho. Isso certamente arruinaria a colaboração e a melhoria contínua, que são parte fundamental do método Kanban.

## As limitações do método Kanban

O método Kanban é frequentemente reconhecido como parte do movimento ágil, sendo apenas uma entre diversas práticas conhecidas na comunidade. Existem algumas sombras do ágil em que os praticantes de Kanban também podem estar sujeitos. Além disso, o Kanban não vai te ajudar a resolver diversos problemas comuns de design organizacional, que listamos abaixo.

**O Kanban não define tomada de decisão**: O método Kanban não estabelece como as decisões de mudança no quadro ou no fluxo devem acontecer. Pelo contrário, ele diz inclusive que você deve respeitar a governança da organização para promover as mudanças. Se você procura maior responsividade e adaptabilidade, talvez precise de algum método de autogestão.

**O Kanban não estabelece papéis**: Diferentemente do Scrum que define um conjunto de papéis, o Kanban é silencioso nesse sentido. No entanto, pode ser importante definir melhor as expectativas sobre cada pessoa envolvida no fluxo de valor. Veja a seção sobre Organização Orgânica para saber como complementar o Kanban nesse aspecto.

**O Kanban pode ser demais para projetos simples**: Se você está querendo organizar tarefas ou projetos na sua organização que não possuem uma cadeia de valor complexa e com muita interdependência, talvez Kanban seja demais para o seu contexto.

Boa parte das limitações tem a ver com coisas que o método Kanban não foi destinado para resolver. Por isso tome cuidado para não depositar mais confiança no método do que ele próprio!

## Método Kanban & Autogestão (O2)

O método Kanban advoca uma evolução colaborativa e contínua. Isso tem tudo a ver com autogestão, que é um tema que gostamos muito aqui na Target Teal. Para não ter confusão, vamos definir melhor. Autogestão é:


Conjunto de práticas organizacionais que buscam distribuir a autoridade, dando clareza de responsabilidades e o máximo de autonomia a cada integrante da organização. Nesse caso, as pessoas deixam de reportar a um superior, porém seguem um conjunto de regras e acordos firmados coletivamente. Esses acordos formam uma estrutura organizacional que não exige que todos tenham o mesmo poder de decisão e autoridade, apenas deixa claro como isso é feito e impede a relação de chefe-subordinado.

O nosso método de autogestão favorito é a Organização Orgânica (acesse as nossas videoaulas gratuitas para entender melhor), que abordamos com bastante frequência aqui no blog A O2 possui alguns componentes básicos que são totalmente compatíveis com o método Kanban:

**Papéis**. Na O2, buscamos esclarecer responsabilidades e expectativas através de papéis claros. Esse processo ajuda muito na hora de montar o quadro e entender como o seu processo funciona atualmente. Usamos o mesmo princípio do Kanban na O2. Começamos a partir da estrutura organizacional já existente. Além disso, o seu processo inevitavelmente terá uma série de papéis envolvidos nas diversas etapas. Tornar claras as responsabilidades de cada agente já gera ganhos no início.

**Restrições**. Uma das regras mais importantes da O2 é que *tudo é permitido, a não ser que explicitamente proibido*. Nos trabalhos de Kanban que fazemos, usamos o mesmo princípio na hora de definir as políticas. Colocamos todas elas na forma de restrições ou proibições. Por exemplo, ao invés de escrever:


Todos devem movimentar os cartões para a frente, sem voltar etapas.

Transformaríamos essa política em uma restrição do círculo, reescrevendo dessa forma:


Ninguém pode movimentar cartões para trás.

É uma mudança sutil, mas que faz toda a diferença. Se alguém perguntar: *posso sinalizar um impedimento no cartão colocando uma bolinha colorida?* A nossa resposta será: *tudo é permitido, a não ser que explicitamente proibido*. Então se não está proibido, siga em frente! ;)

### Papel Designer do Sistema

Quando começamos um trabalho de Kanban, também é comum assumirmos um papel de *designer do sistema*. Esse papel tem autoridade para realizar mudanças no processo de forma autocrática. Esse está longe de ser o estado que buscamos, pois sempre queremos nos tornar desnecessários o mais rápido possível. Mas antes disso acontecer, há um caminho que deve ser percorrido. O grupo passará por várias tentações no processo (aumentar os limites, por exemplo) que podem ser evitadas tendo alguém experiente no método com responsabilidade e domínio exclusivo sobre as regras do jogo.

Isso pode ser feito facilmente na O2, com um papel explícito com um artefato “Fluxo, políticas e restrições do Kanban”. Também vale colocar responsabilidade nos outros papéis de seguir as orientações do designer do sistema.

Não é “feio” começar assim. Na realidade é mais funcional ter alguém com a “chave do quadro” no início do que pretender uma evolução colaborativa, que na prática você não vai executar.

### Kanban como restrições de um círculo

Chega um momento que o grupo já tem conhecimento o suficiente para evoluir o sistema Kanban por conta própria. Nessa hora vale excluir o papel designer do sistema e transferir a responsabilidade para o grupo. Uma forma fácil de fazer isso com a O2 é simplesmente transformando todas as políticas do quadro em restrições do círculo. Isso fará com que estas restrições só possam ser alteradas mediante propostas no **modo** **adaptar** da reunião do círculo. Se isso for uma língua estranha para você, leia mais os nossos posts sobre O2.

## E tem muito mais que ainda não está aqui

Chegamos ao fim deste guia (quase) completo sobre o método Kanban. O assunto é amplo. A comunidade em torno dele é maior ainda. Existem muitos temas relacionados que não conseguimos ainda cobrir nesse guia, mas que adicionaremos ao longo do tempo. Ainda não falamos sobre **previsões**, **modelos de melhoria** e **teoria das filas**. Esses assuntos ficam para o futuro.

Se você quiser aprofundar o seu conhecimento sobre sistemas Kanban, vale a pena ler os livros do David. J Anderson e do Donald G. Reinertsen.

Precisa de ajuda para trazer o método Kanban para a sua organização? Vamos tomar um café e falar sobre isso. :)

João Paulo Del Conti Esteves22 de março de 2018 at 13:30Muito legal esse resumo. Acabei de terminar o livro do David Anderson e realmente está muito bem feito.

Uma coisa legal de se acrescentar seria uma explicação da forma de se montar os itens de trabalho na coluna selecionados (backlog) , com um exemplo prático de como é feita essa decisão dentro de uma empresa que já tem o Kanban em funcionamento.

Quando chega uma demanda relativamente grande, como é dividido esse trabalho dentro da coluna selecionados/backlog? Imagino como seja mas nunca tive a oportunidade de ver isso na prática. Acredito que outros iniciantes devam ter a mesma dúvida.

Mas uma vez, parabéns pelo artigo!!

Davi Gabriel da Silva30 de março de 2018 at 10:11Show João! Que bom que vc curtiu. Sim, essa parte de “refinamento do Backlog” é fundamental. É geralmente uma das maiores fontes de variabilidade em um fluxo de desenvolvimento de produtos. Acho que vamos montar um post só sobre isso, porque é um assunto BEM vasto. Valeu pela dica aí. ;)

Estratégia em um mundo VUCA - O fim de uma era - Target Teal23 de março de 2018 at 07:56[…] se fossem estimativas mas ainda chamam de prazos. Já vi até pessoas chamarem plano de ação de Kanban! No final quando as coisas não ocorrem do jeito previsto não percebem que a bagunça foi criada […]

Levando a Agilidade para toda a sua Organização - Target Teal23 de março de 2018 at 07:57[…] a maneira como lidamos com projetos na área de tecnologia. Se você já experimentou Scrum, Kanban ou algum outro método ágil na prática, você deve ter feito a pergunta: por que outras áreas e […]

henry27 de março de 2018 at 09:49Incrivel a generosidade em compartilhar conhecimento da TT. Muito obrigado!

Davi Gabriel da Silva30 de março de 2018 at 10:09Obrigado Henry! :)

Sergio Sampaio29 de maio de 2018 at 17:27Valeu, Davi! Muito bacana e didático. Agradeço a generosidade tb :-)

Davi Gabriel da Silva17 de agosto de 2018 at 15:31Valeu Sergião!!!

Felipe Oliveira17 de agosto de 2018 at 14:15Prezados,

Achei o texto muito explicativo. Bem descrito, com bom embasamento. Porém, tenho alguns questionamentos, no que se trata da comparação com o Scrum:

Sobre Múltiplos focos: apesar da convivência mostrada entre sustentação e desenvolvimento, por exemplo, ter múltiplos focos pode representar aumento do WIP, não em nível de coluna, em frentes de demandas / objetivos / iniciativas. Como enxergam isso?

Sobre Entregas constantes: quando se fala de ciclos menores, falam de sprints. Há possibilidade de ter sprints de 1 semana a 1 mês, para influenciar na rotina e ritmo do time. Como enxergam a diminuição do ciclo, levando em conta essa percepção?

Sobre mais evolutivo: concordo com a questão da mudança organizacional, pois envolve uma cultura muitas vezes contrária ao processo multidisciplinar no scrum. Porém, qual a abordagem então, se times grandes podem prejudicar a comunicação, integração e engajamento? Além disso, se criamos silos funcionais, não há a possibildiade associada ao mesmo gargalo gerado?

Grato.

Davi Gabriel da Silva17 de agosto de 2018 at 20:07Oi Felipe! Que bom que você gostou. ;)

1. Ter mais que um foco não aumenta necessariamente o WIP. Quer dizer, se você mantiver o WIP total igual, você só estará diluindo a sua capacidade em temas diferentes.

2. No Kanban os ciclos são usados como uma ferramenta de acompanhamento e evolução. Já no Scrum eles são usados tanto para isso quando para a entrega e feedback. De qualquer forma, o principal pilar da abordagem moderna é validar sua entrega o mais rápido que você puder e for operacionalmente adequado para um grupo. Ou seja, ciclos menores são geralmente desejáveis.

3. A abordagem no Kanban é trabalhar com pequenos incrementos, tratando cada oportunidade de melhoria percebida. Talvez você comece a praticar Kanban com time grandes e funcionais. Os silos então vão começar a se mostrar, na forma de gargalos no processo, dependência de especialistas, lead time muito alto, etc. A dinâmica social da visualização do fluxo trará o incômodo necessário para que a colaboração comece a acontecer naturalmente. Ou seja, é aqui que a postura Kaizen aparece. Os silos funcionais vão se desmanchar naturalmente, se vantajoso para o grupo. O caminho da mudança estrutural é natural.

Scrum: o que é e quando fazer - Target Teal1 de abril de 2019 at 14:49[…] muitos novos itens durante a realização de cada ciclo. Caso este seja o caso, talvez o método Kanban faça mais sentido para esse produto. Falarei mais sobre isso em um próximo artigo sobre alguns […]

Ágil além do software: 10 práticas para qualquer time - Parte 1 - Target Teal1 de maio de 2019 at 20:28[…] que fica não são os valores, mas sim as práticas. Ao tentar aplicar um framework como Scrum ou o método Kanban, muitos entusiastas desanimam, porque os métodos na sua totalidade podem ser difíceis de adotar […]

Pedro Grillo20 de maio de 2019 at 08:22Excelente, Davi! Obrigado

Gestão Imobiliária: aumente a produtividade do seu negócio - Blog da Vista20 de maio de 2019 at 21:21[…] 1. Gestão Imobiliária com o Método Kanban […]

MARCO AURELIO CASTALDO ANDRADE12 de agosto de 2019 at 14:11Parabéns pelo texto, pela clareza e organização das informações e do tema.

Meus times estão adotando Kanban por iniciativa própria (aqui, na Elotech, os líderes definem apenas “o que” e “quando” com seus times, eles definem o resto), e entendi que precisava saber o mínimo sobre o assunto.

Engraçado que encontrei seu blog porque pretendo aprofundar a autonomia das equipes e incluir, nisso, a superação do modelo de orçamento. Encontrei seu blog, li o post sobre Beyond Budgeting, e encontrei este sobre kanban. Decidi não perder a oportunidade, e não me arrependi.

Método Kanban – Agile Kanban13 de agosto de 2019 at 16:40[…] fonte: https://targetteal.com/pt/blog/metodo-kanban/ […]

EDUARDO PEREIRA TAVARES3 de dezembro de 2019 at 04:59Maravilhoso as formas abordadas. Estudei os prcessos, fiquei com uma visão geral sobre o assunto. Concerteza tenho clareza para ainda estudar mais e ser perito nisso.

Obrigado

Gestão Imobiliária: guia completo para a alta performance!31 de janeiro de 2020 at 17:45[…] 5. Gestão Imobiliária com o Método Kanban […]

Angelina14 de fevereiro de 2020 at 10:09Texto muito bom e rico em conteúdo de verdade, parabéns!

Ronny24 de fevereiro de 2020 at 21:25Muito bom! Parabéns, não aprofunda em alguns assuntos como por exemplo métricas, mas por outro lado aborda todos os assuntos (inclusive métricas) de maneira interessante e didática.

ronny24 de fevereiro de 2020 at 21:34O link para o post do Leonardo Campos sobre como ler e montar o gráfico CFD está quebrado, poderia olhar por favor?

Linkagem de Maio – Leonardo Morais30 de maio de 2020 at 11:21[…] Um excelente guia Kanban da Target Teal. Eu já tinha lido esse post, mas revisitei pra tirar algumas dúvidas. O blog da Target Teal é excelente, com posts muito completos. […]

sandra7 de julho de 2020 at 08:26gostaria de compreender melhor, o fluxo de valores dentro do método kanban, e o sistema de puxada e empurrada, apesar de compreender os dois em cada uma da sua função, o que explica perfeitamente a diferenças entre eles, o que o sistema de empurrada serviria no método kanban, então nesse caso , se o kanban mostra, método para não haver desperdício, não compreendo por que o empurrado, poderia ser útil no método kanban, e que momento ele pode ser usado?

Interdependência e Reuniões Regulares - Target Teal8 de julho de 2020 at 08:32[…] reunião incorporar práticas que permitam a visualização e otimização do fluxo de trabalho. O método Kanban é muito bom para […]

Heurísticas para Intervenções em Organizações - Target Teal12 de agosto de 2021 at 09:16[…] Para quem tem mais poder e influência essa opacidade costuma ser benéfica. Gera a ambiguidade que é aproveitada com as famosas “carteiradas” que tornam uma tarefa ultra urgente por motivos que não podem ser questionados. A opacidade permite ignorar com facilidade a “não priorização” que leva ao infinito a quantidade do que chamamos de trabalho em progresso (WIP). […]