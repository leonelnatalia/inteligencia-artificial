grafo = { #vizinhos
    'Teste': ['Neamt', 'Iasi'],
    'Teste2': ['Neamt'],
    'Arad': ['Zerind', 'Timisoara', 'Sibiu'],
    'Bucharest': ['Giurgiu', 'Pitesti', 'Fagaras', 'Urziceni'], 
    'Craiova': ['Dobreta', 'Rimnicu', 'Pitesti'],
    'Dobreta': ['Mehadia', 'Craiova'],
    'Eforie': ['Hirsova'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Giurgiu': ['Bucharest'],
    'Hirsova': ['Eforie', 'Urziceni'],
    'Iasi': ['Neamt', 'Vaslui', 'Teste'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Neamt': ['Iasi', 'Teste', 'Teste2'], 
    'Oradea': ['Zerind', 'Sibiu'],
    'Pitesti': ['Rimnicu', 'Craiova', 'Bucharest'],
    'Rimnicu': ['Sibiu', 'Pitesti', 'Craiova'],
    'Sibiu': ['Fagaras', 'Rimnicu', 'Arad', 'Oradea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Urziceni': ['Bucharest', 'Vaslui', 'Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Zerind': ['Oradea', 'Arad'],
}

tabela = { #distancia em linha reta ate Bucharest
    'Teste': [200],
    'Teste2': [250],
    'Arad': [366],
    'Bucharest': [0], 
    'Craiova': [160],
    'Dobreta': [242],
    'Eforie': [161],
    'Fagaras': [176],
    'Giurgiu': [77],
    'Hirsova': [151],
    'Iasi': [226],
    'Lugoj': [244],
    'Mehadia': [241],
    'Neamt': [234], 
    'Oradea': [380],
    'Pitesti': [100],
    'Rimnicu': [193],
    'Sibiu': [253],
    'Timisoara': [329],
    'Urziceni': [80],
    'Vaslui': [199],
    'Zerind': [374],
}

def busca_gulosa(grafo, tabela, inicio, objetivo):
    caminho = [inicio]
    visitados = set()
    visitados.add(inicio)

    while caminho[-1] != objetivo:
        vizinhos = grafo[caminho[-1]]
        vizinhos.sort(key=lambda cidade: tabela[cidade][0])

        for vizinho in vizinhos:
            if vizinho not in visitados:
                caminho.append(vizinho)
                visitados.add(vizinho)
                break
        

    return caminho

cidade_inicial = input("Insira a cidade inicial: ")
caminho = busca_gulosa(grafo, tabela, cidade_inicial, 'Bucharest')

print("Caminho:", caminho)