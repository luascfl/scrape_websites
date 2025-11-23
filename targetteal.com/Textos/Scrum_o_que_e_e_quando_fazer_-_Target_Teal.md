---
title: Scrum: o que é e quando fazer - Target Teal
author: Danilo Fascio
url: https://targetteal.com/blog/o-que-e-scrum/
hostname: targetteal.com
description: O Scrum é um framework que auxilia times a construírem e evoluírem produtos em ambientes complexos. Conheça o que é Scrum e quando fazer.
sitename: Target Teal
date: 2019-04-01
categories: ['Ágil']
---
Criado em 1995 por Ken Schwaber e Jeff Sutherland, o Scrum é um framework que busca auxiliar times a construírem e evoluírem produtos em ambientes complexos. O Scrum é classificado como sendo parte de um movimento maior, chamado de Ágil, que exploramos em outro texto. O Scrum é incrivelmente popular: 56% dos respondentes da maior pesquisa de adoção de métodos ágeis afirmam utilizá-lo. Mas essa “massificação” também traz diversos mal entendidos e desafios que exploraremos neste guia.

## O que é Scrum?

Como dissemos no início, o Scrum é um “framework”. Isso significa que ele não diz exatamente como você deve gerenciar o desenvolvimento de produtos, mas apenas estabelece um “meta-processo” para fazê-lo.

No Guia do Scrum, está escrito que ele foi utilizado com sucesso para desenvolver software, hardware, software embarcado, redes de função de interação, veículos autônomos, escolas, projetos governamentais, marketing, etc. Quase tudo que usamos em nosso dia a dia.

O Scrum define alguns papéis, artefatos e eventos (reuniões) que são utilizados na organização do trabalho de um time. Neste guia, usaremos exemplos de desenvolvimento de software, pois acredito que esses podem ser facilmente compreendidos por boa parte dos leitores.

### Sprints

No Scrum, o trabalho é dividido nas famosas “Sprints”, que são os ciclos de trabalho de duração fixa (de 1 a 4 semanas). Ao final de cada Sprint, um incremento (parte que pode ser usada) do produto é entregue. Diferentemente da abordagem tradicional de desenvolvimento de software, o Scrum busca realizar entregas de valor curtas e contínuas ao longo de todo o ciclo de vida de um produto.

Por exemplo: imagine que você faz parte de um time Scrum responsável por desenvolver um aplicativo que conecta motoristas autônomos com passageiros que querem se deslocar. Vamos chamar esse aplicativo de Umber. ;)

Na abordagem tradicional, teríamos primeiro uma fase de levantamento de requisitos, com entrevistas e pesquisas para entender o público-alvo e assim registrar em detalhes todas as funcionalidades desejadas pelos motoristas e passageiros. Nos 3 meses seguintes os desenvolvedores ficariam projetando o software, definindo sua arquitetura e criando o banco de dados. Mais 4 meses, por exemplo, seriam utilizados para implementar todas as features desse produto. E por fim, mais 2 meses seriam compostos por testes finais de qualidade com os usuários.

Parece um plano perfeito, certo? O problema é que nesse modo de pensar investe-se muito dinheiro e energia, para somente no final do longo período obter algum feedback útil dos usuários.

Por outro lado, no Scrum o time realizaria todas essas atividades dentro de uma Sprint, entregando uma parte simples (porém funcional) desse produto ao cliente final a cada ciclo.

#### A analogia do bolo

Para explicar a diferença do tradicional para o Scrum, podemos utilizar a analogia do bolo. Em um projeto tradicional, temos um conjunto de fases onde cria-se uma camada do bolo de cada vez. Cada camada corresponde a uma etapa funcional do projeto, como por exemplo, criar o banco de dados, desenvolver as APIs ou desenhar a interface do usuário. O problema é que o usuário final não utiliza uma dessas camadas de forma independente. Não adianta entregar o banco de dados para ele no final da fase. Ele só pode comer o bolo inteiro. Só o merengue não significa nada para o cliente.

