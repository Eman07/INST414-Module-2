import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load data
file_path = '/Users/emmanuelephraim/Desktop/INST 414/Assignment 2/Crime_Data_from_2020_to_Present.csv' # Update with your file path
crime_data = pd.read_csv(file_path)

# Initialize an empty graph
G = nx.DiGraph()  # Using directed graph for in/out-degree analysis

# Create nodes and edges based on crimes within the same area (if DR_NO has only one crime per entry)
for _, group in crime_data.groupby('AREA NAME'):
    crimes = group['Crm Cd Desc'].dropna().unique()  # Unique crimes in the same area
    for crime1 in crimes:
        for crime2 in crimes:
            if crime1 != crime2:
                # Add nodes if they don't already exist
                if not G.has_node(crime1):
                    G.add_node(crime1)
                if not G.has_node(crime2):
                    G.add_node(crime2)
                # Add edge between co-occurring crimes
                G.add_edge(crime1, crime2)

# Step 3: Calculate Centrality Measures

# Degree Centrality
degree_centrality = nx.degree_centrality(G)
top_10_degree = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:10]
print("Top 10 Crimes by Degree Centrality:")
for crime in top_10_degree:
    print(f"- {crime}")

# In-Degree Centrality
in_degree_centrality = nx.in_degree_centrality(G)
top_10_in_degree = sorted(in_degree_centrality, key=in_degree_centrality.get, reverse=True)[:10]
print("\nTop 10 Crimes by In-Degree Centrality:")
for crime in top_10_in_degree:
    print(f"- {crime}")

# Out-Degree Centrality
out_degree_centrality = nx.out_degree_centrality(G)
top_10_out_degree = sorted(out_degree_centrality, key=out_degree_centrality.get, reverse=True)[:10]
print("\nTop 10 Crimes by Out-Degree Centrality:")
for crime in top_10_out_degree:
    print(f"- {crime}")

# Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(G)
top_10_betweenness = sorted(betweenness_centrality, key=betweenness_centrality.get, reverse=True)[:10]
print("\nTop 10 Crimes by Betweenness Centrality:")
for crime in top_10_betweenness:
    print(f"- {crime}")
# Step 4: Plot the Top 10 Crimes by Degree Centrality
top_10_subgraph = G.subgraph(top_10_degree)
node_size = [1000 * degree_centrality[node] for node in top_10_subgraph.nodes()]

plt.figure(figsize=(10, 8))
nx.draw(top_10_subgraph, with_labels=True, node_size=node_size, node_color='skyblue', font_size=10)
plt.title('Top 10 Crimes by Degree Centrality')
plt.show()

# Step 5: Dictionary Mapping Crimes to Degree Centrality
crime_to_degree = {crime: degree_centrality[crime] for crime in G.nodes()}
print(crime_to_degree)

# Step 6: Draw the Subgraph with Node Sizes Based on Degree Centrality
top_20_degree = sorted(degree_centrality, key=degree_centrality.get, reverse=True)[:20]
subgraph = G.subgraph(top_20_degree)
node_sizes = [1000 * degree_centrality[node] for node in subgraph.nodes()]

plt.figure(figsize=(12, 10))
nx.draw(subgraph, with_labels=True, node_size=node_sizes, node_color='lightgreen', font_size=9)
plt.title('Subgraph of Top 20 Crimes by Degree Centrality')
plt.show()




