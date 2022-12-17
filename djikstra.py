import grafo

arq = open('Grafo.txt', 'r')
tam = int(arq.readline())
cont = arq.readlines()
arq.close()

grafo = grafo.Grafo(tam)

grafo.le_matriz(tam, cont)

grafo.print_list()

def algoritmo_dijkstra(nodo_inicio, grafo):
    nao_visitados = grafo.retorna_nodos()
    
    # caminho mais curto a partir do ponto de inicio
    mais_curto = {}
    # os nodos anteriores a ele
    anteriores = {}
    
    # valor maximo, simulando um infinito
    valor_max = 10000000
    for nodo in nao_visitados:
        mais_curto[nodo] = valor_max
    
    # o nodo inicial tem custo 0, então zeramos ele
    mais_curto[nodo_inicio] = 0
    
    # laço que vai manter o código funcionando
    while nao_visitados:
        nodo_min_atual = None
        
        # iterando sob os nodos
        for nodo in nao_visitados:
            if nodo_min_atual == None:
                nodo_min_atual = nodo
            elif mais_curto[nodo] < mais_curto[nodo_min_atual]:
                nodo_min_atual = nodo

        # vê os vizinhos do nodo min atual e da update nas distancias
        vizinhos = grafo.ve_vizinhos(nodo_min_atual)
        for vizinho in vizinhos:
            tentativa_valor = mais_curto[nodo_min_atual] + vizinho[1]
            if tentativa_valor < mais_curto[vizinho[0]]:
                mais_curto[vizinho[0]] = tentativa_valor
                anteriores[vizinho[0]] = nodo_min_atual
                
        nao_visitados.remove(nodo_min_atual)
    
    return anteriores, mais_curto

def printa_dijkstra(nodos_anteriores, caminho_curto, nodo_inicio, nodo_alvo):
    caminho = []
    nodo = nodo_alvo
    
    while nodo != nodo_inicio:
        caminho.append(nodo)
        nodo = nodos_anteriores[nodo]
        
    caminho.append(nodo_inicio)
    
    print("O menor caminho até", nodo_alvo, "tem valor de", caminho_curto[nodo_alvo])
    print(*reversed(caminho), sep=" -> ")
    
nodo_inicial = int(input("Qual nodo será o inicial? "))
nodo_objetivo = int(input("Qual o nodo que deseja chegar? "))

nodos_anteriores, mais_curto = algoritmo_dijkstra(nodo_inicial, grafo)

printa_dijkstra(nodos_anteriores, mais_curto, nodo_inicial, nodo_objetivo)