No Scrum, ao invés de entregarmos uma camada por vez, buscamos entregar fatias. Uma fatia bem fina do bolo, mas que tenha todas as camadas. Assim o usuário pode experimentar e dizer: *humm, gostaria que massa fosse mais doce*. Assim no próximo ciclo de desenvolvimento (Sprint) o time ajusta a quantidade de açúcar. Agora, se ele comer o bolo só depois que ele estivesse completamente pronto, o custo de mudar seria muito alto.

### Papéis do Scrum

O guia do Scrum define 3 papéis necessários para manter o framework em funcionamento. O Product Owner, o Time de Desenvolvimento e o Scrum Master.

#### Product Owner (PO)

O Product Owner é responsável por maximizar o retorno sobre o investimento do produto. Ele deve estar sempre atento às demandas de negócio e em constante contato com as partes interessadas: o time, clientes, acionistas, diretores, usuários, etc.

O PO detém a visão do produto, ou seja, ele visualiza e busca levar o produto sendo construído para um determinado caminho. Isso é geralmente feito através da escrita de Itens de Backlog, que correspondem a funcionalidades, correções de defeitos e novos recursos que serão disponibilizados no produto.

O Product Owner prioriza constantemente esse Backlog do Produto, que é uma lista frequentemente revisada com as coisas que devem ser implementadas no produto. O PO deve ser apenas uma pessoa, e não um grupo. Além disso, ele precisa ter a autoridade exclusiva de mexer no Backlog, em especial a prioridade das coisas. Diretores, gerentes e até sócios devem negociar com esse papel se quiserem incluir novos itens ou alterar os existentes.

#### Time de Desenvolvimento

O Time de Desenvolvimento é um grupo pequeno (de 3 a 9 integrantes, segundo o Guia do Scrum) que contém (em essência) todas as competências e condições necessárias para criar e manter o produto sendo desenvolvido (leia sobre equipes multidisciplinares). Além disso, o Time de Desenvolvimento é auto-organizado: não existe um chefe responsável por gerenciar o trabalho (o Scrum Master também NÃO faz isso!).

Neste ponto vale ressaltar a diferença entre auto-organizado (self-organized), autodirecionado (self-directed) e autogerido (self-managed). No Scrum estamos falando de auto-organização, ou seja, autonomia completa para funcionar respeitando os acordos estabelecidos na organização e também às diretrizes do framework Scrum. Já a direção é definida pelo PO (considerando as perspectivas do time, naturalmente), e a gestão depende do modelo aplicado na organização.

No exemplo do nosso aplicativo de assinatura de receitas, provavelmente precisaríamos de pessoas com capacidade de desenvolver software, criar protótipos de interface, testar software, fazer pesquisas com usuário, etc. Todas essas competências devem estar presentes no Time de Desenvolvimento, em uma ou mais pessoas. Ou seja, provavelmente precisaríamos de um desenvolvedor, um designer e um testador. Obviamente, o time ser multidisciplinar não significa que todos devem saber tudo.

E aqui encontramos uma das maiores belezas que o movimento ágil e o Scrum trouxeram para as organizações que aplicam verdadeiramente seus princípios. Buscando atender a essa condição necessária para a entrega contínua de valor (conter todas as competências e condições necessárias para criar e manter o produto), os times e as organizações se colocam em uma situação verdadeira de melhoria contínua. Nesse contexto, é muito comum que os times descubram deficiências em suas capacidades e estruturas, e essas descobertas levem a sua evolução.

#### Scrum Master (SM)

O Scrum Master suporta os demais (Time de Desenvolvimento e Product Owner) no entendimento e aplicação do Scrum. Ele facilita as cerimônias e ajuda o grupo como um todo a se auto-organizar. Ninguém nasce sabendo usar o Scrum, muito menos trabalhar de forma autogerida. É por isso que esse papel é tão importante, especialmente durante as etapas iniciais de adoção do *framework*.

