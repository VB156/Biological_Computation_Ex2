import itertools
import networkx as nx
from collections import defaultdict


"""
------------------------------------------------------------------------------------------------
Function: read_graph

This function reads a graph from a .txt file in edge-list format.

Input: 
    string file_path - path to the file containing the graph

Output: 
    DiGraph Graph - graph read from the file in networkx format
------------------------------------------------------------------------------------------------
"""
def read_graph(file_path):

    # New directed graph Graph
    dir_graph = nx.DiGraph() 

    with open(file_path, 'r') as file:
        for line in file: 
            v_source, v_target = map(int, line.strip().split())
            # save edge read to Graph
            dir_graph.add_edge(v_source, v_target) 

    return dir_graph



"""
------------------------------------------------------------------------------------------------
Function: find_all_possible_motifs

This function creates all possible motifs of the given size.

Input: 
    int motif_size - size of the motifs (number of vertices)    

Output: 
    list motifs_list - all possible motifs of the given size  
------------------------------------------------------------------------------------------------
"""
def find_all_possible_motifs(motif_size):

    motifs_list = []
    dir_graph = nx.DiGraph()

    # Create a complete directed graph with motif_size number of vertices
    for i in range(1, motif_size+1):
        for j in range(1, motif_size+1):
            # Self-loops are not allowed
            if i != j:  
                dir_graph.add_edge(i, j)
    
    # Find all possible edge combinations
    max_edges = motif_size * (motif_size-1) 
    for num_edges in range(motif_size-1, max_edges + 1):
        for edges in itertools.combinations(dir_graph.edges(), num_edges):
            subgraph = nx.DiGraph()
            subgraph.add_edges_from(edges)
            if nx.is_weakly_connected(subgraph):
                # Check if motif is unique (not isomorphic to any existing one)
                is_unique = True
                for existing_motif in motifs_list:
                    if nx.is_isomorphic(subgraph, existing_motif):
                        is_unique = False
                        break
                #Add to list if unique
                if is_unique:
                    motifs_list.append(subgraph)
    
    return motifs_list



"""
------------------------------------------------------------------------------------------------
Function: find_all_subgraphs

This function creates all possible subgraphs of the given size.

Input: 
    DiGraph dir_graph - graph to create subgraphs from
    int size - size of the subgraphs (number of vertices)

Output: 
    list subgraphs - all possible subgraphs of the given size
------------------------------------------------------------------------------------------------
"""
def find_all_subgraphs(dir_graph, size):

    vertices_list = list(dir_graph.nodes())
    subgraphs_list = []
    
    # Generate all possible combinations of |size| vertices
    for vertex_set in itertools.combinations(vertices_list, size):
        subgraph = dir_graph.subgraph(vertex_set)
        if nx.is_weakly_connected(subgraph):
            subgraphs_list.append(subgraph)
    
    return subgraphs_list



"""
------------------------------------------------------------------------------------------------
Function: is_isomorphic

This function checks if two graphs are isomorphic.

Input: 
    DiGraph G1 - first graph
    DiGraph G2 - second graph

Output: 
    bool is_isomorphic - True if the graphs are isomorphic, else False
------------------------------------------------------------------------------------------------
"""
def is_isomorphic(G1, G2):
    return nx.is_isomorphic(G1, G2)



"""
------------------------------------------------------------------------------------------------
Function: count_motifs

This function counts how many times each motif appears in the subgraphs.

Input: 
    list subgraphs - list of subgraphs  
    list all_possible_motifs - list of all possible motifs

Output: 
    dict motif_counts - dictionary with motifs as keys and counts as values
------------------------------------------------------------------------------------------------
"""
def count_motifs(subgraphs, all_possible_motifs):

    # Dictionary to store motif counts
    motif_counts = {}
    processed_subgraphs = set()
    
    # Init. all possible motifs
    for motif in all_possible_motifs:
        motif_counts[motif] = 0
    
    # Count actual occurrences
    for i, subgraph in enumerate(subgraphs):
        # Skip if already found
        if i in processed_subgraphs:
            continue
        count = 1
        processed_subgraphs.add(i)
        
        # Check if isomorphic subgraphs
        for j, other_subgraph in enumerate(subgraphs[i+1:], i+1):
            # Skip if already found
            if j in processed_subgraphs:
                continue
            if is_isomorphic(subgraph, other_subgraph):
                count += 1
                processed_subgraphs.add(j)
        
        # Find which motif this subgraph matches
        for motif in all_possible_motifs:
            if is_isomorphic(subgraph, motif):
                motif_counts[motif] = count
                break
    
    return motif_counts



"""
------------------------------------------------------------------------------------------------
Function: print_formatted_output

This function creates and formats the output as wanted.

Input: 
    int motif_size - size of the motifs     
    dict motif_counts - dictionary with motifs as keys and counts as values

Output: 
    string output - formatted output
------------------------------------------------------------------------------------------------
"""
def print_formatted_output(motif_size, motif_counts):
    output = []
    output.append(f"n={motif_size}")
    
    # Count existing and non-existing motifs
    existing_count = sum(1 for count in motif_counts.values() if count > 0)
    non_existing_count = sum(1 for count in motif_counts.values() if count == 0)
    
    output.append(f"count={len(motif_counts)}")
    output.append(f"Count of existing motifs: {existing_count}")
    output.append(f"Count of non-existing motifs: {non_existing_count}")
    
    # Add motifs with count > 0
    motif_number = 1
    output.append("")
    output.append("--------Existing motifs--------")
    for motif, count in motif_counts.items():
        if count > 0:
            output.append(f"#{motif_number}")
            output.append(f"count={count}")
            for edge in motif.edges():
                output.append(f"{edge[0]} {edge[1]}")
            motif_number += 1
            output.append("")
            
    
    # Add motifs with count = 0
    output.append("--------Non-existing motifs--------")
    for motif, count in motif_counts.items():
        if count == 0:
            output.append(f"#{motif_number}")
            output.append(f"count={count}")
            for edge in motif.edges():
                output.append(f"{edge[0]} {edge[1]}")
            motif_number += 1   
            output.append("")
        
    
    return "\n".join(output)
    


    

def main():
    # Input from user
    motif_size = int(input("Enter n (size of the motifs): "))
    graph_file = input("Enter your graph file path: ")
    
    # Proccess graph from given file
    dir_graph = read_graph(graph_file)
    
    # Get all possible motifs of size n
    all_possible_motifs = find_all_possible_motifs(motif_size)
    
    # Get all subgraphs of size n
    subgraphs = find_all_subgraphs(dir_graph, motif_size)
    
    # Count motifs in subgraphs
    motif_counts = count_motifs(subgraphs, all_possible_motifs)
    
    # Print output
    output = print_formatted_output(motif_size, motif_counts)
    print(output)

if __name__ == "__main__":
    main()
