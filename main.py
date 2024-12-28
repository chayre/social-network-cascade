import networkx as nx
import matplotlib.pyplot as plt
from utils.cascade_simulation import independent_cascade, find_influencers
from utils.plotting import plot_graph

def main():
    # Create a random graph with 50 nodes and a 5% probability of connection
    G = nx.erdos_renyi_graph(n=50, p=0.05)
    # Remove nodes with no neighbors (degree = 0)
    solitary_nodes = [node for node, degree in dict(G.degree()).items() if degree == 0]
    G.remove_nodes_from(solitary_nodes)
    # Precompute positions using spring layout
    pos = nx.spring_layout(G, seed=42)  # Seed ensures the same result every time

    # Plotting
    nx.draw(G, pos, with_labels=True)
    plt.title("Random Graph")
    plt.show()

    plot_graph(G, pos)


    # Find the top 5 influencers
    seed_nodes = find_influencers(G, k=5, activation_prob=0.15)

    # Simulate the spread starting from the seed nodes (top 5 influencers)
    active_nodes = independent_cascade(G, seed_nodes, activation_prob=0.50)

    # Visualize the results
    plot_graph(G, pos, active_nodes, seed_nodes)

    # Print results
    print(f"Seed Nodes: {seed_nodes}")
    print(f"Total Active Nodes: {len(active_nodes)}")


if __name__ == "__main__":
    main()