O Scrum Master não é um chefe. Ele não “cobra as entregas” dos membros do time ou é responsável pelo sucesso do produto. O Scrum Master atua mais como um coach, que oferece o espelho nos momentos adequados e encoraja os membros do time a tratarem as suas próprias tensões entre eles e a dependerem menos do SM ou do PO.

O SM também atua expandindo o Scrum dentro da organização em que atua, ensinando outros times e departamentos a trabalharem com o *framework*. É comum também o SM auxiliar o Product Owner a melhor expressar os itens do Backlog do Produto (normalmente na forma de histórias de usuário).

Costuma-se dizer que existe um equilíbrio saudável das forças produzidas por esses 3 papéis neste grupo. Por um lado, o PO está constantemente procurando entregar “a coisa certa” (eficácia), ou seja, aquilo que os stakeholders, principalmente os usuários e clientes esperam do produto para considerá-lo valioso. Já o Time de Desenvolvimento tem a tendência em buscar a realização do trabalho “do jeito certo” (eficiência), preocupado com a qualidade do produto, dada a entropia natural de sistemas complexos. O Scrum Master, por sua vez, persegue a “rapidez”, nem tanto pela busca por produtividade e sim da redução do ciclo de feedback (validação da entrega de valor) junto aos stakeholders.

### Artefatos do Scrum

Além dos papéis, o Guia do Scrum define também um conjunto de “artefatos” que são peças importantes no funcionamento do framework.

#### Backlog do Produto

O Backlog do Produto é uma lista ordenada e em constante evolução sobre “tudo” (você já vai entender o porquê das aspas) que precisa ser feito para que o produto em construção atinja a visão definida pelo Product Owner (PO). Embora o Scrum não defina como detalhar o Backlog, uma prática comum é o uso de histórias [1] do usuário, que listamos acima. Por exemplo, poderíamos ter os seguintes itens no Backlog do Produto Umber:

“Enquanto passageiro, preciso encontrar um motorista para me transportar até o meu destino.”

“Enquanto passageiro, quero encontrar um carro para transportar as minhas bagagens.”

“Enquanto passageiro, gostaria de poder pagar a viagem em dinheiro.”

“Enquanto motorista, gostaria de aceitar apenas cartão como forma de pagamento.”


Estas seriam as 4 funcionalidades no topo do nosso Backlog e que seriam implementadas pelo Time de Desenvolvimento. Note que na escrita da História de Usuário não detalhamos “como” o item será desenvolvido. O detalhamento técnico vêm depois e normalmente na Sprint Backlog.

Dizemos que um bom Backlog de Produto é DEEP, ou seja, têm as seguintes características:

**Detalhado (apenas o suficiente)**: Os itens no topo (ou seja, mais próximos de serem desenvolvidos) em um Backlog do Produto devem estar detalhados o suficiente. Ou seja, já devem ter sido discutidos entre o Time de Desenvolvimento e o PO, com critérios de aceitação definidos, etc. O quanto é “suficiente” varia de contexto para contexto e de time para a time. Como o Scrum é baseado no empirismo, vale testar diferentes níveis detalhamento e ver como isso impacta o funcionamento do time e na entrega de valor. Geralmente esse nível de detalhamento desejado é capturado em um artefato chamado “Definição de Preparado” (Definition of Ready, em inglês). O importante é que os itens mais próximos de serem feitos estejam MAIS detalhados do que os que estão mais longe. No Scrum, não faz sentido especificar os requisitos/funcionalidades muito antes de elas serem desenvolvidas, porque isso implica em potencial desperdício (itens planejados que nunca são implementados).

**Estimado**: Como o Scrum trabalha com Sprints de duração fixa (de 1 a 4 semanas), o Time de Desenvolvimento terá que fazer algum tipo de estimativa para planejar o que vai entrar na próxima Sprint. Por isso que os primeiros itens do Backlog do Produto também devem ser estimados. Existem diversas técnicas para isso, sendo a mais comum o Planning Poker.

Vale lembrar também que existem abordagens que consideram qualquer esforço de estimativa um potencial desperdício de energia de um grupo, que poderia estar dedicando esse tempo para o trabalho propriamente dito. O movimento #NoEstimates discute profundamente este tema.

