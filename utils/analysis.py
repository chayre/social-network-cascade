import networkx.algorithms.community as nx_comm
import networkx as nx
import random

def detect_communities(G):
    """
    Detects communities in the graph using modularity-based clustering.
    
    Parameters:
    - G: The graph.
    
    Returns:
    - communities: List of sets, where each set represents a community.
    """
    communities = list(nx_comm.greedy_modularity_communities(G))
    return communities

def centrality_analysis(G):
    """
    Computes centrality measures for all nodes and visualizes the graph based on centrality.
    
    Parameters:
    - G: The graph.
    
    Returns:
    - centrality: Dictionary of centrality scores for nodes.
    """
    centrality = nx.degree_centrality(G)
    return centrality

def evolve_graph(G, steps=10, add_prob=0.2, remove_prob=0.9):
    """
    Simulates the evolution of a graph over time.
    
    Parameters:
    - G: The initial graph
    - steps: Number of evolution steps
    - add_prob: Probability of adding a new edge
    - remove_prob: Probability of removing an existing edge
    
    Returns:
    - G: The evolved graph
    """
    for _ in range(steps):
        if random.random() < add_prob:
            # Add a random edge
            nodes = list(G.nodes())
            u, v = random.sample(nodes, 2)
            if not G.has_edge(u, v):
                G.add_edge(u, v)
        
        if random.random() < remove_prob:
            # Remove a random edge
            if G.edges():
                edge = random.choice(list(G.edges()))
                G.remove_edge(*edge)
    return G
    
def adjust_weights(G, delta=0.1):
    """
    Adjusts weights of edges randomly within a range of -delta to +delta.
    
    Parameters:
    - G: The graph
    - delta: Value to increase or decrease the weight
    
    Returns:
    - G: The graph with adjusted weights
    """
    for u, v in G.edges():
        G[u][v]['weight'] = max(0, G[u][v].get('weight', 1) + random.uniform(-delta, delta))
    return G