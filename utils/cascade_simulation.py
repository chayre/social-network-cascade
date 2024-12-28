import random
import networkx as nx

def create_graph(n=50, p=0.05):
    """
    Creates a graph of n nodes with p probability they will be connected. Don't include any solitary nodes (ones with no connections/neighbors).
    
    Parameters:
    - n: Total number of nodes in the graph
    - p: Probability of connection
    
    Returns:
    - G: A created graph
    """    
    G = nx.erdos_renyi_graph(n=50, p=0.05)

    # Remove nodes with no neighbors (degree = 0)
    solitary_nodes = [node for node, degree in dict(G.degree()).items() if degree == 0]
    G.remove_nodes_from(solitary_nodes)

    return G

def independent_cascade(G, seed_nodes, activation_prob=0.1):
    """
    Simulates influence spread in a network using the Independent Cascade Model.
    
    Parameters:
    - G: The graph
    - seed_nodes: List of initial active (seed) nodes
    - activation_prob: Probability of activating a neighbor
    
    Returns:
    - active: Set of all nodes that became active during the simulation
    """
    active = set(seed_nodes)  # Keep track of all active nodes
    new_active = set(seed_nodes)  # Nodes activated in the current iteration

    # Continue simulation until no new nodes are activated
    while new_active:
        current_active = set()  # Nodes activated in this iteration
        for node in new_active:  # Check all newly active nodes
            for neighbor in G.neighbors(node):
                # Activate the neighbor with probability `activation_prob`
                if neighbor not in active and random.random() < activation_prob:
                    current_active.add(neighbor)
        active.update(current_active)  # Update the active nodes
        new_active = current_active  # Move to the next iteration

    return active  # Return all active nodes

def find_influencers(G, k, activation_prob=0.1):
    """
    Finds the top `k` influencers using a greedy algorithm.
    
    Parameters:
    - G: The graph
    - k: Number of influencers to find
    - activation_prob: Probability of activation in the Independent Cascade Model
    
    Returns:
    - influencers: List of the top `k` influencers
    """
    influencers = [] 
    for _ in range(k):
        best_node = None
        best_spread = 0
        for node in set(G.nodes()) - set(influencers):  # Nodes not yet selected
            # Simulate the spread with this node added
            spread = len(independent_cascade(G, influencers + [node], activation_prob))
            # Select the node with the largest spread
            if spread > best_spread:
                best_node = node
                best_spread = spread
        influencers.append(best_node)  # Add the best node to the influencers
    return influencers
