---
title: Otimizando dependências no design organizacional - Target Teal
author: Davi Zimmer
url: https://targetteal.com/blog/otimizando-dependencias/
hostname: targetteal.com
description: ALERTA: este é um texto para praticantes avançados de design organizacional e pressupõe bastante conhecimento sobre padrões de design autogeridos.
sitename: Target Teal
date: 2021-07-06
categories: ['Design Organizacional']
---
**ALERTA**: este é um texto para praticantes avançados de design organizacional e pressupõe bastante conhecimento sobre padrões de design autogeridos.

As organizações também são sistemas de informação, dado que coletam, armazenam, processam e distribuem informações. Olhando por essa lente, a forma que organizamos os componentes internos deste sistema parece determinante na sua efetividade. Nesse texto compartilharei em detalhes os tipos de dependência que observo em organizações e como é possível otimiza-las.

Já abordamos em outro texto que baixo acoplamento, alta coesão e boas interfaces de encapsulamento são fundamentais para um design organizacional fluido. Relembrando esses 3 conceitos, temos:

**Acoplamento**: É o grau de dependência entre dois componentes de um sistema. Em geral, buscamos baixo acoplamento, mas o acoplamento na medida certa pode indicar alta coesão. Por exemplo, o nível de dependência entre dois times diferentes em uma organização.**Coesão**: É o grau de foco de um dado componente, ou quanto as partes internas dele estão funcionalmente relacionadas. Um componente coeso faz apenas uma única coisa e os seus componentes internos são altamente acoplados. Por exemplo, um papel “Pagador de Contas” é muito mais coeso do que um “Analista Financeiro”, pois é menor e mais focado.**Encapsulamento**: É a característica de um sistema que permite esconder os detalhes de implementação por trás de um componente de quem o utiliza. Por exemplo, quando uma área recebe demandas a partir de um formulário que permite com que qualquer pessoa faça um pedido sem necessariamente entender como ele será atendido.

Para esta análise também utilizaremos uma linguagem para entender como as dependências se estabelecem dentro do sistema organizacional. Esta linguagem será a da O2, mas mesmo que a sua organização não adota um sistema de autogestão, isso não impede que você olhe para ela a partir desses conceitos:

**Papel**: Um conjunto de responsabilidades com um propósito em comum e que são desempenhadas por uma ou mais pessoas.**Propósito**: O objetivo de um papel ou círculo.**Responsabilidade**: Expectativas de atividade que um papel ou círculo irá executar e que os outros podem invocar/cobrar.**Artefato/domínio**: Um recurso que um papel ou círculo controla exclusivamente (outros devem pedir permissão). Todo recurso que não é definido por um artefato/domínio é considerado um recurso compartilhado.**Círculo**: Um conjunto de papéis com um propósito em comum. O círculo também possui responsabilidades que resumem o que ele faz. Também existem encontros regulares entre os seus membros, o que facilita a interação. Virtualmente qualquer área, time e departamento pode ser encarado como um círculo.

Sobre a alocação de pessoas em papéis, assuma que uma pessoa pode desempenhar mais de um papel e um papel pode ser desempenhado por mais de uma pessoa.

## Tipos de dependências

**Muito fraca**: Um papel ou círculo faz algo que quando é somado com o trabalho de um papel ou círculo cria algo maior e mais completo (também conhecido como interdependência agrupada).

**Fraca**: Um papel ou círculo espera que outro papel ou círculo faça algo (existe uma responsabilidade acordada), mas não tem impeditivos para fazer ele mesmo. Em outras palavras, é conveniente esperar que outro execute aquilo, mas em último caso o papel ou círculo que espera pode fazer ele mesmo.

**Forte**: Um papel ou círculo precisa que outro papel ou círculo libere acesso a algum recurso (artefato/domínio). Ou seja, a dependência é obrigatória.

Para os praticantes “avançados” de autogestão: Existem outras formas de criar dependências fortes, como acontece quando temos uma política/restrição que define que um papel/círculo integre objeções de outro. Também é possível definir uma responsabilidade bastante prescritiva que espera que um papel ou círculo faça algo de acordo com algum outro papel ou círculo. Em todos estes casos há um requisito de que um elemento do design organizacional “aguarde” outro e por isso nomeamos a dependência como forte.

É também possível olhar para as dependências como agrupadas, sequenciais ou recíprocas, como abordou Rodrigo Bastos neste outro texto.

## 1) Dependência interna

As responsabilidades de um mesmo papel ou círculo podem ser dependentes entre si (de forma agrupada, recíproca ou sequencial).

Por exemplo, “Produzir conteúdos para o blog” e “Adicionar ofertas de serviços nos posts” são claramente muito dependentes uma da outra dentro do papel “Produtor de Conteúdo”. Só posso adicionar ofertas depois que o conteúdo for escrito, portanto há uma dependência sequencial.

