class Grafo:
    # Construtor da lista de adjacencia através de um dicionario para orientar
    def __init__(self, num_v):
        self.m_num_v = num_v
        self.m_vertices = range(self.m_num_v)

        self.m_list_adj = {vertice: list() for vertice in self.m_vertices}

    # Adiciona arestas 
    def add_aresta(self, v1, v2, peso=0):
        self.m_list_adj[v1].append([v2, peso])
        self.m_list_adj[v2].append([v1, peso])

    # Printa a lista de adjacencia
    def print_list(self):
        for key in self.m_list_adj.keys():
            print("vertice", key, ": ", self.m_list_adj[key])    

    # Função para ler a matriz de adjacencia referente ao grafo que será utilizado 
    def le_matriz(self, num_v, conteudo):
        for i in range(0, num_v):
            conca = ''
            count = 0
            for j in conteudo[i]:
                if j == '\n':
                    valor = int(conca)
                    if count <= i: 
                        break
                    elif valor == 0: 
                        break
                    else:
                        self.add_aresta(i, count, valor)
                        conca = ''
                        count += 1
                        break
                if j != ' ':
                    conca = conca + j
                    continue
                if j == ' ':
                    valor = int(conca)
                    if count <= i: 
                        count += 1
                        conca = ''
                        continue
                    elif valor == 0: 
                        count += 1
                        conca = ''
                        continue
                    else:
                        self.add_aresta(i, count, valor)
                        conca = ''
                        count += 1
                        continue

    def ve_vizinhos(self, nodo):
        vizinhos = []
        for i in self.m_list_adj[nodo]:
            vizinhos.append(i)
        return vizinhos
    
    def print_vizinhos(self, vizinhos):
        for i in vizinhos:
            print(i)
            
    
    