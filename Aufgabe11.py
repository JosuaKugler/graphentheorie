import dsa
import random
random.seed(42)

def Liniengraph(graph):
    Liniengraph = dsa.Graph()
    for edge in graph.edges:
        Liniengraph.make_node(str(edge))
    #print(Liniengraph)
    for edge in graph.edges:
        Nodes = graph.edge_to_vertices(edge)
        for edge2 in graph.edges:
            if edge == edge2:
                continue
            Nodes2 = graph.edge_to_vertices(edge2)
            #Auf Übereinstimmung prüfen
            if Nodes[0] == Nodes2[0] or Nodes[0] == Nodes2[1] or Nodes[1] == Nodes2[0] or Nodes[1] == Nodes2[1]:
                #print(edge)
                #print(edge2)
                if not Liniengraph.get_edge(str(edge), str(edge2)):
                    Liniengraph.make_edge(str(edge), str(edge2))
    return Liniengraph
        #Nachbarn = neighbours(graph, Nodes[0]) + neighbours(graph, Nodes[1])
        #for node in Nachbarn:
         #   if not Liniengraph.get_edge(Nodes[0], node):
          #      graph.get_edge
           #     Liniengraph.make_edge()
            #if not Liniengraph.get_edge(Nodes[1], node):             
             #   Liniengraph.make_edge(Nodes[1], node)
        
def neighbours(graph, node):
    """returns the neighbours of "node" in the graph "graph" """
    ret = []
    for other_node in graph.nodes:
        if graph.get_edge(node, other_node):
            ret.append(other_node)
    return ret

def Kreis(AnzahlNodes):
    if AnzahlNodes < 3:
        AnzahlNodes = 3
    Graph = dsa.Graph()
    Graph.make_node(str(0))
    for i in range(1,AnzahlNodes):
        Graph.make_node(str(i))
        Graph.make_edge(str(i), str(i-1))
        #print(hamiltonisch(Graph))
    Graph.make_edge(str(0), str(AnzahlNodes-1))
    return Graph

def HamiltonscherGraph(AnzahlEdges, AnzahlNodes):
    if AnzahlNodes < 3:
        AnzahlNodes = 3
        print("Unzulässige Eingabe. Die Eingabe wurde korrigiert.")
    if AnzahlNodes > AnzahlEdges:   #Ein Hamiltonscher Graph muss eine Mindestanzahl an Kanten haben
        AnzahlEdges = AnzahlNodes
        print("Unzulässige Eingabe. Die Eingabe wurde korrigiert.")
    if AnzahlEdges > AnzahlNodes*(AnzahlNodes-1)/2: #Der Graph darf nich mehr Kanten als ein vollständiger Graph haben
        AnzahlEdges = AnzahlNodes*(AnzahlNodes-1)/2
        print("Unzulässige Eingabe. Die Eingabe wurde korrigiert.")
    AnzahlEdgesImGraph = AnzahlNodes #EinKries hat so viele Knoten wie Kanten
    Graph = Kreis(AnzahlNodes)
    #print(Graph)
    while AnzahlEdgesImGraph < AnzahlEdges: # Zufällig wietere Kanten einfügen bis die gewünschte Zahl erreicht wurde.
        Node1 = random.randint(0, AnzahlNodes-1)
        Node2 = random.randint(0, AnzahlNodes-1)
        if (not Node1 == Node2) and not Graph.get_edge(str(Node1),str(Node2)):
            Graph.make_edge(str(Node1),str(Node2))
            AnzahlEdgesImGraph = AnzahlEdgesImGraph + 1
    return Graph

