import networkx as nx
import matplotlib.pyplot as plt
import random

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
            for neighbor in G.neighbors(node):  # Check their neighbors
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


def main():
    # Create a random graph
    G = nx.erdos_renyi_graph(n=300, p=0.01)  # 300 nodes, 1% connection probability
    nx.draw(G, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()