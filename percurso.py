import numpy
from collections import deque

def ler_arquivo_grafo(nome_arquivo_grafo):
    matriz_adjacencias = numpy.loadtxt(open(nome_arquivo_grafo, "rb"), delimiter=",", skiprows=0)
    return matriz_adjacencias


def busca_profundidade(matriz_adjacencias, vertice_atual = 0, vertices_visitados = set()):
    vertices_visitados.add(vertice_atual)
    print(str(vertice_atual), end=", ")
    for i in range(len(matriz_adjacencias[vertice_atual])):
        if matriz_adjacencias[vertice_atual][i] > 0 and i not in vertices_visitados:
            busca_profundidade(matriz_adjacencias, i, vertices_visitados)


def busca_largura(matriz_adjacencias, vertice_atual = 0):
    fila_vertices = deque([])
    vertices_visitados = set()
    vertices_visitados.add(vertice_atual)
    print(str(vertice_atual), end=", ")
    fila_vertices.append(vertice_atual)

    while len(fila_vertices) > 0:
        vertice_atual = fila_vertices.popleft()
        for i in range(len(matriz_adjacencias[vertice_atual])):
            if matriz_adjacencias[vertice_atual][i] > 0 and i not in vertices_visitados:
                vertices_visitados.add(i)
                print(str(i), end=", ")
                fila_vertices.append(i)


if __name__ == '__main__':
    nome_arquivo = 'arquivos_grafos/Parte1_Aciclico.csv'
    matriz_adjacencias = ler_arquivo_grafo(nome_arquivo)

    print(f"Arquivo: {nome_arquivo}")
    print(matriz_adjacencias)

    print("\n***Busca por profundidade***")
    busca_profundidade(matriz_adjacencias)

    print("\n***Busca por largura***")
    busca_largura(matriz_adjacencias)