import dsa
import random
import shelve

#random.seed(0)

def neighbours(graph, node):
    """returns the neighbours of "node" in the graph "graph" """
    ret = []
    for other_node in graph.nodes:
        if graph.get_edge(node, other_node):
            ret.append(other_node)
    return ret

def is_triangle(graph):
    """returns True if there are three nodes 
    with edges to each other in "graph" """
    t=False
    for node in graph.nodes:
        neighborlist=neighbours(graph,node)
        for n2 in neighborlist:
            for n3 in neighborlist:
                if n3!=n2:
                    if graph.get_edge(n2,n3):
                        t=True
    return t


def colors(colordict,nodelist):
    """returns a list with the colors of the nodes in "nodelist"
    according to "colordict" """
    list2=[]
    for node in nodelist:
        list2.append(colordict[node])
    return list2

def colornode(graph,c,node,colordict):
    """changes "colordict" of "graph"
    as it tries to find a proper c-coloring, 
    starts the coloring at "node" """
    neighborlist=neighbours(graph,node)
    c_neighbors=colors(colordict, neighborlist)
    for color in range(1,c+1):
        proceed=True
        if color not in c_neighbors:
            colordict[node]=color
            break
        else:
            proceed=False
    
    if proceed:
        for nnode in neighborlist:
            if colordict[nnode]==0:
                colornode(graph,c,nnode,colordict)

def colorfunction(graph,c,colordict,nodelist,nodenumber=0):
    node=nodelist[nodenumber]
    neighborlist=neighbours(graph,node)
    c_neighbors=colors(colordict, neighborlist)
    for color in range(1,c+1):
        if color not in c_neighbors:
            colordict[node]=color
            liste=colorfunction(graph,c,colordict,nodelist,nodenumber=nodenumber+1)
            f=liste[0]
            if f:
                return [True,colordict]
                break
    return [False,colordict]



    
    
def faerbbar2(graph,c):
    """backtracking-algorithmus"""
    nodelist1=[]
    colordict={}
    for node in graph.nodes:
        nodelist1.append(node)
        nodelist=[node]
        colordict[node]=0
    while len(nodelist)<len(nodelist1):
        for node in nodelist:
            for node1 in neighbours(graph,node):
                if node1 not in nodelist:
                    nodelist.append(node1)
    colordict[nodelist[0]]=1
    result=colorfunction(graph,c,colordict,nodelist)
    return result
            
                
                
def faerbbar(graph,c):
    """returns True, if "graph" has a proper c-coloring"""
    colordict={}
    for node in graph.nodes:
        colordict[node]=0
        startnode=node
    colornode(graph, c, startnode, colordict)
    f=True
    for node in graph.nodes:
        if colordict[node]==0:
            f=False
    print("colordict",colordict)
    liste1=[f,colordict]
    return liste1


def addnode(graph,p_edges):
    """adds a node to the graph; 
    creates "p_edges" times the number of possible edges to the graph,
    without creating a triangle"""
    i=len(graph.nodes)
    node1=graph.make_node("n{}".format(i))
    nodedict=graph.nodes
    nodekeys=[]
    graph.make_edge(node1,nodedict["n{}".format(random.randint(1,i-1))])
    for key in graph.nodes.keys():
        nodekeys.append(key)
    random.shuffle(nodekeys)
    while len(nodekeys)>int(len(nodekeys)*p_edges)+1:
        nodekeys.remove(nodekeys[len(nodekeys)-1])
    for key in nodekeys:
        node=nodedict[key]
        if str(node) != str(node1):
            if not graph.get_edge(node,node1):
                graph.make_edge(node,node1)
                if is_triangle(graph):
                    graph.remove_edge(node,node1)

def change_node_name(node,c,colordict):
    """returns the changed name of "node" in G_"c" with "colordict" """
    nodenumber=node[1:]
    if colordict[node]==0:
        color=c+1
    else:
        color=colordict[node]
    new_name="G_{};{};{}".format(c,color,nodenumber)
    return new_name

def change_node_names(graph,c,colordict):
    """changes names of the nodes and edges in "graph" 
    so that they suit the "dsa_aufgabe9.py" code"""
    G_c=dsa.Graph()
    for node in graph.nodes:
        new_name=change_node_name(node,c,colordict)
        G_c.make_node(new_name)
    for edge in graph.edges:
        edgelist=graph.edge_to_vertices(edge)
        edgelist2=[]
        for node in edgelist:
            edgelist2.append(change_node_name(node,c,colordict))
        G_c.make_edge(edgelist2[0],edgelist2[1])
    return G_c

def save_graph(graph,c,colordict):
    """save "graph" g_c with index "c" to "dsa_A9_graphs" """
    graph=change_node_names(graph,c,colordict)
    gs=shelve.open("dsa_A9_graphs")
    if str(c) in gs.keys():
        g_c=gs[str(c)]
        if len(g_c.nodes)>len(graph.nodes):
            gs[str(c)]=graph
    else:
        gs[str(c)]=graph
    gs.close()
    
def mk_graph(c,safe=False):
    g=dsa.Graph()
    for i in range(5):
        g.make_node("n{}".format(i))
    for i in range(5):
        g.make_edge(g.nodes["n{}".format(i)],g.nodes["n{}".format((i+1)%5)])
    c_f=True
    nn=5
    while c_f:
        addnode(g,0.75)
        print("graph:",g)
        c_f=faerbbar(g,c)[0]
        print("Anzahl der knoten",nn)
        nn+=1
    sure=faerbbar2(g,c)[0]
    if safe:
        while not sure:
            addnode(g,0.75)
            print("graph",g)
            sure=faerbbar2(g,c)[0]
            print("anzahl der knoten",nn)
            nn+=1
        
    #colordict=faerbbar(g,c)[1]
    #save_graph(g,c,colordict)
    return g

def get_graph(c):
    """if there is a g_c in "dsa_A9_graphs", return g_c,
    else return create_graph(c)"""
    
    gs=shelve.open("dsa_A9_graphs")
    if str(c) in gs.keys() and c==0:
        return gs[str(c)]
    else:
        print("graph ist nicht im shelve")
        return mk_graph(c)
    gs.close()
    
if __name__=="__main__":
    while True:
        try:
            c=int(input("c: "))
            break
        except ValueError:
            print("please enter an integer")
    #c=4
    print(get_graph(c))
    print(is_triangle(get_graph(c)))