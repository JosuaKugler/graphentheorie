# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 22:08:35 2018

@author: DELL
"""

import dsa
import graphtopdf
import random

def Liniengraph(graph):
    Liniengraph = dsa.Graph()
    for edge in graph.edges:
        Liniengraph.make_node(str(graph.edge_to_vertices(edge)[0])+str(graph.edge_to_vertices(edge)[1]))
    for edge in graph.edges:
        Nodes = [str(graph.edge_to_vertices(edge)[0]),str(graph.edge_to_vertices(edge)[1])]
        for edge2 in graph.edges:
            if edge == edge2:
                continue
            Nodes2 = [str(graph.edge_to_vertices(edge2)[0]),str(graph.edge_to_vertices(edge2)[1])]
            #Auf Übereinstimmung prüfen
            if Nodes[0] == Nodes2[0] or Nodes[0] == Nodes2[1] or Nodes[1] == Nodes2[0] or Nodes[1] == Nodes2[1]:
                if not Liniengraph.get_edge(str(graph.edge_to_vertices(edge)[0])+str(graph.edge_to_vertices(edge)[1]), str(graph.edge_to_vertices(edge2)[0])+str(graph.edge_to_vertices(edge2)[1])):
                    Liniengraph.make_edge(str(graph.edge_to_vertices(edge)[0])+str(graph.edge_to_vertices(edge)[1]), str(graph.edge_to_vertices(edge2)[0])+str(graph.edge_to_vertices(edge2)[1]))
    return Liniengraph 


def neighbours(graph, node):
    """returns the neighbours of "node" in the graph "graph" """
    ret = []
    for other_node in graph.nodes:
        if graph.get_edge(node, other_node):
            ret.append(other_node)
    return ret

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
    while AnzahlEdgesImGraph < AnzahlEdges: # Zufällig wietere Kanten einfügen bis die gewünschte Zahl erreicht wurde.
        Node1 = random.randint(0, AnzahlNodes-1)
        Node2 = random.randint(0, AnzahlNodes-1)
        if (not Node1 == Node2) and not Graph.get_edge(str(Node1),str(Node2)):
            Graph.make_edge(str(Node1),str(Node2))
            AnzahlEdgesImGraph = AnzahlEdgesImGraph + 1
    return Graph

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

graph=dsa.Graph()
graph.make_node("a")
graph.make_node("b")
graph.make_node("c")
graph.make_node("d")
graph.make_edge("a","b")
graph.make_edge("b","c")
graph.make_edge("c","d")
graph.make_edge("d","a")
graph.make_edge("a","c")

lg=Liniengraph(graph)

graphtopdf.plotgraph(lg,"5_graph",quelltext=True)