---
title: Criando o Modelo Spotify com O2 - Target Teal
author: Davi Zimmer
url: https://targetteal.com/blog/modelo-spotify-com-o2/
hostname: targetteal.com
description: Recentemente, exploramos como a Organização Orgânica (O2) pode ser utilizada para replicar o modelo RenDanHeYi da Haier. Hoje, vamos demonstrar como a O2 pode
sitename: Target Teal
date: 2024-08-05
categories: ['Ágil']
---
Recentemente, exploramos como a Organização Orgânica (O2) pode ser utilizada para replicar o modelo RenDanHeYi da Haier. Hoje, vamos demonstrar como a O2 pode ser aplicada para implementar o modelo Spotify, destacando sua versatilidade como uma tecnologia social capaz de se adaptar a diferentes estruturas organizacionais.

O modelo Spotify, conhecido por sua abordagem ágil e flexível para o desenvolvimento de produtos, tem inspirado muitas organizações a repensar suas estruturas, inclusive empresas que não trabalham com tecnologia. Neste artigo, mostraremos como os elementos-chave do modelo Spotify podem ser recriados utilizando a Organização Orgânica, adicionando ainda uma camada estrutural que permite uma evolução constante.

Aqui não vamos entrar no mérito se você deve ou não copiar o modelo Spotify na sua organização. O que quero demonstrar é o quanto um sistema de governança como a O2 é versátil o suficiente para replicar a suposta estrutura do Spotify e talvez seja uma escolha mais interessante para a sua organização.

Para aproveitar ao máximo este texto, recomendamos que você esteja familiarizado com o modelo Spotify e tenha um conhecimento básico da Organização Orgânica (O2).

## Elementos fundamentais do modelo Spotify

Você já sabe, mas não custa relembrar. O modelo Spotify é composto por quatro elementos principais:

**Squads**: Equipes multidisciplinares e auto-organizadas, semelhantes a mini-startups. Cada squad é responsável por uma parte específica do produto e tem autonomia para decidir como trabalhar.**Tribos**: Agrupamentos de squads relacionados que trabalham em áreas similares do produto. Uma tribo geralmente contém até 100 pessoas e é liderada por um Tribe Lead.**Capítulos**: Grupos de pessoas com habilidades similares que trabalham em diferentes squads dentro de uma tribo. Os capítulos promovem o compartilhamento de conhecimento e o desenvolvimento profissional.**Guildas**: Comunidades de interesse que atravessam as fronteiras das tribos. São grupos orgânicos e voluntários que reúnem pessoas com interesses comuns, independentemente de sua posição na organização.

Estes elementos trabalham em conjunto para criar uma estrutura que equilibra autonomia e alinhamento, permitindo que os times tenham muita agilidade autonomia enquanto mantêm a coesão organizacional.

## Squads e Tribos como Círculos

Os Squads podem ser representados como círculos internos dentro dos círculos de Tribo. Isso permite definir um propósito claro, responsabilidades específicas e manter a autonomia característica dos Squads. Por exemplo:


Círculo: Squad de Checkout

Propósito: Experiência de checkout fluida e segura para maximizar as conversões

Responsabilidades:

- Desenvolver e manter o fluxo de checkout
- Implementar e otimizar métodos de pagamento
- Tomar ações para melhorar a segurança das transações
- Analisar e melhorar as taxas de conversão

Uma vantagem significativa da O2 é que ela oferece um sistema de governança completo para os Squads, permitindo que eles definam seus próprios papéis e evitem estruturas de poder implícito. Isso resolve uma limitação do modelo Spotify original, onde a auto-organização dos Squads pode levar a dinâmicas de grupo desestruturadas.

As Tribos podem ser implementadas como círculos diretamente ligados ao círculo geral da organização, agrupando Squads relacionados e facilitando a coordenação entre eles.

## Capítulos e Guildas como Círculos

Diferentemente do modelo Spotify, onde Capítulos e Guildas são estruturas “transversais”, na O2 eles seriam implementados como círculos regulares. A O2 não possui conceito de estruturas transversais, pois qualquer círculo pode interagir livremente com outros círculos e pessoas na organização.

Os círculos dos Capítulos devem estar localizados dentro dos círculos das Tribos, enquanto que os círculos das Guildas dentro do Círculo Geral. Caso um Capítulo seja responsável por padronizar alguma prática na organização inteira, basta adicionar na descrição do círculo correspondente o artefato necessário.

Por exemplo, imagine que o capítulo de “Design” necessita definir uma ferramenta padronizada para ser utilizada por toda a organização no que tange a produção de protótipos de interface para o usuário. Isso poderia ser um artefato do círculo desse capítulo: “Ferramentas de protótipos”. Então esse círculo poderia publicar orientações para as Squads de como fazer uso dessas ferramentas.

Para garantir que as pessoas que desempenham papéis nos Squads também estejam automaticamente alocadas nos Capítulos correspondentes, podemos implementar uma restrição de alocação no círculo geral. Por exemplo:


Restrição: Alocação Automática em CapítulosQuando um parceiro for atribuído a um papel técnico específico (por exemplo, desenvolvedor, designer, analista de dados) em um Squad, o @Guia do Círculo deve:


