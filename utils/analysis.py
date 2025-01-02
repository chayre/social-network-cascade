import networkx.algorithms.community as nx_comm

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

    