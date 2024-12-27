import networkx as nx
import matplotlib.pyplot as plt
from utils.cascade_simulation import independent_cascade

def main():
    # Create a random graph
    G = nx.erdos_renyi_graph(n=300, p=0.01)  # 300 nodes, 1% connection probability
    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()