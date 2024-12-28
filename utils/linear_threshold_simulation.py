import random

def linear_threshold_model(G, seed_nodes):
        """
        Simulates influence spread in a network using the Linear Threshold Model. In LTM, nodes become active based on the sum of influence from 
        active neighbors which exceeds a threshold level.
        
        Parameters:
        - G: The graph representing the network, where nodes are individuals and edges represent connections between them.
        - seed_nodes: List of initial active (seed) nodes

        Returns:
        active (set): A set of nodes that are activated after the influence spread has completed
    
        The process works as follows:
        - Each node is assigned a random threshold between 0 and 1.
        - Active nodes spread influence to their neighbors. Each edge has a weight that represents the strength of influence
        - A node activates when the cumulative influence from its active neighbors exceeds its threshold
        - The process repeats iteratively until no more nodes can be activated.
        """
        # Assign random thresholds to nodes
        thresholds = {node: random.uniform(0.3, 0.7) for node in G.nodes()}
        active = set(seed_nodes)
        new_active = set(seed_nodes)

        while new_active:
            current_active = set()
            for node in set(G.nodes()) - active:
                # Calculate the total influence from active neighbors
                influence = sum(G[neighbor][node].get('weight', 1) for neighbor in G.neighbors(node) if neighbor in active)
                if influence >= thresholds[node]:
                    current_active.add(node)
            active.update(current_active)
            new_active = current_active

        return active
