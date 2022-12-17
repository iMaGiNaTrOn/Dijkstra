import grafo

arq = open('Grafo.txt', 'r')
tam = int(arq.readline())
cont = arq.readlines()
arq.close()

grafo = grafo.Grafo(tam)

grafo.le_matriz(tam, cont)

grafo.print_list()

vizinhos = grafo.ve_vizinhos(8)

def algoritmo_dijkstra(nodo_inicio, grafo):
    for key in grafo:
        print("key", key)
    print("nodo escolhido", nodo_inicio)

algoritmo_dijkstra(6, grafo.m_vertices)