Em um papel, este tipo de dependência não gera nenhum problema, porque uma mesma pessoa fará ambas as atividades. Inclusive isso pode ser um sinal de alta coesão (papel com propósito focado e específico). É positivo reunir coisas que seriam tipicamente passadas de uma pessoa para outra em um mesmo papel, porque isso reduz perdas de comunicação.

Em um círculo, precisamos olhar para como os seus componentes internos (papéis e círculos internos) distribuem essa dependência para chegar a qualquer conclusão, já que ele é apenas uma abstração.

De forma geral, este tipo de dependência é um sinal de um design coeso. No limite, se não houver nenhuma interdependência entre as responsabilidades de um papel ou círculo dá para dizer que é um monte de coisas aleatórias que foram ali reunidas e não tem nada em comum.

Talvez seja por isso que as abordagens ágeis preferem o “profissional em T“: ele permite maior flexibilidade de alocação, ou seja, uma mesma pessoa pode ter papéis mais amplos e que seriam tipicamente atribuídos a pessoas com diferentes especialidades.

## 2) Dependência externa próxima

**Ou dependência entre papéis ou círculos diretamente conectados**.

Um papel/círculo pode ser dependente de um outro papel/círculo dentro de uma mesma camada, e portanto, diretamente conectado na estrutura organizacional através de um ritual. Aqui se aplicam as tipologias fraca e forte que vimos anteriormente.

**Dependência externa próxima forte**. Exemplo: o papel Mestre dos Cursos tem como responsabilidade “desenvolver e ofertar cursos inovadores”. Mas para fazer isso, precisa de uma autorização de outro círculo chamado Jurídico que tem como artefato/domínio a “novas ofertas de serviços”. O Mestre dos Cursos deve aguardar uma autorização do de algum representante do Jurídico para seguir em frente.

**Dependência externa próxima fraca. **Exemplo: o papel Produtor de Conteúdos gostaria de saber quais são as preferências dos leitores do blog antes de escrever mais textos. Existe um papel com a responsabilidade de “fornecer informações referentes aos visitantes do site” chamado Mago do WordPress. O Produtor de Conteúdo pode solicitar essas informações ao Mago WordPress. Mas caso o Mago do WordPress não esteja disponível ou priorizando esse tipo de trabalho, o Produtor de Conteúdo poderá ele mesmo buscar as informações, pois não existe artefato/domínio que limite.

As dependências entre papéis ou círculos diretamente conectados são bastante comuns e características dos trabalhos de natureza complexa, e até certo ponto, inevitáveis. Elas são facilmente navegadas e não criam grandes problemas para a organização porque os grupos envolvidos estão na “mesma camada”, e portanto possuem interações mais frequentes.

Quando possível, as dependências fortes devem ser transformadas em fracas ou então movidas para um mesmo papel ou círculo (dependência interna).

## 3) Dependência externa distante

**Ou dependência entre papéis ou círculos de camadas diferentes**

Este tipo é idêntico ao anterior, com a diferença de que os elementos conectados não estão em uma mesma camada, o que cria mais dificuldade nas interações.

Vamos analisar a seguinte estrutura:

O círculo Produtos tem como responsabilidade “lançar novos produtos para diversificar o portfólio”. Cada produto da organização é um círculo dentro deste círculo (produto A, produto B e produto C), com responsabilidade de “Desenvolver e manter produto X”. Para fazer isso, os círculos de produto precisam de uma autorização de outro círculo chamado Reputação que tem como artefato/domínio a “comunicação com a imprensa”. Cada círculo deve aguardar uma autorização do círculo de reputação para seguir em frente. Portanto temos uma dependência **forte**, representada pela imagem abaixo:

Papéis conectores podem ser usados para gerenciar este tipo de dependência. Geralmente gestores dentro de uma estrutura hierárquica buscam resolver esse problema, e o mesmo vale para o conceito de elos duplos de tecnologias sociais para autogestão baseadas na sociocracia. Mas mesmo na presença de bons conectores, um intermediário para levar e trazer a tensão sempre dificulta. Este tipo de dependência piora quanto mais camadas ou círculos existirem entre os dois elementos conectados.

No caso aqui o círculo Reputação pode ter diversos pedidos vindos dos círculos de Produtos e se ver obrigado a priorizar alguns mais do que outros. Isso coloca os círculos de cada Produto em uma situação de espera. A primeira estratégia para resolver essa tensão seria transformar uma dependência forte em dependência fraca:

Isso poderia ser feito de diversas maneiras:

