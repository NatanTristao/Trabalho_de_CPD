import pandas as pd

# Configura o Pandas para exibir floats com 2 casas decimais
pd.options.display.float_format = '{:.3f}'.format

class HashTable:

    def __init__(self, M):
        self.__hash_table = [""] * int(M)
        self.size = int(M)

    # Hash Function (just V mod M)
    def __hash(self, v):

        try:
            return int(v) % self.size
        except:
            return sum(map(ord, v)) % self.size

    # Insert a value into the table
    def insert(self, key, value):

        hash: int = self.__hash(key)

        if(self.__hash_table[hash] == ""):
           self.__hash_table[hash] = [[key, value]]
        else:
            self.__hash_table[hash].append([key, value])

    # append to list if exist
    def append(self, key, value):
        
        hash: int = self.__hash(key)


        if(self.__hash_table[hash] == ""):
            self.__hash_table[hash] = [[key, [value]]]
        else:
            l = self.__hash_table[hash] 
            for i in range(len(l)):
                if l[i][0] == key:
                    l[i][1].append(value)

                    
                    
    def ichange(self, key, value):
        
        hash: int = self.__hash(key)

        if(self.__hash_table[hash] == ""):
           self.insert(key, value)
        else:
            l = self.__hash_table[hash] 
            for i in range(len(l)):
                    if l[i][0] == key:
                        l[i][1] = value
        
    
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
            return ""

        for i in self.__hash_table[hash]:
            if i[0] == key:
                return i[1]

        return ""


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
            if self.__hash_table[i] != "":
                print(f"{i} -> {self.__hash_table[i]}")


class TrieNode:
    def __init__(self):
        self.children = {} # Cada nó possui um dicionario de filhos para armazenar caracteres
        self.players_ids = [] # IDs dos jogadores associados ao final do nome

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, name, player_id):
        node = self.root

        for char in name:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        # Adiciona o ID do jogador ao nó final do nome
        node.players_ids.append(player_id)

    def search_prefix(self, prefix):
        node = self.root

        for char in prefix:
            if char not in node.children:
                return [] #Prefixo não encontrado
            node = node.children[char]

        return self.__collect_player_ids(node)
    
    def __collect_player_ids(self, node):
        # Coleta todos os IDs de jogadores a partir do nó atual
        ids = []
        stack = [node]

        while stack:
            current = stack.pop()
            ids.extend(current.player_ids)

            for child in current.children.values():
                stack.append(child)
            
        return ids
    
# Busca jogadores avaliados por um usuário
def get_ratings_by_user(user_id):
    ratings = user_ratings.get(user_id)
    if ratings:
        return ratings
    else:
        return 0
#----------------------------------------------

# === Abrindo Arquivos ===
arqPlayers = pd.read_csv('players.csv')
arqTags = pd.read_csv('tags.csv')
arqRating = pd.read_csv('minirating.csv')


# === Criando Hashs ===
players = HashTable(arqPlayers.size) # <-- Informações dos jogadores
ratings = HashTable(arqRating.size)  # <-- Informações dos ratings
player_ratings = HashTable(arqRating.size) # <-- Notas dos jogadores
tags = HashTable(arqTags.size/1000) # <-- Tags e cada jogador que tem essa tag
positions = HashTable(arqTags.size/1000) # <-- Posições e os jogadores daquela posição

user_ratings = HashTable(arqRating.size) # <-- Informações dos ratings dados pelos usuarios

# === Lendo arquivo de Ratings ===
for i in arqRating.values.tolist():
    
    ratings.insert(i[0], i[1:]) # user_id and sofifa_id are in floating point
    player_ratings.append(i[1], i[2])

    user_id = int(i[0])
    player_id = int(i[1]) 
    rating = i[2] 
    user_ratings.append(user_id, (player_id, rating))
    
# === Lendo arquivo de players ===
for i in arqPlayers.values.tolist():
    players.insert(i[0], i[1:])
    
    for p in i[3].replace(" ","").split(","):
        positions.append(p, i[0])

# === Lendo arquivo de Tags ===
arqTags = arqTags[arqTags['tag'].notnull()]
for i in arqTags.values.tolist():
    tags.append(i[2], i[1])

    
print("Fez")

player_names_trie = Trie()

# === Insere long_names e IDs dos jogadores na Trie ===
for i in arqPlayers.values.tolist():
    player_id = i[0]
    full_name = i[1]
    player_names_trie.insert(full_name.lower(), player_id)

# === Busca IDs por prefixo ===
def search_players_by_prefix(prefix):
    prefix = prefix.lower()
    return player_names_trie.search_prefix(prefix)

print("Fez_x2")