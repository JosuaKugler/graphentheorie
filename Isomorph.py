import dsa

def wennAlleGeradeGleichSind(graph):
    if len(dsa.neighbors(graph, graph.nodes[0])) < 3:
        return True
    for node in graph.nodes:
        print("A")
    return False

def neighbours(graph, node):
    """returns the neighbours of "node" in the graph "graph" """
    ret = []
    for other_node in graph.nodes:
        if graph.get_edge(node, other_node):
            ret.append(other_node)
    return ret

def vergleiche2(graph1, graph2):
    AnzahlPassendeKnoten = []
    passendeKnoten0 = []
    for node in graph1:
        passendeKnoten = vergleiche(graph1, graph2, node)
        AnzahlPassendeKnoten.append(len(passendeKnoten))
        minAnzahlPassendeKnoten = len(passendeKnoten)
        passendeKnoten0.append(passendeKnoten)
    for zahl in AnzahlPassendeKnoten:
        if Zahl < minAnzahlPassendeKnoten:
            Zahl = minAnzahlPassendeKnoten
        

def vergleiche(graph1, graph2, node1):
    passendeKnoten = []
    E1 = macheErreichbarkeitshiraschie(graph1, node1)
    #print(E1)
    #print(gibStufe(E1))
    E2 = wandleErreichbarkeitshiraschieUm(E1, gibStufe(E1))
    #print(E2)
    for node in graph2.nodes:
        E3 = macheErreichbarkeitshiraschie(graph2, node)
        #print(E3)
        #print(gibStufe(E3))
        E4 = wandleErreichbarkeitshiraschieUm(E3, gibStufe(E3))
        #print(E4)
        if vergleicheErreichbarkeitshiraschie(E2, E4):
            passendeKnoten.append(node)
    #print(passendeKnoten)
    return passendeKnoten

def findeDreiecke(graph, node):
    Dreiecke = []
    neighbours = neighbours(graph, node)
    for node1 in neighbours:
        for node2 in neighbours:
            if get_edge(node1, node2):
                Dreieck = {node, node1, node2}
                Dreiecke.append(Dreieck)

def macheErreichbarkeitshiraschie(graph, node):
    stufe = 0
    Erreichbarkeitshiraschie = {node: stufe}
    lenErreichbarkeitshiraschie = -1
    while len(Erreichbarkeitshiraschie) < len(graph.nodes):
        #print(str(len(Erreichbarkeitshiraschie)) + ", " + str(len(graph.nodes)))
        #print(Erreichbarkeitshiraschie)
        if lenErreichbarkeitshiraschie == len(Erreichbarkeitshiraschie):
            #print("Hallo")
            for node in graph.nodes:
                if node not in Erreichbarkeitshiraschie:
                    Erreichbarkeitshiraschie[node] = -1
        lenErreichbarkeitshiraschie = len(Erreichbarkeitshiraschie)
        for node in graph.nodes:
            #print(str(node) + str(Erreichbarkeitshiraschie) + str(stufe))
            if node in Erreichbarkeitshiraschie and Erreichbarkeitshiraschie[node] == stufe:
                nnode = neighbours(graph,node)
                #print(nnode)
                for n in nnode:
                    if n not in Erreichbarkeitshiraschie:
                        Erreichbarkeitshiraschie[n] = stufe+1
                        
        stufe = stufe +1
    return Erreichbarkeitshiraschie

def gibStufe(Erreichbarkeitshiraschie):
    stufe = 0
    for node in Erreichbarkeitshiraschie:
        if Erreichbarkeitshiraschie[node] > stufe:
            stufe = Erreichbarkeitshiraschie[node]
    return stufe

def wandleErreichbarkeitshiraschieUm(Erreichbarkeitshiraschie, stufe):
    NeueErreichbarkeitshiraschie = {}
    for i in range(-1,stufe+1):
        NeueErreichbarkeitshiraschie[i] = 0
    #print(NeueErreichbarkeitshiraschie)
    for node in Erreichbarkeitshiraschie:
        Zahl = Erreichbarkeitshiraschie[node]
        NeueErreichbarkeitshiraschie[Zahl] = NeueErreichbarkeitshiraschie[Zahl] + 1
        #print(NeueErreichbarkeitshiraschie)
    return NeueErreichbarkeitshiraschie
        
def vergleicheErreichbarkeitshiraschie(Eh1, Eh2):
    for i in Eh1:
        if Eh1[i] != Eh2[i]:
            return False
    return True

def gib3Ecke(graph):
    for edge in graph.edges:
        nodes = graph.edge_to_vertices(edge2)
        neigbours1 = neighbours(graph,nodes[0])
        neigbours2 = neighbours(graph,nodes[1])
        for node1 in neighbours1:
            for node2 in neighbours2:
                if node1 == node2:
                    a = 1
def gibGraph():
    g = dsa.Graph()
    g.make_node("1")
    g.make_node("2")
    g.make_node("3")
    g.make_node("4")
    g.make_node("5")
    g.make_node("6")
    g.make_node("7")
    g.make_node("8")
    g.make_node("9")
    g.make_edge("1", "2")
    g.make_edge("1", "3")
    g.make_edge("2", "4")
    g.make_edge("3", "5")
    g.make_edge("4", "6")
    g.make_edge("5", "7")
    g.make_edge("6", "8")
    g.make_edge("7", "1")
    g.make_edge("8", "2")
    g.make_edge("3", "4")
    g.make_edge("5", "6")
    g.make_edge("7", "8")
    return g
a = gibGraph()
b = gibGraph()
print(vergleiche(a, b, "1"))
print(macheErreichbarkeitshiraschie(gibGraph(), "1"))
