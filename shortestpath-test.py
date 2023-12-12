import matplotlib.pyplot as plt
import networkx as nx
G = nx.karate_club_graph()
pos = nx.spring_layout(G)
nx.draw(G,pos,node_color='k')
# draw path in red
path = nx.shortest_path(G,source=14,target=16)
path_edges = list(zip(path,path[1:]))
nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=10)
plt.axis('equal')
plt.show()
plt.savefig("path.png")