**Reduzir o escopo do artefato/domínio**: Ao invés de todas as comunicações passarem pela aprovação do círculo de Reputação, definir apenas os tipos mais críticos como artefato e deixar as outras como livres.**Remover o artefato/domínio**: Seria o equivalente a inverter o propósito do círculo de Reputação. Ao invés de ser o “controlador e aprovador” das mensagens à imprensa, o círculo poderia se tornar uma consultoria interna com o objetivo de apoiar os círculos de produto a fazerem isso. Dessa forma seria responsabilidade dos círculos de Produto cuidarem da reputação, sendo o círculo de Reputação apenas um apoio.**Criando uma política/restrição**: Pode-se por exemplo definir uma regra que se as comunicações não forem aprovadas em até X dias, o círculo solicitante automaticamente ganha autoridade para seguir em frente com a comunicação desejada. Esse é só um exemplo de política/restrição mais sofisticada capaz de enfraquecer a dependência e dar mais autonomia para os círculos de Produto.

O que vai funcionar é claro que depende absolutamente de outras informações contextuais impossíveis de serem antecipadas aqui. Inclusive o design inicial com uma **dependência externa distante** pode ser o melhor design possível para um contexto onde se valoriza mais segurança do que velocidade.

Outra forma possível de enfraquecer a dependência é incorporando parte do círculo de Reputação dentro do círculo de Produtos:

Poderíamos reduzir o escopo de atuação do círculo Reputação e mover somente a responsabilidade referente à comunicação relacionada à Produtos para o próprio círculo de Produtos. Assim o círculo de Produtos poderia definir um papel internamente e adicionar neste papel o artefato/domínio “Comunicações de produtos à imprensa”. Ainda manteríamos uma dependência forte, mas ela seria transformada em uma **dependência externa próxima**.

## 4) Dependência ligada à alocação

Outro tipo de dependência comum em organizações também merece ser descrita. São aquelas em que somente funcionam se uma mesma pessoa estiver fazendo diferentes papéis, geralmente em círculos diferentes.

Poderíamos retornar no exemplo anterior dos círculos de Reputação e Produtos. Vamos supor que uma estratégia desejada por Reputação para estabelecer um maior controle das comunicações à imprensa fosse inserir um mesmo papel dentro de todos os círculos de Produto (A, B e C). Esse papel teria como objetivo colher as solicitações de comunicados, elaborá-los e revisá-los. A colheita seria responsabilidade do papel definido nos círculos de Produtos A, B e C, e a elaboração e revisão seria responsabilidade de Reputação.

Este tipo de design além de criar uma redundância desnecessária – pois o papel pode estar em Reputação – é difícil de manter, pois cada círculo tem sua própria governança e poderia alterar o papel livremente, sem manter qualquer padrão.

Mas a questão aqui não é essa. O problema maior está em que esse tipo de padrão só irá funcionar se a mesma pessoa que está alocada nos papéis inseridos nos círculos A, B e C também desempenha o papel responsável pela revisão em Reputação (estamos assumindo aqui que estas atividades não podem ser divididas sem grandes perdas).

Sabemos que coisas que **devem** ser feitas pela mesma pessoa ou grupo de pessoas **devem** estar no mesmo papel/círculo. Essa prática é nada mais do que um desmembramento em dois círculos de um papel que deveria ser feito por uma só pessoa.

Esta é uma dependência que deve ser evitada* devido à sua fragilidade. Para que tudo funcione bem, o processo/pessoa responsável pela alocação de pessoas em papéis deve manter esse “acordo implícito” na memória. Quando se trata de autogestão, normalmente cada círculo tem um papel responsável por isso (O Elo Externo / Lead Link), o que aumenta ainda mais a confusão e abre espaço para acordos por fora da governança.

*Existem algumas exceções para isso. Parecem existir algumas tensões que só se resolvem com esse tipo de dependência. Neste caso é importante também ter uma política/restrição que impede que uma alocação incorreta aconteça, ou seja, que sempre atribua a mesma pessoa para esses dois papéis acoplados em círculos diferentes.

## Otimize as dependências, não as elimine

Espero que com esse texto você possa ter ampliado a sua visão sobre os diferentes tipos de dependências existentes em organizações e que isso te ajude a fazer escolhas mais conscientes. Ressalto que **o objetivo não é eliminar as dependências**, já que isso seria impossível e talvez até inefetivo no design organizacional. **O convite é otimizar as conexões e entender os impactos** dos diferentes graus de acoplamento em um sistema social.

Lula22 de julho de 2021 at 19:25Post providencial, Davi! Tenho um papo amanhã exatamente sobre uma dependência externa distante, mas não tinha esses padrões em mente. Já me adiantou um bocado ver as possíveis soluções aqui! Muito obrigado! <3

Davi Gabriel da Silva23 de julho de 2021 at 09:18Show, que bom que foi útil meu caro! Um abraço

Bruno Lopes Mello4 de abril de 2023 at 23:23Puro ouro!