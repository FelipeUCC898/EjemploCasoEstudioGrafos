import networkx as nx
import pandas as pd

def analyze_use_graph(G):
    """
    Performs comprehensive analysis on the economic-use graph.
    """
    print("\n" + "="*60)
    print("📊 GRAPH ANALYSIS RESULTS")
    print("="*60)
    
    # Basic graph properties
    print(f"\n📈 Basic Graph Properties:")
    print(f"   • Nodes: {G.number_of_nodes()}")
    print(f"   • Edges: {G.number_of_edges()}")
    print(f"   • Density: {nx.density(G):.6f}")
    print(f"   • Is strongly connected: {nx.is_strongly_connected(G)}")
    print(f"   • Strongly connected components: {nx.number_strongly_connected_components(G)}")
    print(f"   • Weakly connected components: {nx.number_weakly_connected_components(G)}")
    
    # Degree centrality (number of connections)
    degree_centrality = nx.degree_centrality(G)
    print(f"\n🔗 Degree Centrality (Most Connected Sectors):")
    for node, value in sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"   • {node}: {value:.4f}")
    
    # Weighted degree (total economic flow)
    weighted_degree = dict(G.degree(weight='weight'))
    print(f"\n💰 Weighted Degree (Total Economic Flow):")
    for node, value in sorted(weighted_degree.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"   • {node}: {value:,.2f} million USD")
    
    # Betweenness centrality (bridge sectors)
    betweenness = nx.betweenness_centrality(G, weight='weight')
    print(f"\n🌉 Betweenness Centrality (Key Bridge Sectors):")
    for node, value in sorted(betweenness.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"   • {node}: {value:.4f}")
    
    # In-degree and Out-degree analysis
    in_degrees = dict(G.in_degree(weight='weight'))
    out_degrees = dict(G.out_degree(weight='weight'))
    
    print(f"\n📥 Top Importers (Highest In-Degree):")
    for node, value in sorted(in_degrees.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"   • {node}: {value:,.2f} million USD")
    
    print(f"\n📤 Top Exporters (Highest Out-Degree):")
    for node, value in sorted(out_degrees.items(), key=lambda x: x[1], reverse=True)[:3]:
        print(f"   • {node}: {value:,.2f} million USD")
    
    return {
        'degree_centrality': degree_centrality,
        'weighted_degree': weighted_degree,
        'betweenness': betweenness,
        'in_degrees': in_degrees,
        'out_degrees': out_degrees
    }

def find_important_paths(G, analysis_results, source_sector=None, target_sector=None):
    """
    Finds important economic pathways in the graph.
    """
    print(f"\n🛣️  Important Economic Pathways:")
    
    if not source_sector or not target_sector:
        # Use top sectors by betweenness as examples
        top_sectors = sorted(analysis_results['betweenness'].items(), 
                           key=lambda x: x[1], reverse=True)[:3]
        if len(top_sectors) >= 2:
            source_sector = top_sectors[0][0]
            target_sector = top_sectors[1][0]
    
    if source_sector in G and target_sector in G:
        try:
            shortest_path = nx.shortest_path(G, source_sector, target_sector, weight='weight')
            path_length = nx.shortest_path_length(G, source_sector, target_sector, weight='weight')
            
            print(f"   Shortest economic path from {source_sector} to {target_sector}:")
            print(f"   {' → '.join(shortest_path)}")
            print(f"   Total economic distance: {path_length:.2f}")
        except nx.NetworkXNoPath:
            print(f"   No direct economic path from {source_sector} to {target_sector}")