**Emergente**: O Backlog do Produto é um artefato vivo, ou seja, ele não é escrito uma única fez, impresso e colado na parede. O mais comum é que ele seja atualizado todos os dias pelo Product Owner. Isso implica que o Backlog é “emergente”, ou seja, vai surgindo a partir das interações entre Product Owner, Time de Desenvolvimento, Usuários, Stakeholders, etc. Não existe algo como um “Backlog” pronto. Ele está sempre em constante evolução.

**Priorizado**: Por fim, o Backlog é uma lista “ordenada”. Como responsável pela priorização do que é feito, o Product Owner está constantemente reorganizando essa lista. Novas descobertas sobre o produto, necessidades do cliente, do mercado e também da sustentação da plataforma tecnológica geralmente impactam essa priorização, que é feita para maximizar o retorno sobre o investimento.

Agora que vimos as características de um Backlog do Produto, vamos ao Backlog da Sprint!

#### Backlog da Sprint

Os itens do topo do Backlog do Produto são movidos para o Backlog da Sprint quando chega o momento de serem implementados. Isto é feito na cerimônia de Planejamento da Sprint, como veremos mais para frente.

O Backlog da Sprint é o plano do Time de Desenvolvimento de como entregar a Meta da Sprint definida em conjunto com o Product Owner. Geralmente cada Sprint possui um objetivo de negócio, definido na forma de uma meta, como: “Possibilitar que os passageiros encontrem motoristas rapidamente”. Nesse caso, provavelmente o Product Owner selecionaria as histórias do Backlog do Produto relacionadas com o tema *passageiros encontrarem motoristas*. Essas histórias seriam então detalhadas na Sprint Backlog.

Novamente, o Scrum não nos dá muitas respostas de como montar o Backlog da Sprint. Uma das práticas mais comuns é o Time de Desenvolvimento quebrar cada item do Backlog do Produto selecionado em diversas “tarefas técnicas” que são implementadas ao longo da Sprint. Por exemplo, dada a história:

Enquanto passageiro, gostaria de encontrar um carro para transportar as minhas bagagens


O Time de Desenvolvimento poderia definir as seguintes “tarefas”:

Desenhar interface de seleção do tipo de veículo


Testar interface com usuário

Criar tabela e modelo de “tipos de veículo”

Criar testes automatizados para o controller VehycleType

Essas tarefas geralmente compõem tudo que é necessário para implementar a história em questão. Mais importante do que a descrição das tarefas em si são as conversas e trocas entre os membros do Time de Desenvolvimento. Lembre-se que o Scrum, como parte do guarda-chuva ágil, valoriza a comunicação cara a cara mais do que documentação extensa.

Neste quadro os post-its pequenos representam as tarefas técnicas, enquanto que os grandes correspondem aos itens do Backlog (funcionalidades, defeitos, melhorias, etc).

#### Definição de Pronto

A Definição de Pronto é um checklist de todos os critérios necessários para que um determinado item do Backlog do Produto seja considerado “pronto”. O objetivo é garantir um entendimento comum do que significa um item “estar pronto” entre todas as partes. Por exemplo, poderíamos colocar na nossa definição de pronto do Umber que é necessário que o FAQ seja atualizado para que novas funcionalidades sejam consideradas “prontas”. Ou seja, se no final da Sprint nós finalizamos o desenvolvimento e testes da história de transporte das bagagens, mas não atualizamos o FAQ, este item seria considerado não-pronto.

Por mais simples que pareça, este artefato permite que o Time Scrum aumente cada vez mais a qualidade dos itens de Backlog sendo entregues. Em geral, a Definição de Pronto fica mais completa e criteriosa a medida que o time vai evoluindo.

Agora que vimos os principais artefatos do Scrum, vamos aos eventos!

### Cerimônias do Scrum

As cerimônias do Scrum, também chamadas de eventos, são diferentes momentos que se repetem a cada Sprint e permitem que o Time Scrum se adapte ao ambiente e entregue valor rapidamente.

