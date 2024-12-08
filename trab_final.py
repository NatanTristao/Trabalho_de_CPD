import pandas as pd

# Estrutura 1: Armazenando Dados Sobre Jogadores

def calcular_media_rating(arqMiniRating, sofifa_id):
    dados = pd.read_csv(arqMiniRating)

    avaliacoes_jogador = dados[dados['sofifa_id'] == sofifa_id] #encontrar o sofifa_id em ambos arquivos

    if avaliacoes_jogador.empty:
        return 0 

    return avaliacoes_jogador['rating'].mean() #calculo da media de rating
#-------------------------------------------

arqPlayers = pd.read_csv('players.csv')
arqTags = pd.read_csv('tags.csv')
arqMiniRating = pd.read_csv('minirating.csv')

media_avaliacoes = []
for jogador_id in arqPlayers['sofifa_id']:
    media = calcular_media_rating('minirating.csv', "sofifa_id")
    media_avaliacoes.append(media)

arqPlayers['media_rating'] = media_avaliacoes

resultado = pd.merge(arqPlayers, arqTags, on='sofifa_id', how='outer')
resultado = pd.merge(resultado, arqMiniRating, on='sofifa_id', how='outer')  

print(resultado)