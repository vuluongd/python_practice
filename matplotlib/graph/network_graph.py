import networkx as nx
import matplotlib.pyplot as plt 

G = nx.cycle_graph(10)
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_size=10, node_color = 'skyblue')
plt.title('Network Graph')
plt.show()