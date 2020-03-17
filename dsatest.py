
import dsa
g=dsa.Graph()
a=g.make_node("a")
b=g.make_node("b")
e=g.make_edge("a","b")

h=dsa.Graph()
nodelist=[]
edgelist=[]
for i in range(5):
    nodelist.append(h.make_node("n{}".format(i)))
    counter=0
    for n in nodelist:
        if counter!=i:
            edgelist.append(h.make_edge("n{}".format(i),n))
        counter+=1
   

if __name__=="__main__":
    print(g)
    print(h)            
    print(neighbours(h,"n0"))
