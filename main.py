from utils.cascade_simulation import create_graph, independent_cascade, find_influencers
from utils.linear_threshold_simulation import linear_threshold_model, apply_weights
from utils.plotting import plot_graph, compute_positions
from utils.analysis import detect_communities, centrality_analysis

def main():
    # Create starting graph
    G = create_graph(n=40, p=0.10)

    # Determine communities 
    comm = detect_communities(G)

    # Calculate centrality and plot
    centr = centrality_analysis(G)

    # Precompute positions using spring layout
    pos = compute_positions(G)

    # Plotting original Graph
    plot_graph(G, pos)

    # Find the top 5 influential nodes
    seed_nodes = find_influencers(G, k=5, activation_prob=0.05)

    # Simulate the spread starting from the seed nodes (top 5 influencers)
    cascade_active_nodes = independent_cascade(G, seed_nodes, activation_prob=0.40)

    # Print results
    print(f"Seed Nodes: {seed_nodes}")
    print(f"Total Active Nodes: {len(cascade_active_nodes)}")

    # Plot results of independent cascade
    plot_graph(G, pos, cascade_active_nodes, seed_nodes)

    # Add weights to the edges for influence strength
    G_weighted_edges = apply_weights(G, 0.2, 0.4)

    # Plot results of linear threshold model
    linear_active_nodes = linear_threshold_model(G, seed_nodes)
    plot_graph(G_weighted_edges, pos, linear_active_nodes, seed_nodes)

if __name__ == "__main__":
    main()
