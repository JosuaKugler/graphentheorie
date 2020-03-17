# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 17:09:00 2018

@author: DELL
"""
import dsa
import copy

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















def neighbours(graph,list1):
    list2=[]
    for node in list1:
        neighborlist=dsa.neighbors(graph,node)
        for node1 in neighborlist:
            if node1 not in list2:
                list2.append(node1)
    return list2



def mk_testgraphs():
    """erstellt zwei Testgraphen und vergleicht sie"""
    g1=dsa.Graph()
    g2=dsa.Graph()
    g1.make_node("n1")
    g1.make_node("n2")
    g1.make_node("n3")
    g1.make_node("n4")
    g1.make_node("n5")
    g1.make_node("n6")
    g1.make_node("n7")
    g1.make_edge("n1","n2")
    g1.make_edge("n2","n3")
    g1.make_edge("n3","n4")
    g1.make_edge("n1","n4")
    g1.make_edge("n6","n5")
    g1.make_edge("n5","n7")
    g1.make_edge("n6","n7")
    g1.make_edge("n1","n7")
    g2.make_node("n1")
    g2.make_node("n2")
    g2.make_node("n3")
    g2.make_node("n4")
    g2.make_node("n5")
    g2.make_node("n6")
    g2.make_node("n7")
    g2.make_edge("n1","n2")
    g2.make_edge("n2","n3")
    g2.make_edge("n3","n4")
    g2.make_edge("n1","n4")
    g2.make_edge("n6","n5")
    g2.make_edge("n5","n7")
    g2.make_edge("n6","n7")
    g2.make_edge("n6","n1")
    return compare(g1,g2) 

def searchpath(graph,startnode,lenght,endnode,kreisliste=None):
    print("Aufruf startnode={}, lenght={}, kreisliste={}".format(startnode,lenght,kreisliste))
    if lenght<0:
        #print("Es gibt keine negativen Wege")
        return "Es gibt keine negativen Wege"
    if kreisliste is None:
        kreisliste=[startnode]
    newkreisliste=copy.deepcopy(kreisliste)
    if lenght==0:
        print("lenght is 0")
        return [False,kreisliste]
    
    elif lenght==1:
        print(kreisliste)
        for nnode in dsa.neighbors(graph,startnode):
            print(kreisliste)
            print("lenght is 1")
            print(nnode)
            if nnode==endnode:
                return [True,kreisliste]
        return [False,kreisliste]   
    path=False
    for nnode in dsa.neighbors(graph,startnode):
        newkreisliste.append(nnode)
        print("Ist {} in {}?".format(nnode,kreisliste))
        if nnode not in kreisliste:
            a=searchpath(graph,nnode,lenght-1,endnode,newkreisliste)
            if a[0]:
                kreisliste=a[1]
                print("pfad gefunden")
                path=True
                break
            else:
                print("kein pfad gefunden")
        newkreisliste.remove(nnode)
        kreisliste=copy.deepcopy(newkreisliste)
    return [path,kreisliste]
                    
                    
def Zshgkmpt(graph,Zshglist=None):
    """returns a list [graph,zshgkmpt1,...,zshgkmptn]"""
    #print("graph:\n",graph)
    if Zshglist is None:
        Zshglist=[]
    graph1=copy.deepcopy(graph)
    startnode=list(graph1.nodes)[0]
    neighborlist=dsa.neighbors(graph1,startnode)
    neighborlist.append(startnode)
    a=True
    while a:
        neighborlist2=neighborlist
        for node in neighborlist2:
            nlist=dsa.neighbors(graph1,node)
            for node1 in nlist:
                if node1 not in neighborlist2:
                    neighborlist2.append(node1)
        if len(neighborlist2)==len(neighborlist):
            a=False
        neighborlist=neighborlist2

    if len(neighborlist)==len(graph1.nodes):
        if neighborlist not in Zshglist:
            Zshglist.append(neighborlist)
            return Zshglist
    else:
        Zshglist.append(neighborlist)
        for node in neighborlist:
            graph1.remove_node(node)
        
        return Zshgkmpt(graph1,Zshglist)

def nlist2graph(nlist,graph):
    """nlist ist eine Liste aus Knoten, die auch in graph vorkommen.
    Die Funktion erstellt nun alle Kanten, die es in graph gibt 
    und die zwischen den Knoten in nlist existieren"""
    TG=dsa.Graph()
    for node1 in nlist:
        TG.make_node(node1)
    for node1 in TG.nodes:
        for node2 in TG.nodes:
            if str(node1)!=str(node2):
                if graph.get_edge(node1,node2):
                    if not TG.get_edge(node1,node2):
                        TG.make_edge(node1,node2)
    return TG              
            
    
def grad(graph,node):
    return len(dsa.neighbors(graph,node))

def mk_graddict(graph1):
    graddict1={}
    for node in graph1.nodes:
        if grad(graph1,node) not in graddict1.keys():
            graddict1[grad(graph1,node)]=[node]
        else:
            graddict1[grad(graph1,node)].append(node)
    return graddict1


def Hierarchie(graph,nodelist,hierarchiedict,ebene,hnodes,counter=0):
    #print("Hierarchie wird mit folgenden Parametern aufgerufen: hierarchiedict: {}, ebene: {}, hnodes: {}".format(hierarchiedict,ebene,hnodes))
    counter+=1
    if counter>100:
        return "funktioniert nicht"
    ebene+=1
    glist=[]
    nodelistout=[]
    for node in nodelist:
        for node1 in dsa.neighbors(graph,node):
            if node1 not in  hnodes:
                nodelistout.append(node1)
                glist.append(grad(graph,node1))
                hnodes.append(node1)
    hierarchiedict[ebene]=glist
    if len(graph.nodes)==len(hnodes):
        return hierarchiedict
    else:
        return Hierarchie(graph,nodelistout,hierarchiedict,ebene,hnodes,counter)
        
def mk_hierarchiedict(graph,node=None):
    if node is None:
        node=list(graph.nodes)[0]
    hierarchiedict0={0:grad(graph,node)}
    return Hierarchie(graph,[node],hierarchiedict0,0,[node])

def compare(graph1,graph2):
    if len(graph1.nodes)!=len(graph2.nodes):
        print("Unterschiedliche Anzahl an Knoten")
        return False
    elif len(graph1.nodes)<2:
        return True
    if len(graph1.edges)!=len(graph2.edges):
        print("Unterschiedliche Anzahl an Kanten")
        return False
    elif len(graph1.nodes)<=3:
        return True
    
    graddict1=mk_graddict(graph1)
    graddict2=mk_graddict(graph2)
    if len(graddict1)!=len(graddict2):
        print("Grade sind unterschiedlich 1")
        return False
    if len(graddict1)==1:
        eg=True
        if eg:
            vergleiche(graph1,graph2,list(graph1.nodes)[0])
    lendict1={}
    for grad1 in graddict1:
        if len(graddict1[grad1])!=len(graddict2[grad1]):
            print("Grade sind unterschiedlich 2")
            return False
        lendict1[len(graddict1[grad1])]=grad1
    shortest1=min(lendict1.keys())
    shortestgrad1=lendict1[shortest1]
    shortestgradlist1=graddict1[shortestgrad1]
    lendict2={}
    for grad2 in graddict2:
        lendict2[len(graddict2[grad2])]=grad2
    shortest2=min(lendict2.keys())
    shortestgrad2=lendict2[shortest2]
    shortestgradlist2=graddict2[shortestgrad2]
    if len(shortestgradlist1)!=len(shortestgradlist2):
        return False
    #an dieser Stelle schmeißt er gleiche Zusammenhangskomponenten raus
    Zshgkmpt1=Zshgkmpt(graph1)
    #print("Zshgkmpt1",Zshgkmpt1)
    Zshgkmpt2=Zshgkmpt(graph2)
    #print("Zshgkmpt2",Zshgkmpt2)
    if len(Zshgkmpt1)!=len(Zshgkmpt2):
        return False
    if len(Zshgkmpt1)>1:
        zeq1=[]
        zeq2=[]
        for kmpt1 in Zshgkmpt1:
            gkmpt1=nlist2graph(kmpt1,graph1)
            for kmpt2 in Zshgkmpt2:
                gkmpt2=nlist2graph(kmpt2,graph2)
                if gkmpt2 not in zeq2:
                    #print("{} und {} werden verglichen".format(gkmpt1,gkmpt2))
                    if compare(gkmpt1,gkmpt2):
                        #print("{} und {} sind gleich".format(gkmpt1,gkmpt2))
                        zeq1.append(gkmpt1)
                        zeq2.append(gkmpt2)
                        break
        if len(Zshgkmpt1)!=len(zeq1):
            print("ungleiche Zusammenhangskomponenten")
            return False
        else:
            return True
    #Hier kommt das backtracking:
    hierarchiedict1=mk_hierarchiedict(graph1)
    probablyequal=False
    for node2 in graph2.nodes:
        hierarchiedict2=mk_hierarchiedict(graph2,node2)
        if hierarchiedict2==hierarchiedict1:
            probablyequal=True
            break
    if not probablyequal:
        print("Es gibt keinen Knoten in graph2, der dem ersten Knoten in graph1 vom Hierarchiedict her gleicht")
        return False
    return True
print(mk_testgraphs())