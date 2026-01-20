import networkx as nx
import matplotlib.pyplot as plt

def find_most_connected_diseases(G, top_n=10):
    disease_degrees = [(node, G.in_degree(node) + G.out_degree(node)) 
                       for node, data in G.nodes(data=True) if data.get('kind') == 'Disease']
    
    most_connected_diseases = sorted(disease_degrees, key=lambda x: x[1], reverse=True)
    return most_connected_diseases[:top_n]

def analyze_disease_symptom_connections(G):
    disease_symptom_nodes = [node for node, data in G.nodes(data=True) 
                             if data.get('kind') in ['Disease', 'Symptom']]
    subgraph = G.subgraph(disease_symptom_nodes)
    
    total_edges = subgraph.number_of_edges()
    total_nodes = len(disease_symptom_nodes)
    average_connections = total_edges / total_nodes if total_nodes else 0
    return average_connections, subgraph

def find_diseases_for_symptom(G, symptom_name):
    # Find symptom node first
    symptom_id = next((node for node, data in G.nodes(data=True) 
                       if data.get('name') == symptom_name and data.get('kind') == 'Symptom'), None)
    
    if not symptom_id:
        return []
    
    diseases = []
    predecessors = G.predecessors(symptom_id)
    for pred in predecessors:
        if G.nodes[pred].get('kind') == 'Disease':
            diseases.append(G.nodes[pred].get('name'))
    return diseases

def find_compounds_for_disease(G, disease_name):
    compounds = []
    disease_id = next((node for node, data in G.nodes(data=True) 
                       if data.get('name') == disease_name and data.get('kind') == 'Disease'), None)
    
    if disease_id:
        predecessors = G.predecessors(disease_id)
        for pred in predecessors:
            if G.nodes[pred].get('kind') == 'Compound':
                compounds.append(G.nodes[pred].get('name', 'Unknown'))
    return compounds

def count_side_effects(G, compound_names):
    counts = {}
    for compound_name in compound_names:
        compound_id = next((node for node, data in G.nodes(data=True) 
                            if data.get('name') == compound_name and data.get('kind') == 'Compound'), None)
        if compound_id:
            successors = G.successors(compound_id)
            count = sum(1 for succ in successors if G.nodes[succ].get('kind') == 'Side Effect')
            counts[compound_name] = count
        else:
            counts[compound_name] = 0
    return dict(sorted(counts.items(), key=lambda item: item[1]))
