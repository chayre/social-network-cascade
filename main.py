from utils.cascade_simulation import create_graph, independent_cascade, find_influencers
from utils.plotting import plot_graph, compute_positions

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
    active_nodes = independent_cascade(G, seed_nodes, activation_prob=0.40)

    # Print results
    print(f"Seed Nodes: {seed_nodes}")
    print(f"Total Active Nodes: {len(active_nodes)}")

    # Plot results of independent cascade
    plot_graph(G, pos, active_nodes, seed_nodes)

if __name__ == "__main__":
    main()