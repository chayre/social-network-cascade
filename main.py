from utils.cascade_simulation import create_graph, independent_cascade, find_influencers
from utils.linear_threshold_simulation import linear_threshold_model
from utils.plotting import plot_graph, compute_positions
import random

def main():
    # Create starting graph
    G = create_graph(n=50, p=0.05)

    # Precompute positions using spring layout
    pos = compute_positions(G)

    # Plotting original Graph
    plot_graph(G, pos)

    # Find the top 5 influencers
    seed_nodes = find_influencers(G, k=5, activation_prob=0.10)

    # Simulate the spread starting from the seed nodes (top 5 influencers)
    cascade_active_nodes = independent_cascade(G, seed_nodes, activation_prob=0.40)

    # Print results
    print(f"Seed Nodes: {seed_nodes}")
    print(f"Total Active Nodes: {len(cascade_active_nodes)}")

    # Plot results of independent cascade
    plot_graph(G, pos, cascade_active_nodes, seed_nodes)

    # Add weights to the edges for influence strength
    for u, v in G.edges():
        G[u][v]['weight'] = random.uniform(0.3, 0.5)

    # Plot results of linear threshold model
    linear_active_nodes = linear_threshold_model(G, seed_nodes)
    plot_graph(G, pos, linear_active_nodes, seed_nodes)

if __name__ == "__main__":
    main()