def EulerscherGraph(AnzahlEdges, AnzahlNodes):
    if AnzahlNodes < 3:
        AnzahlNodes = 3
        print("Unzulässige Eingabe. Die Eingabe wurde korrigiert.")
    if AnzahlNodes > AnzahlEdges:   #Ein Eulerscher Graph muss eine Mindestanzahl an Kanten haben
        AnzahlEdges = AnzahlNodes
        print("Unzulässige Eingabe. Die Eingabe wurde korrigiert.")
    if AnzahlEdges > AnzahlNodes*(AnzahlNodes-1)/2: #Der Graph darf nich mehr Kanten als ein vollständiger Graph haben
        AnzahlEdges = AnzahlNodes*(AnzahlNodes-1)/2
        print("Unzulässige Eingabe. Die Eingabe wurde korrigiert.")
    Graph = dsa.graph()
    for i in range(0,AnzahlNodes):
        Graph.make_node(str(i))
    Graph.make_edge("0", "1")
    KnotenMitUngeradenGrad1 = 0
    KnotenMitUngeradenGrad2 = 1
    AnzahlEdgesImGraph = 1
    while AnzahlEdgesImGraph < AnzahlEdges-1:
        r = random.randint(0, AnzahlNodes-1)
        if r == KnotenMitUngeradenGrad1 or r == KnotenMitUngeradenGrad2:
            Graph.make_edge(KnotenMitUngeradenGrad1, r)
            KnotenMitUngeradenGrad1 = r
    Graph.make_edge(KnotenMitUngeradenGrad1, KnotenMitUngeradenGrad2)
    return Graph
        
def eulersch(graph):
    r=True
    for node in graph.nodes:
        if len(neighbours(graph,node))%2==1:
            r=False
    return r  

def hamiltonisch(graph,node="default",waynodes=[],lenght=0):
    """tries to find a Hamiltoncircle"""
    #setting the startnode
    if node=="default":
        node=list(graph.nodes)[0]
        waynodes=[node]
        #print("startknoten:",node)
    #print("hamiltonisch wird mit waynodes={} aufgerufen".format(waynodes))
    
    for node in dsa.neighbors(graph,node):
        if node not in waynodes:
            #print("getesteter Knoten:",node,", nachbarknoten:",dsa.neighbors(graph,node),", waynodes:",waynodes)
            waynodes.append(node)
            if len(waynodes)==len(graph.nodes):
                if graph.get_edge(waynodes[-1],waynodes[0]):
                    print("hamiltonweg:",waynodes)
                    return True
            if len(waynodes)<len(graph.nodes):
                if hamiltonisch(graph,node,waynodes,lenght):
                    return True
                else:
                    waynodes.remove(node)
            else:
                break
    #print("forschleife ist durch")
    return False
            
def TesteEinPaarGraphen1(Anzahl):
    for i in range(0, Anzahl):
        H = HamiltonscherGraph(random.randint(25,100),random.randint(10,20))
        L = Liniengraph(H)
        if eulersch(L):
            print("Eulersch!!!")
            #print(L)
        else:
            print(H)
            print("Nicht Eulersch!!!")
            print(L)
            break

def TesteEinPaarGraphen2(Anzahl):
    for i in range(0, Anzahl):
        H = HamiltonscherGraph(random.randint(25,100),random.randint(10,20))
        L = Liniengraph(H)
        if hamiltonisch(L):
            print("Hamiltonsch!!!")
        else:
            print(H)
            print("Nicht Hamiltonsch!!!")
            print(L)
            break
        
def TesteEinPaarGraphen3(Anzahl):
    for i in range(0, Anzahl):
        H = EulerscherGraph(random.randint(25,100),random.randint(10,20))
        L = Liniengraph(H)
        if hamiltonisch(L):
            print("Hamiltonsch!!!")
        else:
            print(H)
            print("Nicht Hamiltonsch!!!")
            print(L)
            break
#print(Kreis(4))
#print(hamiltonisch(Kreis(20)))
#print(HamiltonscherGraph(10,6))
#print(Liniengraph(Kreis(4)))
TesteEinPaarGraphen1(200)
TesteEinPaarGraphen2(200)
TesteEinPaarGraphen3(200)
