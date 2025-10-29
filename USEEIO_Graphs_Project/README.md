# USEEIO Graph Project — Economic and Environmental Interconnections

This educational project demonstrates how **graph theory** can represent real-world **economic relationships** between industries using the **USEEIO v2.0.1-411** dataset from the **U.S. Environmental Protection Agency (EPA)**.

## 🧠 Learning Objectives

Students will learn to:
- Convert economic matrices into graph structures
- Apply network analysis to identify key economic sectors
- Visualize complex inter-industry relationships
- Interpret centrality measures in economic contexts
- Understand input-output analysis through graph theory

## 📊 Dataset Background

**USEEIO (U.S. Environmentally-Extended Input-Output)** models track:
- **Economic flows** between 411 industrial sectors
- **Environmental impacts** (emissions, resource use)
- **Supply chain relationships** across the U.S. economy

The "U" matrix represents **inter-industry consumption**: how much each sector purchases from other sectors.

## ⚙️ Setup Instructions

### 1. Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt


# HOLA