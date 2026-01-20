import networkx as nx
import os

def load_graph(nodes_path='hetionet-v1.0-nodes.tsv', edges_path='hetionet-v1.0-edges.sif'):
    """
    Loads the Hetionet graph from nodes and edges files.
    """
    if not os.path.exists(nodes_path):
        raise FileNotFoundError(f"Nodes file not found: {nodes_path}")
    if not os.path.exists(edges_path):
        raise FileNotFoundError(f"Edges file not found: {edges_path}")

    G = nx.DiGraph()

    # Load Nodes
    with open(nodes_path, 'r') as f:
        for l in f:
            if l.startswith('id'):
                continue
            parts = l.strip().split('\t')
            if len(parts) >= 3:
                id, name, kind = parts[0], parts[1], parts[2]
                if name not in G.nodes():
                    G.add_node(id, name=name, kind=kind)

    # Load Edges
    with open(edges_path, 'r') as f:
        for line in f:
            if line.startswith('source'):
                continue
            parts = line.strip().split('\t')
            if len(parts) >= 3:
                source, metaedge, target = parts[0], parts[1], parts[2]
                G.add_edge(source, target, type=metaedge)

    print(f"Graph loaded with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    return G
