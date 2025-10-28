import networkx as nx
import pandas as pd

def build_use_graph(df, sector_names=None, threshold=0.1):
    """
    Builds a directed weighted graph from the 'U' matrix.
    
    Parameters:
    - df: DataFrame containing the U matrix
    - sector_names: List of meaningful sector names
    - threshold: Minimum weight to include edge (filters noise)
    """
    G = nx.DiGraph()
    
    num_sectors = min(len(df.columns), len(df.index))
    
    # Use meaningful names if available, otherwise generic
    if sector_names and len(sector_names) >= num_sectors:
        node_names = sector_names[:num_sectors]
    else:
        node_names = [f"Sector_{i}" for i in range(num_sectors)]
    
    # Add nodes with sector information
    for i, name in enumerate(node_names):
        G.add_node(name, id=i, total_output=df.iloc[i,:].sum(), total_input=df.iloc[:,i].sum())
    
    # Add edges with weights (economic flows)
    total_edges = 0
    max_weight = df.values.max()
    
    for i in range(num_sectors):
        for j in range(num_sectors):
            weight = df.iloc[i, j]
            # Only add significant economic relationships
            if weight > threshold:
                G.add_edge(node_names[j], node_names[i], weight=weight, 
                          normalized_weight=weight/max_weight)
                total_edges += 1
    
    print(f"✅ Graph built with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
    print(f"📊 Edge weight threshold: {threshold}")
    print(f"💰 Maximum transaction: {max_weight:.2f} million USD")
    
    return G, node_names