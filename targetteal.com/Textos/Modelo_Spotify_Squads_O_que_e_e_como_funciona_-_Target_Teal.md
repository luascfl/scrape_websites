---
title: Modelo Spotify Squads: O que é e como funciona - Target Teal
author: Davi Zimmer
url: https://targetteal.com/blog/modelo-spotify-squads/
hostname: targetteal.com
description: Conheça o "modelo Spotify Squads" e entenda como funcionam os seus elementos: Squads, Chapters, Tribes e Guilds.
sitename: Target Teal
date: 2018-11-12
categories: ['Ágil']
---
Henrik Kniberg publicou um vídeo em 2014 que popularizou o que muitos hoje conhecem como “modelo Spotify Squads”. Neste artigo, veremos os principais elementos da estrutura organizacional descrita por ele, como Squads, Chapters, Guilds e Tribes.

Vou me manter fiel à descrição da cultura de engenharia de software feita por Henrik no vídeo. No final do texto falaremos sobre porque copiá-lo pode não ser uma boa ideia para a sua organização.

## O que é afinal o “modelo Spotify Squads”?

No início, o Spotify era uma empresa pequena, que basicamente utilizava o framework Scrum, com seus times pequenos e multidisciplinares. Conforme o número de equipes foi aumentando, eles perceberam que algumas práticas do Scrum não faziam mais tanto sentido para eles. A conclusão foi: os princípios do Ágil são mais importantes do que um método específico.

Como resultado, o Spotify renomeou o antigo papel de “Scrum Master” para “Agile Coach”. A intenção era que o Agile Coach fosse menos um especialista em Scrum, e mais um líder-servidor capaz de estimular e suportar a melhoria contínua. A segunda medida foi passar a chamar as equipes multidisciplinares de “**Squads**“, ao invés de “Times Scrum”.

As Squads, além de contarem com especialistas de diferentes funções, são auto-organizados e pequenos (8 ou menos integrantes). Eles possuem responsabilidade ponta a ponta, ou seja, projetam, desenham, desenvolvem e dão manutenção aos produtos Spotify. As Squads também têm um nível elevado de autonomia: eles decidem o que construir, como construir e como trabalhar juntos para construir. Coisa que muitas organizações nem sequer experimentam.

Obviamente, a autonomia das Squads não é infinita. Algumas restrições afetam esse nível de liberdade: geralmente a missão da própria Squad (toda Squad tem uma), a estratégia geral de produto e objetivos de curto-prazo negociados a cada trimestre.

Essa estrutura potencializa a autonomia, que por ser um motivador intrínseco forte, torna as pessoas mais felizes. Além, a estrutura em Squads dá muita velocidade, pois evita esquemas de aprovação, afunilamento de decisões no topo e dependência de outras equipes.

Mas segundo o Kniberg, autonomia não é o suficiente para construir produtos incríveis. Ele afirma no vídeo que alinhamento (em inglês, alignment) também é vital para o modelo Spotify. Em linhas gerais, todas as Squads precisam estar “alinhados” com a estratégia da empresa, objetivos trimestrais e outras Squads. A missão do Spotify como organização é mais importante do que a missão individual de qualquer Squad.

Para possibilitar o alinhamento sem sacrificar a autonomia, o papel da liderança no Spotify torna-se muito mais *comunicar qual problema deve ser resolvido e porquê*. O *como* o problema será resolvido é tarefa das Squads.

## Outros elementos: Chapters, Guilds e Tribes

Na data do vídeo (2014), Henrik disse que o Spotify tinha mais de 50 Squads, distribuídos em 4 países. Algum tipo de estrutura além do time multidisciplinar, pequeno e auto-organizado é necessária para coordenar os esforços de tanta gente. É aí que entram as **Tribes**.

Uma **Tribe** é uma estrutura matricial leve, composta por um conjunto de Squads e Chapters. Como vimos, cada Squad é geralmente focada em um segmento do produto. Já os **Chapters** são áreas de competência, como desenvolvimento, qualidade de software ou Agile coaching. Cada Chapter possui um Chapter Lead, que é um gerente de linha, ou líder-servidor que atua no apoio ao desenvolvimento de uma determinada competência. Como membro desta estrutura, você sempre faz parte de um Chapter e uma Squad pelo menos.

As Squads possuem um Product Owner, que atua de forma semelhante ao que prega o Scrum, refinando o Backlog e definindo as prioridades daquela Squad. As Tribes possuem um Tribe Lead, que dá orientações gerais de prioridade e objetivos de negócio para toda a Tribe.

O último elemento descrito por Kniberg são as **Guilds**, que são comunidades de prática focadas em um determinado tema (como testes unitários), que podem atravessar diferentes Tribes, Squads e Chapters. As Guilds têm caráter voluntário e são formadas conforme interesse das pessoas nos temas que as originam.

