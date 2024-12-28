import networkx as nx
import matplotlib.pyplot as plt

def compute_positions(G):
    """
    Creates a list of node positions so that plots are spatially consistent.
    
    Parameters:
    - G: The graph.
    
    Returns:
    - pos: List of positions for plotting
    """    
    # Precompute positions using spring layout
    pos = nx.spring_layout(G, seed=7)  
    
    return pos

def plot_graph(G, pos, active_nodes=[], seed_nodes=[]):
    """
    Plots the graph with nodes color-coded based on their status.
    
    Parameters:
    - G: The graph representing the network, where nodes are individuals 
    - pos: Positions of nodes 
    - active_nodes: Set of nodes that are active
    - seed_nodes: List of initial seed nodes
    """
    colors = [
        'green' if node in seed_nodes else
        'red' if node in active_nodes else
        'blue'
        for node in G.nodes()
    ]
    nodelist = list(G.nodes())
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=300, nodelist=nodelist)
    plt.title("Graph Visualization with Active and Seed Nodes")
    plt.show()