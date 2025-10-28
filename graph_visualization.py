import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

def visualize_use_graph(G, analysis_results, layout='spring', max_nodes=50):
    """
    Visualizes the directed graph with enhanced styling for educational purposes.
    """
    # Create a subgraph if too large for clear visualization
    if G.number_of_nodes() > max_nodes:
        # Keep top nodes by weighted degree
        weighted_degree = analysis_results['weighted_degree']
        top_nodes = sorted(weighted_degree.items(), key=lambda x: x[1], reverse=True)[:max_nodes]
        top_node_names = [node for node, _ in top_nodes]
        G = G.subgraph(top_node_names)
        print(f"📉 Using subgraph with top {max_nodes} sectors for clarity")
    
    plt.figure(figsize=(16, 12))
    
    # Choose layout
    if layout == 'circular':
        pos = nx.circular_layout(G)
    elif layout == 'spring':
        pos = nx.spring_layout(G, weight='weight', k=2, iterations=50)
    else:
        pos = nx.random_layout(G)
    
    # Prepare edge data
    edges = G.edges(data=True)
    weights = [data['weight'] for _, _, data in edges]
    
    # Normalize weights for visualization
    if weights:
        max_weight = max(weights)
        min_weight = min(weights)
        normalized_weights = [(w - min_weight) / (max_weight - min_weight) * 5 + 0.5 for w in weights]
    else:
        normalized_weights = [1] * len(edges)
    
    # Node sizes based on weighted degree
    node_sizes = [analysis_results['weighted_degree'].get(node, 1) for node in G.nodes()]
    max_size = max(node_sizes) if node_sizes else 1
    node_sizes = [300 + (size / max_size) * 2000 for size in node_sizes]
    
    # Node colors based on betweenness centrality
    node_colors = [analysis_results['betweenness'].get(node, 0) for node in G.nodes()]
    
    # Draw the graph
    nodes = nx.draw_networkx_nodes(G, pos, 
                                 node_size=node_sizes,
                                 node_color=node_colors,
                                 cmap=plt.cm.viridis,
                                 alpha=0.8)
    
    # Draw edges with varying widths and colors
    edges = nx.draw_networkx_edges(G, pos,
                                 edge_color=weights,
                                 edge_cmap=plt.cm.Blues,
                                 width=normalized_weights,
                                 alpha=0.6,
                                 arrowstyle='->',
                                 arrowsize=15,
                                 connectionstyle="arc3,rad=0.1")
    
    # Draw labels
    labels = {node: node[:20] + '...' if len(node) > 20 else node for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=8, font_weight='bold')
    
    # Add colorbars
    plt.colorbar(nodes, label='Betweenness Centrality', shrink=0.75)
    if edges:
        plt.colorbar(edges, label='Economic Flow (million USD)', shrink=0.75)
    
    plt.title("USEEIO v2.0 - Economic Interconnections Between Industries\n"
             "Node size = Total economic flow, Color = Bridge importance", 
             fontsize=14, pad=20)
    
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def plot_economic_metrics(analysis_results):
    """
    Creates additional plots for economic metrics.
    """
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))
    
    # Plot 1: Top sectors by total economic flow
    weighted_degree = analysis_results['weighted_degree']
    top_sectors = sorted(weighted_degree.items(), key=lambda x: x[1], reverse=True)[:10]
    sectors, flows = zip(*top_sectors)
    ax1.barh([s[:25] + '...' if len(s) > 25 else s for s in sectors], flows, color='skyblue')
    ax1.set_xlabel('Total Economic Flow (million USD)')
    ax1.set_title('Top 10 Sectors by Economic Flow')
    ax1.grid(axis='x', alpha=0.3)
    
    # Plot 2: Degree distribution
    degrees = [d for d in analysis_results['degree_centrality'].values()]
    ax2.hist(degrees, bins=20, alpha=0.7, color='lightgreen')
    ax2.set_xlabel('Degree Centrality')
    ax2.set_ylabel('Frequency')
    ax2.set_title('Degree Centrality Distribution')
    ax2.grid(alpha=0.3)
    
    # Plot 3: Betweenness centrality
    betweenness = analysis_results['betweenness']
    top_betweenness = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:10]
    sectors, betw = zip(*top_betweenness)
    ax3.barh([s[:25] + '...' if len(s) > 25 else s for s in sectors], betw, color='salmon')
    ax3.set_xlabel('Betweenness Centrality')
    ax3.set_title('Top 10 Bridge Sectors')
    ax3.grid(axis='x', alpha=0.3)
    
    # Plot 4: In-degree vs Out-degree scatter
    in_deg = list(analysis_results['in_degrees'].values())
    out_deg = list(analysis_results['out_degrees'].values())
    ax4.scatter(in_deg, out_deg, alpha=0.6, color='purple')
    ax4.set_xlabel('In-Degree (Imports)')
    ax4.set_ylabel('Out-Degree (Exports)')
    ax4.set_title('Import vs Export Economic Flows')
    ax4.grid(alpha=0.3)
    
    # Add identity line
    max_val = max(max(in_deg), max(out_deg))
    ax4.plot([0, max_val], [0, max_val], 'r--', alpha=0.5, label='x=y')
    ax4.legend()
    
    plt.tight_layout()
    plt.show()


    """sdaad"""