#### Reunião Diária

O primeiro e mais conhecido evento do Scrum é a Reunião Diária, Daily Meeting ou Daily Scrum. Como o próprio nome sugere, este encontro de no máximo 15 minutos deve acontecer todos os dias durante a Sprint. É um momento destinado ao Time de Desenvolvimento, onde grupo planeja o trabalho das próximas 24h em direção à Meta da Sprint. O formato mais comum é cada participante responder às “3 perguntas”:

- O que eu fiz ontem que ajudou o Time de Desenvolvimento a atingir a Meta da Sprint? Ou ainda “como” eu fiz o que fiz ontem?
- O que eu pretendo fazer hoje que ajudará o Time de Desenvolvimento a atingir a Meta da Sprint? Ou “como” farei o que pretendo fazer hoje?
- Existem impedimentos que vejo que possam impedir que eu ou o Time de Desenvolvimento atinja a Meta da Sprint?

O encontro possui timebox (limite de tempo) de 15 minutos. O objetivo é catalisar a colaboração e outras possíveis conversas que podem acontecer na sequência do evento. Lembre-se que o Time de Desenvolvimento é auto-organizado, ou seja, não tem um chefe coordenando as atividades de cada um. A ênfase no “como” ajuda o time a de fato debater e trocar conhecimento sobre possíveis caminhos e lições aprendidas.

#### Planejamento da Sprint

No início de cada Sprint, o Time Scrum (PO, SM e Time de Desenvolvimento) se reúne para planejar a Sprint a seguir. Essa cerimônia tem um timebox de 8h para uma Sprint de 4 semanas, ou 4h para Sprints de 2 semanas. Nesse encontro o Time Scrum busca responder às seguintes perguntas:

- O que pode ser entregue como resultado da próxima Sprint?
- Como o trabalho necessário para entregar a Sprint será feito?

Em geral, quando mais bem preparado estiver o Backlog do Produto seguindo os critérios DEEP, mais fácil é o processo de Planejamento da Sprint. O encontro geralmente começa com o grupo discutindo qual será a próxima Meta da Sprint. Na sequência o Time de Desenvolvimento estima quais próximas histórias poderão ser entregues dentro do timebox da Sprint para atingir a Meta combinada.

Ao final da cerimônia, o Time de Desenvolvimento deverá ser capaz de explicar como pretende se auto-organizar para entregar a Meta e os itens selecionados.

#### Revisão da Sprint

Ao final de cada Sprint, acontecem a Revisão e a Retrospectiva. A primeira cerimônia tem como objetivo demonstrar o “incremento” (pedaço do produto) criado durante a Sprint para os clientes/usuários. Geralmente diversos Stakeholders participam, além de todo o Time Scrum. Nesse momento o Time de Desenvolvimento demonstra (com software real, nada de PPTs ou fotos de telas) o que foi finalizado de acordo com a Definição de Pronto.

Tudo pode acontecer na Revisão. Os clientes podem ficar maravilhados com o que foi produzido pelo time. Ou o Time de Desenvolvimento pode sentir vergonha por não ter entregue nada de valor. O importante é realizar o evento em qualquer um dos casos, pois é uma prestação de contas importante do time para os clientes.

É comum que além de demonstrar o que foi feito, o Time de Desenvolvimento comente como foi a Sprint, ou seja, que impedimentos apareceram, como o grupo se organizou para resolvê-los, etc.

Apesar do Scrum propor a Revisão da Sprint, esse não precisa (e não deve) ser o único momento de buscar feedback dos clientes e usuários. Times ágeis maduros estão em constante contato com as partes interessadas e integram feedbacks o mais rápido possível.

A Revisão tem timebox de 4h para Sprints de 4 semanas e progressivamente menos para Sprints menores.

#### Retrospectiva da Sprint

Após a Revisão acontece o último evento da Sprint, a famosa Retrospectiva. O timebox é de 3h para Sprints de 4 semanas. Ainda assim, eu pessoalmente prefiro diminuir um pouco o tempo da Revisão e investir mais na Retrospectiva, porque acredito que essa é a cerimônia mais importante de todas. O objetivo é o Time Scrum inspecionar e adaptar o seu processo de desenvolvimento. Ou seja, falar sobre como todos estão trabalhando juntos.

