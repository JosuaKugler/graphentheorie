
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:18:01 2018

@author: DELL
"""

import dsa
import shelve

gs=shelve.open("dsa_A9_graphs",writeback=True)
if "0" not in gs:
    g=dsa.Graph()
    g.make_node("G_0;1;1")
    #g.make_node("G_1;2;1")
    gs["0"]=g
gs.close()

def save(graph, c):
    """save "graph" g_c with index "c" to "dsa_A9_graphs" """
    gs=shelve.open("dsa_A9_graphs")
    if str(c) in gs.keys():
        g_c=gs[str(c)]
        if len(g_c.nodes)>len(graph.nodes):
            gs[str(c)]=graph
    else:
        gs[str(c)]=graph
    gs.close()


def get_graph(c):
    """if there is a g_c in "dsa_A9_graphs", return g_c,
    else return create_graph(c)"""
    
    gs=shelve.open("dsa_A9_graphs")
    if str(c) in gs.keys():
        return gs[str(c)]
    else:
        return create_graph(c)
    gs.close()
 

def create_graph(c):
    """create a G_c, i.e. a graph without proper c-coloring"""
    gs=shelve.open("dsa_A9_graphs")
    #test, whether there is already a G_c
    if str(c) in gs.keys():
        print("graph is already in shelve")
        return gs[str(c)]
    #get all required graphs g_n with n<c and save them to graphs
    else:
        graphs=[]
        for i in range(0,c):
            graphs.append(get_graph(i))
        g_c=connect(graphs)
        save(g_c, c)
        return g_c
    gs.close()

def fak(x):
    """returns x!"""
    result=1
    for i in range(1,x+1):
        result*=i
    return result

def connect(graphs):
    """connect all graphs in the list "graphs" as described by Vincent
    and add the new nodes"""
    print("connect wird mit folgender Liste aufgerufen:",graphs)
    c = len(graphs)
    G_c = dsa.Graph() #create a new graph
    # Calculates the number of new nodes
    cFaculty = fak(c)
    for i in range(1,cFaculty+1): # Creates the new nodes
        colour=cFaculty*fak(i)
        G_c.make_node( "G_" + str(c) + ";" + str(c +1 ) + ";" + str(i)) # "G_C;number of the colour; number of the node;"
   
    #copy nodes and edges from "graphs" in "G_c"  
    for graph in graphs:        
        for node_name in graph.nodes:           
            new_name = "G_" + str(c) + node_name # Writes G_c in front of the name           
            G_c.make_node(new_name) # Makes the new node
            # Writes all edges from graph to g_c
            neighbours1 = neighbours(graph, node_name) # Creates a list of neighbours in the graph
            for neighbour_node in neighbours1:   # If there is not already an edge in G_c a new edge is created
                    neighbours_new_name = "G_" + str(c) + str(node_name) # Writs G_c in front of the name
                    if not graph.is_edge( new_name, neighbours_new_name ):
                        if new_name!=neighbours_new_name:
                            graph.make_edge( new_name, neighbours_new_name )

            # makes edges beween the node and the new nodes
            c_node = get_c(node_name)
            #colour_node ?? = get_colour(node_name) # Adds new edges to a difficult to explain principle
            colour = get_colour(node_name)
            colour = colour - 1

            c_node_Faculty = fak(c_node)
            
            length_of_a_part = cFaculty / c_node_Faculty
            i = 1

            while i < cFaculty + 1:
                if c_node!=0:
                    if (i/length_of_a_part) % c_node == colour:
                        G_c.make_edge(new_name, "G_" + str(c) + ";" + str(c +1 ) + ";" + str(i))
                
                        #G_c.make_edge(new_name, "G_" + str(c) + ";" + str(c +1 ) + ";" + str(i))
                i+=1
    
    return G_c

                
def get_c(node_name):
    """returns the c of the graph of this node"""
    for i in range(2,len(node_name)): # The mname starts with "G_" and than there is the c
        if node_name[i] == 'G' or node_name[i] == ';': # the first character after the c is G or ;
            return int(node_name[2:i])
            break


def get_colour(node_name):
    """returns the colour of a node"""
    first_semicolon = 0
    second_semicolon = 0
    for i in range(1,len(node_name)): # The colour ist between the first and the second semicolon
        if node_name[i] == ';' and first_semicolon == 0:
            first_semicolon = i
        else:
            second_semicolon = i
    return int(node_name[first_semicolon+1:second_semicolon-1])


def neighbours(graph, node):
    """returns the neighbours of "node" in the graph "graph" """
    ret = []
    for other_node in graph.nodes:
        if graph.get_edge(node, other_node):
            ret.append(other_node)
    return ret

if __name__=="__main__":
    while True:
        try:
            c=int(input("c: "))
            break
        except ValueError:
            print("please enter an integer")
    print(create_graph(c))

