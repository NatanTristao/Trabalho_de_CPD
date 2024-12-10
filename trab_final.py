import pandas as pd

# Configura o Pandas para exibir floats com 2 casas decimais
pd.options.display.float_format = '{:.3f}'.format

class HashTable:

    def __init__(self, M):
        self.__hash_table = [""] * M
        self.size = M

    # Hash Function (just V mod M)
    def __hash(self, v):

        try:
            v = int(v)
        except:
            v = sum(map(ord, v))
        
        return v % self.size

    # Insert a value into the table
    def insert(self, key, value):

        hash: int = self.__hash(key)

        if(self.__hash_table[hash] == ""):
           self.__hash_table[hash] = [[key, value]]
        else:
            self.__hash_table[hash].append([key, value])

    # Modify an entrie if it exists or create if not exists
    def ichange(self, key, value):
        
        hash: int = self.__hash(key)

        if(self.__hash_table[hash] == ""):
           self.insert(key, value)
        else:
            l = self.__hash_table[hash] 
            for i in range(len(l)):
                    if l[i][0] == key:
                        l[i][1] = value
                        return 0
            
            self.insert(key, value)
    
    # Modify a existing value on the hash table
    def change(self, key, value):

        hash: int = self.__hash(key)

        if(self.__hash_table[hash] == ""):
           return -1
        else:
            l = self.__hash_table[hash] 
            for i in range(len(l)):
                    if l[i][0] == key:
                        l[i][1] = value
                        return 0
            
            return -1
        
    # return a list contain the data and the number of acess until find the data in case of sucess, or
    # "" text and the number of acess until indentify that the item is not in the list
    def get(self, key):

        hash = self.__hash(key)

        tries = 1
        
        if self.__hash_table[hash] == "":
            return ["", -1*tries]

        for i in self.__hash_table[hash]:
            if i[0] == key:
                return [i[1], tries]
            tries += 1

        return ["", -1*tries]


    # Return the statistics about usage ratio, bigger list size and mean list size
    def statistics(self):
        
        used = 0
        bigger = -1
        sum_sizes = 0

        for i in self.__hash_table:
            if i != "":

                size = len(i)
                #print(i)
                
                used += 1
                sum_sizes += size

                if size > bigger:
                    bigger = size
            
        ocupation_ratio = used/self.size
        mean_list_size = sum_sizes/used

        return [ocupation_ratio, bigger, mean_list_size]

    # Print the map
    def show(self):

        for i in range(self.size):
            print(f"{i} -> {self.__hash_table[i]}")
#---------------------------------------------------

# Estrutura 1: Armazenando Dados Sobre Jogadores

def calcular_media_rating(arqMiniRating, sofifa_id):
    dados = pd.read_csv(arqMiniRating)

    avaliacoes_jogador = dados[dados['sofifa_id'] == sofifa_id] #encontrar o sofifa_id em ambos arquivos

    if avaliacoes_jogador.empty:
        return 0 

    return float(avaliacoes_jogador['rating'].mean()) #calculo da media de rating
#-------------------------------------------

arqPlayers = pd.read_csv('players.csv')
arqTags = pd.read_csv('tags.csv')
arqMiniRating = pd.read_csv('minirating.csv')

media_avaliacoes = []
for jogador_id in arqPlayers['sofifa_id']:
    media = calcular_media_rating('minirating.csv', jogador_id)
    media_avaliacoes.append(media)

arqPlayers['media_rating'] = media_avaliacoes

resultado = pd.merge(arqPlayers, arqTags, on='sofifa_id', how='outer')
resultado = pd.merge(resultado, arqMiniRating, on='sofifa_id', how='outer')  

print(resultado)