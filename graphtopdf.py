# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:51:51 2018

@author: DELL
"""
import os
def plotgraph(graph,name="graph1",diameter=10,quelltextpfad="beispiel",quelltext=False,newfolder=True,newfoldername="pythongraphs"):
    """erstellt eine pdf, in der der graph abgespeichert wird
    und speichert sie im default-Fall im Ordner pythongraphs im gleichen directory wie das ausgeführte python script ab.
    Zudem kann der quelltext ausgegeben werden, wenn im funktionsaufruf quelltext=True eingegeben wird."""
    
    if newfolder:
        if not newfoldername in os.getcwd():
            if not os.path.exists(newfoldername):
                os.mkdir(newfoldername)
            os.chdir(newfoldername)
    radius=diameter/2
    angle=360/len(graph.nodes)
    textextlist1=[u"\\documentclass[tikz]{standalone}",
                  u"\\usepackage{tikz}",
                  u"\\begin{document}"]
    textextlist3=[u"\\end{document}"]
    textextlist2=[]
    i=0
    textextlist2.append(u"\\begin{tikzpicture}")
    #textextlist2.append(u"\\node[circle,draw,red,line width=6pt](zentrum) at (0,0){};")
    for node in graph.nodes:
        #string="\\node[circle,draw]({}) at ({}:{})".format(node,angle*i,radius)+"{"+str(node)+"};"
        string="\\coordinate({}) at ({}:{})".format(node,angle*i+30,radius)+"{};"
        i+=1
        textextlist2.append(string)
    for edge in graph.edges:
        string="\\draw[line width=0.0001pt] ({})--({});".format(graph.edge_to_vertices(edge)[0],graph.edge_to_vertices(edge)[1])
        textextlist2.append(string)
    textextlist2.append(u"\\end{tikzpicture}")
    
    textextlist=textextlist1+textextlist2+textextlist3
    #dateiname=tex_dateien_pfad+datei
    dateiname=name+".tex"
    f=open(dateiname,"w")
    for line in textextlist:
        f.write(line+"\n")
    f.close()
    os.system("pdflatex {}".format(dateiname))
    os.startfile("{}.pdf".format(name))
    print(len(textextlist))
    if quelltext:
        name2=name+"_quelltext"+".txt"
        if quelltextpfad=="beispiel":
            dateiname=name2
        else:
            dateiname=os.path.join(quelltextpfad,name2)
        f=open(dateiname,"w")
        textextlist2.append("%!!!WICHTIG: Im Dokumentenheader '\\usepackage{tikz}' einfügen!!!")
        for line in textextlist2:
            f.write(line+"\n")
        f.close()
        #print("{}.aux".format(name))
        os.remove("{}.aux".format(name))
        os.remove("{}.log".format(name))
        os.remove("{}.tex".format(name))
        print("quelltext wurde als Textdatei in {} abgespeichert".format(dateiname))
        

def n_eck(n,radius):
    textextlist=[u"\\documentclass[tikz]{standalone}",
                  u"\\usepackage{tikz}",
                  u"\\begin{document}",
                  u"\\begin{tikzpicture}"]
    textextlist2=[u"\\end{tikzpicture}",u"\\end{document}"]
    for i in range(n):
        textextlist.append(u"\\coordinate (n{}) at ({}:{})".format(i,360/n*(i),radius)+"{};")
    #textextlist.append(u"\\node[circle,draw,red] (middle) at (0,0){};")
    lastnode=n-1
    for i in range(n):
        textextlist.append(u"\\draw (n{})--(n{});".format(lastnode,i))
        lastnode=i
    for i in textextlist2:
        textextlist.append(i)
    with open("neck.tex","w") as f:
        for line in textextlist:
            print(line)
            f.write(line+"\n")
    os.system("pdflatex neck")
    os.startfile("neck.pdf")
    os.remove("neck.aux")
    os.remove("neck.log")
    os.remove("neck.tex")















   
if __name__=="__main__":
    import dsa
    def fullyconnect(n):
        graph=dsa.Graph()
        for i in range(n):
            graph.make_node("n{}".format(i+1))
        for node in graph.nodes:
            for node1 in graph.nodes:
                if str(node)!=str(node1):
                    if not graph.get_edge(node,node1):
                        graph.make_edge(node,node1)
        return graph
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
    #bsp_g=fullyconnect(50)
    g=fullyconnect(17)
    lg=Liniengraph(g)
    plotgraph(lg,"graph2",diameter=20,quelltext=True)
    #n_eck(13,10)