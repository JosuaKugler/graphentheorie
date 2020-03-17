# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 13:50:13 2018

@author: DELL
"""
import dsa

def eulersch(graph):
    r=True
    for node in graph.nodes:
        if len(dsa.neighbors(graph,node))%2==1 or len(dsa.neighbors(graph,node))==0:
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
    print("forschleife ist durch")
    return False

g=dsa.Graph()
g.make_node("n1")
g.make_node("n2")
g.make_node("n3")
g.make_node("n4")
g.make_edge("n1","n2")
#g.make_edge("n1","n3")
g.make_edge("n2","n3")
g.make_edge("n3","n4")
#g.make_edge("n2","n4")
g.make_edge("n4","n1")
hamiltonisch(g)