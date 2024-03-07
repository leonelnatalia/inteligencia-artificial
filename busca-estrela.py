grafo = { #vizinhos
    'Teste': {'Neamt': 150, 'Iasi': 100},
    'Teste2': {'Neamt': 60},
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Bucharest': {'Giurgiu': 90, 'Pitesti': 101, 'Fagaras': 211, 'Urziceni':85}, 
    'Craiova': {'Dobreta': 120, 'Rimnicu': 145, 'Pitesti': 138},
    'Dobreta': {'Mehadia': 75, 'Craiova': 120},
    'Eforie': {'Hirsova': 86},
    'Fagaras': {'Sibiu': 99,'Bucharest':211},
    'Giurgiu': {'Bucharest': 90},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Iasi': {'Neamt': 87, 'Vaslui': 92, 'Teste': 100},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Dobreta':75},
    'Neamt': {'Iasi': 87, 'Teste': 150, 'Teste2': 60}, 
    'Oradea': {'Zerind': 71,'Sibiu': 151},
    'Pitesti': {'Rimnicu': 97, 'Craiova': 138, 'Bucharest': 101},
    'Rimnicu': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 148},
    'Sibiu': {'Fagaras': 99, 'Rimnicu': 80, 'Arad': 140, 'Oradea': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Zerind': {'Oradea': 71, 'Arad': 75},
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

def busca_estrela(grafo, tabela, inicio, objetivo):
    caminho = [inicio]
    visitados = set()
    visitados.add(inicio)

    while caminho[-1] != objetivo:
        cidade_atual = caminho[-1]
        vizinhos = grafo[cidade_atual]

        distancias_vizinhos = [
            (cidade, tabela[cidade][0] + grafo[cidade_atual][cidade])
            for cidade in vizinhos
        ]

        distancias_vizinhos.sort(key=lambda tupla: tupla[1])

        for vizinho, distancia in distancias_vizinhos:
            if vizinho not in visitados:
                caminho.append(vizinho)
                visitados.add(vizinho)
                break

    return caminho

cidade_inicial = input("Insira a cidade inicial: ")
caminho = busca_estrela(grafo, tabela, cidade_inicial, 'Bucharest')

print("Caminho:", caminho)