- Verificar se existe um Capítulo correspondente à especialidade técnica do papel.
- Se existir, atribuir o parceiro a um papel genérico de “Membro” nesse Capítulo.
- Informar tanto o parceiro quanto o @Guia do Capítulo sobre a nova atribuição.
Esta alocação automática não impede que o parceiro assuma papéis adicionais no Capítulo.


## Modelo de open-source interno

Uma prática pouco falada mas bastante importante dentro da cultura Spotify é o modelo open-source interno. Sempre que uma Squad produz algum componente de software que pode ser reutilizado, ela se torna proprietária daquele repositório. Outros times da organização podem fazer uso dessa porção de código e inclusive melhorá-la, mas as alterações geralmente são revisadas pela Squad que criou o componente.

Na O2, esse efeito pode ser facilmente imitado adicionando esses repositórios de código como “artefatos” dos círculos que os criaram. Outros círculos (Squads) podem então submeter mudanças nesses códigos e a Squad original que detém o artefato pode aprovar essas mudanças ou não. Obviamente essa lógica pode ser extrapolada para outras coisas que não produtos digitais.

## Papéis do modelo Spotify com O2

Ao adaptar o modelo Spotify para a O2, é importante reconhecer que muitas das responsabilidades associadas aos papéis-chave do Spotify já estão contempladas nos papéis essenciais da O2 ou podem ser facilmente incorporadas à estrutura existente. Vamos ver caso a caso:

**Product Owner (PO)**: Na O2, algumas das responsabilidades tradicionalmente atribuídas ao PO, como a priorização, são análogas às do Guia do Círculo. Portanto, não há necessidade de replicar essas funções em um papel separado de PO. No entanto, cada círculo (Squad) pode optar por criar um papel de PO focado especificamente em atividades de negócio, como:

- Definição e refinamento de requisitos de produto
- Interface com stakeholders externos
- Pesquisa de mercado e análise de concorrência

A mesma pessoa que é Guia do círculo da Squad poderia assumir esse papel adicional.

**Agile Coach**: Na O2, o papel de Facilitador do círculo já assume a responsabilidade de conduzir reuniões e facilitar os processos do círculo. Portanto, um papel separado de Agile Coach pode não ser necessário. No entanto, os círculos têm a flexibilidade de:

- Adicionar responsabilidades relacionadas ao coaching ágil ao papel do Facilitador
- Criar um papel específico de Agile Coach, se necessário, com responsabilidades como:
- Mentoria em práticas ágeis
- Facilitação de workshops de melhoria contínua
- Suporte na resolução de impedimentos complexos


**Tribe Lead**: Este papel é essencialmente equivalente ao do Guia do Círculo na O2 (no caso, o Guia dos Círculos das Tribos). Não há necessidade de criar um papel separado de Tribe Lead, a menos que sejam necessárias atividades adicionais específicas que não estejam cobertas pelas responsabilidades padrão do Guia.

É crucial entender que, ao contrário do modelo Spotify original, a O2 não garante uniformidade desses papéis entre diferentes círculos. Isso ocorre porque cada círculo na O2 tem autonomia para modificar sua própria governança. Consequentemente:

- Diferentes Tribos (círculos) podem adaptar as responsabilidades do Tribe Lead (se for criado) conforme necessário.
- Squads dentro da mesma Tribo podem ter variações na definição do papel de Product Owner ou decidir distribuir essas responsabilidades de outras formas.

Essa falta de uniformidade pode ser vista como um desafio para organizações que buscam uma implementação “pura” do modelo Spotify. No entanto, também representa uma força da O2, permitindo que cada parte da organização adapte sua estrutura às suas necessidades específicas.

Os capítulos também podem exercer alguma influência contrária sugerindo uma padronização dos papeis, por exemplo, mas caberá sempre aos círculos seguirem esse padrão ou não.

## Conclusão

Adaptar o modelo Spotify usando a O2 mostra como essa tecnologia social é flexível. Ao transformar Squads, Tribos, Capítulos e Guildas em círculos da O2, criamos algo que vai além do modelo original. A O2 oferece uma grande vantagem ao resolver um desafio comum em times ágeis: a falta de estrutura clara para tomada de decisão. Muitas vezes, esses times acabam dependendo demais do consenso ou de acordos informais, o que pode criar estruturas de poder paralelas. A O2 traz contornos claros para decidir coisas e definir papéis, evitando esses problemas.

Outro ponto forte da O2 é que ela responde a uma questão que o modelo Spotify deixa em aberto: como criar novos Squads, Tribos ou Capítulos? Na O2, isso é feito de forma clara através do processo de governança, usando a interação Adaptar. Isso dá um caminho definido para a evolução da estrutura, algo que o modelo Spotify por si só não oferece.

Claro, toda essa flexibilidade também traz seus desafios, principalmente em manter alguma consistência entre os times. Se você quer implementar esse mix de Spotify e O2, esteja preparado para lidar com diferentes formas de trabalhar dentro da mesma organização. O segredo é focar mais no alinhamento de propósito e menos em padronizar tudo. Assim, dá para aproveitar o melhor dos dois modelos, criando uma estrutura que se adapta continuamente às mudanças, mas com um processo claro para essa adaptação.

## Conteúdos sobre Autogestão & O2

Inscreva-se abaixo para receber mais conteúdos sobre autogestão & O2 por email.