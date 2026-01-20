from src.data_loader import load_graph
from src.analysis import compute_entity_counts, compute_edge_counts, compute_node_degrees, jaccard_similarity_directed
from src.disease_case_study import (find_most_connected_diseases, analyze_disease_symptom_connections, 
                                    find_diseases_for_symptom, find_compounds_for_disease, count_side_effects)
import matplotlib.pyplot as plt

def main():
    print("Starting Network Biology Analysis...")
    try:
        G = load_graph()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please ensure 'hetionet-v1.0-nodes.tsv' and 'hetionet-v1.0-edges.sif' are in the current directory.")
        return

    # Task 2: Basic Analysis
    print("\n--- Task 2: Basic Metrics ---")
    n_entities = compute_entity_counts(G)
    print("Entities per kind:", n_entities)
    
    n_edges = compute_edge_counts(G)
    print("Edges per type (top 5):", list(n_edges.items())[:5])
    
    avg_degrees = compute_node_degrees(G, n_entities)
    print("Average degrees (in/out) per kind:", avg_degrees)

    # Task 2.1: Most Connected Diseases
    print("\n--- Task 2.1: Top Connected Diseases ---")
    top_diseases = find_most_connected_diseases(G)
    for disease, degree in top_diseases:
        name = G.nodes[disease]['name']
        print(f"Disease: {name}, Connections: {degree}")

    # Task 2.2: Disease-Symptom Analysis
    avg_conn, subgraph = analyze_disease_symptom_connections(G)
    print(f"\nAverage connections between Disease and Symptom: {avg_conn}")

    # Task 2.3 & 2.4: Jaccard Similarity
    # Note: IDs are hardcoded based on original script, might vary if data changes
    print("\n--- Task 2.3 & 2.4: Similarity Analysis ---")
    # Finding IDs for specific case study
    def get_id(name, kind):
        return next((n for n, d in G.nodes(data=True) if d.get('name') == name and d.get('kind') == kind), None)

    diabetes1 = get_id("type 1 diabetes mellitus", "Disease")
    diabetes2 = get_id("type 2 diabetes mellitus", "Disease")
    
    if diabetes1 and diabetes2:
        sim = jaccard_similarity_directed(subgraph, diabetes1, diabetes2)
        print(f"Jaccard Similarity (Diabetes T1 vs T2): {sim}")

    # Task 2.5: Case Study
    print("\n--- Task 2.5: Case Study (Constipation -> Lung Cancer) ---")
    symptom = "Constipation"
    possible_diseases = find_diseases_for_symptom(G, symptom)
    print(f"Diseases associated with {symptom}: {possible_diseases[:5]}...")

    target_disease = "lung cancer"
    print(f"\nAnalyzing treatments for {target_disease}...")
    compounds = find_compounds_for_disease(G, target_disease)
    
    if compounds:
        print(f"Found {len(compounds)} compounds. Checking side effects...")
        side_effect_counts = count_side_effects(G, compounds)
        print("Compounds sorted by least side effects (Top 5):")
        for c, count in list(side_effect_counts.items())[:5]:
            print(f"- {c}: {count} side effects")
    else:
        print("No compounds found.")

if __name__ == "__main__":
    main()
