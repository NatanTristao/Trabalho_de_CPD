# Trabalho_de_CPD
Neste trabalho vamos explorar o dataset FIFA21 - Players. Estes dados foram disponibilizados no Kaggle e a partir deles foram gerados os conjuntos de dados disponíveis para este trabalho. Os dados dos jogadores from extraídos do site https://sofifa.com e contém dados extraídos do modo carreira do FIFA 15 ao FIFA 21. 

__Estrutura 1: Armazenando Dados Sobre Jogadores__<br>
Uma tabela Hash foi construída para armazenar as informações associadas aos jogadores. A chave de acesso desta tabela Hash é o id do jogador, e os dados satélites correspondem aos dados adicionais presentes no arquivo players.csv descrito anteriormente somadas às informações de revisões de usuários sobre jogadores do arquivo. Estas informações adicionais foram calculadas. 
 
__Estrutura 2: Estrutura para buscas por strings de nomes__<br>
Uma das consultas solicitadas refere-se a uma busca por prefixos de nomes de jogadores. Para suportar esta consulta, foi construída uma árvore TRIE
 
__Estrutura 3: Estrutura para guardar revisões de usuários__<br>
As avaliações descrevem as notas atribuídas para jogadores por cada usuário. Para poder responder perguntas sobre quais jogadores um usuário avaliou foi criado uma tabela hash que retorna, para um dado usuário, quais jogadores foram avaliadas por este usuário e qual as notas que este atribui.

__Estrutura 4: Estrutura para guardar tags__<br>
Os usuários também atribuem comentários em texto livre sobre jogadores no arquivo tags.csv. A estrutura usada foi a tabela Hash que suporta consultas por um string contendo uma tag, e retornar a lista de jogadores que foram atribuídos esta tag.

__Pesquisa 1: prefixos de nomes de jogadores__<br>
Esta pesquisa tem por objetivo retornar a lista de jogadores cujo short name do jogador começa com um string passado como parâmetro. Todos os jogadores que satisfizerem o string de consulta devem ser retornados, um por linha, contendo o id do jogador, o nome curto, o nome longo, a lista de posições dos jogadores, avaliação média global e número de avaliações.
 
__Pesquisa 2: jogadores revisados por usuários__<br>
Esta pesquisa deve retornar a lista com no máximo 30 jogadores revisados pelo usuário e para cada jogador mostrar a nota dada pelo usuário, a média global e a contagem de avaliações. 
 
__Pesquisa 3: melhores jogadores de uma determinada posição__<br>
Esta pesquisa tem por objetivo retornar a lista de jogadores com melhores notas de uma dada posição. Para evitar que um jogador seja retornado com uma boa média mas com poucas avaliações, esta consulta somente deve retornar os melhores jogadores com no mínimo 1000 avaliações. Para gerenciar o número de jogadores a serem retornados, a consulta deve receber como parâmetro um número N que corresponde ao número máximo de jogadores a serem retornados. 

__Pesquisa 4: prefixos de nomes de jogadores__<br>
Esta pesquisa tem por objetivo explorar a lista de tags adicionadas por cada usuário em cada revisão. Para uma lista de tags dada como entrada, a pesquisa deve retornar a lista de jogadores que estão associados a interseção de um conjunto de tags. O resultado da consulta deve ser ordenado em ordem decrescente da nota global do jogador, e a nota global de avaliação deve usar 6 casas decimais. Além disso, o resultado da consulta deve ser impresso compacto e organizado em colunas tabuladas.