## Práticas de engenharia de software

Existem algumas práticas de engenharia de software que são vitais no “modelo Spotify Squads”, mas geralmente ignoradas pelas empresas que se inspiram nele.

**Inner Source**. As Squads podem criar bibliotecas, componentes ou trechos de código que são utilizadas por outras Squads. Uma vez feito isso, a Squad A, por exemplo, vira a “guardiã” daquela biblioteca. Quando a Squad B precisa alterar esse componente, ela têm duas opções. A primeira e mais intuitiva, é pedir que a Squad A implemente a mudança. Mas se isso não for possível (porque a Squad A está focada em outra coisa), a Squad B pode alterar ela mesmo o trecho de código e enviar para revisão da Squad A. Isso impede que um time fique travado esperando alterações do outro. Esta prática é conhecida como Inner Source, ou Open Source Interno.

**Release Train e Feature Toggle**. Cada aplicação cliente Spotify possui um “Release Train” (trem de lançamento), que roda regularmente, normalmente a cada semana ou quinzena. Este trem carrega todas as funcionalidades implementadas pelas Squads no período anterior e as coloca em produção, mesmo que não estejam prontas. O que acontece é que o outro recurso, chamado de “Feature Toggle”, permite que as Squads desabilitem as funcionalidades que ainda não estão prontas. Esse processo de entrega contínua permite que o Spotify evite os tenebrosos problemas de integração e deploy, tão frequentes no desenvolvimento de software, especialmente em empresas grandes.

## O Modelo Spotify Squads não é uma tecnologia social!

Depois de detalhar o que é conhecido e inspirador para muitos, preciso ressaltar esse ponto: o modelo Spotify squads não é uma **tecnologia** **social**. Este é um termo que utilizamos frequentemente aqui no blog da Target Teal. Uma tecnologia social é um conjunto de práticas que são desenvolvidas e testadas por especialistas em design organizacional. Ou seja, tecnologias sociais são “modelos” que almejam a disseminação e uso por várias organizações. Exemplos incluem o Scrum, Kanban, ou o método Organização Orgânica.

O que é conhecido hoje como modelo Spotify squads é apenas uma descrição do estado momentâneo das práticas ágeis no dia da gravação do vídeo pelo Henrik. Ele mesmo fala que aquilo chega a ser uma descrição fantasiosa, porque a realidade é muito mais complexa.

Outro problema é que o suposto modeloSpotify squads perde totalmente o sentido se aplicado em outras áreas/organizações que não trabalham com desenvolvimento de software. Por exemplo, um squad é um time multidisciplinar. Ou seja, uma área de RH nunca poderá ser um squad, como vemos por aí. No entanto, talvez você queira trazer os princípios da auto-organização do Scrum para a sua área de RH. Isso é perfeitamente possível com autogestão ou uma tecnologia social criada para este propósito, como o O2.

Por esses motivos acreditamos que o modelo Spotify é uma grande inspiração, mas não passa disso. Existem outras tecnologias sociais muito mais efetivas para criar mais autonomia no trabalho e ainda assim manter um alto nível de alinhamento, como a Organização Orgânica.

Equipe multidisciplinar: o que é e como montar uma? - Blog do Instituto Atlântico - Desenvolvimento de soluções tecnológicas21 de janeiro de 2019 at 10:12[…] disso, uma alternativa — que é utilizada pelo Spotify, inclusive — consiste na formação de uma estrutura organizacional funcional para trabalhar […]

Jonas3 de janeiro de 2021 at 10:52Muito claro e objetivo. Obriado pelo artigo.

O que não fazemos - Target Teal16 de fevereiro de 2021 at 09:38[…] Além do escopo do projeto, sabemos que quando uma grande empresa nos contrata para algo que vai além de alguns workshops, ela está buscando alguém que vai incomodar e propor coisas que não foram consideradas. E esse tipo de contratação precisa ter um comprometimento e envolvimento da alta gestão, e não pode ficar restrito ao redesenho de um organograma. Por mais que ele faça uso de termos que estão na moda, como “squads”. […]

Quais habilidades Pessoas Designers aprendem na marra? (Parte 1) | Lambda32 de setembro de 2021 at 13:50[…] uma empresa de tecnologia, é muito comum a formação de times no formato de squad: Modelo popularizado pelo Spotify, que consiste em formar pequenas equipes multidisciplinares com autonomia e dedicação total para […]

5 motivos para apostar em Squad as a Service - Arpia Tecnologia12 de julho de 2022 at 10:40[…] O método ganhou popularidade em 2014, quando o Spotify publicou um vídeo no qual mostrava a organização de seus times de desenvolvimento e apresentava o conceito de Squad as a Service: uma pequena equipe multifuncional e autogerenciada. […]