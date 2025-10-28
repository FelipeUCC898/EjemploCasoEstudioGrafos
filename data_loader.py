import pandas as pd
import numpy as np

def load_use_matrix(filepath):
    """
    Loads the 'U' (Use) matrix from the USEEIO Excel dataset.
    This matrix represents how industries consume goods from other industries.
    """
    try:
        # Read the U matrix sheet
        df = pd.read_excel(filepath, sheet_name="U", header=None)
        
        # Remove any completely empty rows and columns
        df = df.dropna(how='all').dropna(axis=1, how='all')
        
        print(f"✅ 'U' matrix loaded successfully from {filepath}")
        print(f"📊 Matrix shape: {df.shape}")
        print(f"📈 Total economic flow: {df.sum().sum():.2f} million USD")
        
        return df
        
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

def load_sector_names(filepath):
    """
    Loads sector names from the 'Sector' sheet to label nodes meaningfully.
    """
    try:
        sectors_df = pd.read_excel(filepath, sheet_name="Sector")
        sector_names = sectors_df['Name'].tolist()
        print(f"✅ Loaded {len(sector_names)} sector names")
        return sector_names
    except Exception as e:
        print(f"⚠️ Could not load sector names: {e}")
        return None