Existem inúmeros formatos de retrospectivas, e até livros só sobre o assunto, como o Retrospectivas Divertidas do Paulo Caroli ou o Agile Retrospectives da Esther Derby e Diana Larsen. Talvez o mais comum seja o “parar-continuar-começar”, onde o Time Scrum discute o que deve parar de fazer, o que deve continuar fazendo e o que deve começar a fazer.

A Retrospectiva é o momento do time falar sobre o processo e as relações. Por isso que costumamos ouvir o termo “lavação de roupa suja”. É comum que conversas difíceis aconteçam nesse momento. Por isso é importante que um bom Scrum Master esteja disponível para facilitar o encontro.

## Quando fazer Scrum e quando não

Empolgados com Scrum e métodos ágeis, muitas pessoas pegam emprestadas algumas “práticas” do framework e saem implementando sem refletir muito sobre as implicações, condições necessárias para o sucesso das iniciativas e premissas importantes. Nessa parte vou sugerir quando fazer e quando não fazer Scrum, apesar dessa resposta não ser assim tão simples.

Primeiro, o Scrum é um framework com elementos que se auto-reforçam e são muitas vezes interdependentes. Ou seja, se você tirar uma peça, é provável que o todo desmonte. Por exemplo, se o Time Scrum não for multidisciplinar, contendo todas as funções necessárias para entregar o incremento, ao final do Sprint você não terá um pedaço de produto funcional. Sem isso não faz nenhum sentido fazer uma Revisão, pois nenhum valor foi gerado para os clientes e usuários.

Não é sem razão que os criadores do framework, Ken Schwaber e Jeff Sutherland acrescentam ao final do Guia do Scrum a seguinte frase: “*O Scrum é livre e oferecido neste guia. Papéis, eventos, artefatos e regras do Scrum são imutáveis e embora seja possível implementar somente partes do Scrum, o resultado não é Scrum. Scrum existe somente na sua totalidade e funciona bem como um container para outras técnicas, metodologias e práticas.*”.

Certa vez, como consultor apoiando a implantação do modelo em uma grande empresa de software nacional, ouvi que estava sendo muito radical quando sugeri que a organização mantivesse os conceitos e práticas em sua essência no começo do projeto de transformação. O argumento na ocasião foi que a organização precisaria adaptar as práticas para o seu contexto, que é único. Para quem simpatiza com essa perspectiva, fica aqui meu pedido para tratar o assunto com muito cuidado e principalmente bastante humildade.

Claro que cada organização tem um contexto único e que cada contexto exige o seu próprio nível de personalização, mas sugiro que essa adaptação respeite a mentalidade de aprendizado denominada Shu-ha-ri, muito comum nas artes marciais japonesas. Nesta filosofia oriental primeiro você obedece e protege o conhecimento tradicional para somente depois que a essência deste novo conhecimento tenha ficado absolutamente clara para você (e os demais envolvidos), só então você começa a transcender e evoluir uma prática para um contexto mais específico.

Considero o Scrum uma ótima abordagem para o aprendizado inicial (efeito propedêutico) das premissas e práticas da mentalidade ágil. Portanto, é um ótimo framework de iniciação, principalmente para times de desenvolvimento de software, em especial para novos produtos. Quando aplicado no desenvolvimento de um produto já existente, é necessário avaliar se a organização conseguirá respeitar minimamente o escopo de cada Sprint, sem acrescentar muitos novos itens durante a realização de cada ciclo. Caso este seja o caso, talvez o método Kanban faça mais sentido para esse produto. Falarei mais sobre isso em um próximo artigo sobre alguns dos principais antipadrões (erros comuns) na implantação do framework que encontramos frequentemente nas organizações, o que acabou criando na comunidade ágil o termo #fragile (um trocadilho com a palavra frágil em inglês).

