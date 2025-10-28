from data_loader import load_use_matrix, load_sector_names
from graph_builder import build_use_graph
from graph_analysis import analyze_use_graph, find_important_paths
from graph_visualization import visualize_use_graph, plot_economic_metrics
import os

def main():
    print("🎓 USEEIO Economic Graph Analysis - Educational Project")
    print("=" * 55)
    
    # File path - adjust as needed
    filepath = "data/USEEIO_v2_0_1_411.xlsx"
    
    # Check if file exists
    if not os.path.exists(filepath):
        print(f"❌ Error: File {filepath} not found!")
        print("Please download the dataset from:")
        print("https://github.com/USEPA/USEEIO/releases")
        print("And place it in the 'data/' folder")
        return
    
    # Load data
    print("\n📁 Loading USEEIO dataset...")
    df = load_use_matrix(filepath)
    
    if df is not None:
        # Try to load sector names for meaningful labels
        sector_names = load_sector_names(filepath)
        
        # Build graph with meaningful threshold to reduce noise
        print("\n🕸️  Building economic graph...")
        G, node_names = build_use_graph(df, sector_names, threshold=1.0)
        
        # Analyze graph
        analysis_results = analyze_use_graph(G)
        
        # Find important economic pathways
        find_important_paths(G, analysis_results)
        
        # Visualize graph
        print("\n🎨 Generating visualizations...")
        visualize_use_graph(G, analysis_results, layout='spring', max_nodes=40)
        
        # Plot additional economic metrics
        plot_economic_metrics(analysis_results)
        
        print("\n✅ Analysis complete! Students should now understand:")
        print("   • How economic matrices become graphs")
        print("   • How to identify key sectors using centrality measures")
        print("   • How to visualize complex economic relationships")
        
    else:
        print("❌ Failed to load data. Please check the file path and format.")

if __name__ == "__main__":
    main()