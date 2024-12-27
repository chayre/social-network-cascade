import networkx as nx
import matplotlib.pyplot as plt

def main():
    # Create a random graph
    G = nx.erdos_renyi_graph(n=10, p=0.15)  # 100 nodes, 5% connection probability
    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()