Até breve!

[1] Apesar de frequentemente encontrada nos textos em português na internet, a palavra “estória” não faz mais parte da norma culta do português brasileiro, sugiro então o uso do termo “História de Usuário” para falarmos deste formato de escrita dos requisitos.


Ágil além do software: 10 práticas para qualquer time - Parte 1 - Target Teal1 de maio de 2019 at 20:27[…] assim, a dúvida que fica não são os valores, mas sim as práticas. Ao tentar aplicar um framework como Scrum ou o método Kanban, muitos entusiastas desanimam, porque os métodos na sua totalidade podem ser […]

Estrutura Organizacional: Piramidal, Horizontal e Autogerida - Target Teal8 de agosto de 2019 at 15:09[…] uma experiência valiosa para eles. Os times pequenos, auto-organizados e multidisciplinares do Scrum têm esse foco. A estrutura organizacional Spotify, famosa por seus Squads, Tribes, Chapters e […]

Modelo Spotify Squads: O que é e como funciona - Target Teal28 de abril de 2020 at 20:04[…] início, o Spotify era uma empresa pequena, que basicamente utilizava o framework Scrum, com seus times pequenos e multidisciplinares. Conforme o número de equipes foi aumentando, eles […]

Interdependência e Reuniões Regulares - Target Teal8 de julho de 2020 at 08:29[…] a onda ágil chegando em empresas de todos os tipos, vejo que uma disfunção comum é tentar rodar as cerimônias de Scrum com times desse […]

Práticas ou Princípios - Uma falsa dicotomia - Target Teal2 de setembro de 2020 at 15:09[…] Eles contratam cursos para certificar seus gerentes de projeto e começar a rodar cerimônias do Scrum. Todos sabem que existe algo chamado manifesto ágil com valores e princípios. No dia-a-dia, […]

Scrum é a pior droga de entrada - Target Teal7 de outubro de 2020 at 18:50[…] framework Scrum é uma droga de entrada para times e organizações que estão começando no universo da […]

Comunicação e Design Organizacional - Target Teal4 de novembro de 2020 at 15:57[…] é tão importante para os times ágeis que está expresso como um dos 3 pilares do Scrum, junto com inspeção e […]

Practices and principles – a false dichotomy - Target Teal27 de janeiro de 2022 at 09:47[…] be left behind in the market. They hire courses to certify their project managers and start running Scrum ceremonies. Everyone knows that there is something called an agile manifesto with values and […]

Practices or principles – a false dichotomy - Target Teal27 de janeiro de 2022 at 09:47[…] be left behind in the market. They hire courses to certify their project managers and start running Scrum ceremonies. Everyone knows that there is something called an agile manifesto with values and […]

Design de conversas: o óbvio, o quase óbvio e o nada óbvio - Target Teal10 de junho de 2022 at 15:39[…] Cerimônias do Scrum são eventos e cerimônias padrão que um time ágil que trabalha com Scrum costuma realizar. Esses eventos possuem contornos e intenções bem específicas que são partes essenciais do processo de geração de valor do time. São eles a Sprint que é um ciclo de trabalho curto com duração pré-definida e que deve gerar valor, como parte de um trabalho maior de desenvolvimento de produto a ser realizado. Sprint planning é uma reunião em que o time se dedica a responder as perguntas “O que pode ser entregue como resultado da próxima sprint e como o trabalho necessário para entregar a sprint será feito?” Na Sprint review o time se reúne com outros stakeholders para demonstrar o que foi entregue durante a sprint a partir do que foi acordado em seu início, assim como acontecimentos significativos em sua execução. Durante a Sprint Retrospective, o time conversa sobre seu processo de trabalho com a intenção de revisá-lo e adaptá-lo sempre que necessário. E por fim, a Daily meeting que é uma reunião rápida e diária onde cada membro do time responde as perguntas: o que fiz ontem para atingir o objetivo da sprint? o que pretendo fazer hoje para atingir o objetivo da sprint? Percebo algo que possa impedir o time de atingir o objetivo da sprint? […]