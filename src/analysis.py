import networkx as nx

def compute_entity_counts(G):
    """
    Computes total number of entities for each unique kind.
    """
    n_entities = {}
    for node, data in G.nodes(data=True):
        kind = data.get('kind', 'Unknown')
        n_entities[kind] = n_entities.get(kind, 0) + 1
    return n_entities

def compute_edge_counts(G):
    """
    Computes total number of each unique edge type.
    """
    n_edgetypes = {}
    for u, v, data in G.edges(data=True):
        etype = data.get('type', 'Unknown')
        n_edgetypes[etype] = n_edgetypes.get(etype, 0) + 1
    return n_edgetypes

def compute_node_degrees(G, n_entities):
    """
    Computes average in-degree and out-degree for each type of node.
    """
    in_degrees = G.in_degree()
    out_degrees = G.out_degree()
    kind_degrees = {}

    for node in G.nodes():
        kind = G.nodes[node]['kind']
        if kind not in kind_degrees:
            kind_degrees[kind] = [0, 0]
        kind_degrees[kind][0] += in_degrees[node]
        kind_degrees[kind][1] += out_degrees[node]

    # Calculate averages
    avg_kind_degrees = {}
    for kind in kind_degrees:
        count = n_entities.get(kind, 1)
        avg_kind_degrees[kind] = (
            kind_degrees[kind][0] / count,
            kind_degrees[kind][1] / count
        )
    return avg_kind_degrees

def jaccard_similarity_directed(graph, node1, node2):
    """
    Computes Jaccard similarity between two nodes based on directed neighbors.
    """
    try:
        successors_node1 = set(graph.successors(node1))
        successors_node2 = set(graph.successors(node2))
        predecessors_node1 = set(graph.predecessors(node1))
        predecessors_node2 = set(graph.predecessors(node2))
        
        intersection_successors = successors_node1.intersection(successors_node2)
        union_successors = successors_node1.union(successors_node2)
        intersection_predecessors = predecessors_node1.intersection(predecessors_node2)
        union_predecessors = predecessors_node1.union(predecessors_node2)
        
        intersection = intersection_successors.union(intersection_predecessors)
        union = union_successors.union(union_predecessors)
        
        jaccard_sim = len(intersection) / len(union) if union else 0
        return jaccard_sim
    except nx.NetworkXError:
        return 0.0
