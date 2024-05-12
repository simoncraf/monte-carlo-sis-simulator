import networkx as nx
import matplotlib.pyplot as plt
from networkx import Graph

def create_graph(graph_type: str, **kwargs):
    """Generate a graph of a given type with the specified parameters. The function supports
    creating three types of graphs: Barabási-Albert, Erdős-Rényi, and Watts-Strogatz.
    
    Args:
        graph_type (str): Type of the graph to generate. Supported values are:
                          "barabasi_albert", "erdos_renyi", "watts_strogatz".
        **kwargs: Keyword arguments specific to each graph type:
                  - For "barabasi_albert": 'n' (number of nodes, default 500) and
                    'm' (number of edges to attach from a new node to existing nodes, default 2).
                  - For "erdos_renyi": 'n' (number of nodes, default 500) and
                    'p' (probability of edge creation between two nodes, default 0.1).
                  - For "watts_strogatz": 'n' (number of nodes, default 500),
                    'k' (each node is joined with k nearest neighbors in ring topology, default 4),
                    'p' (the probability of rewiring each edge, default 0.1).
                  
    Returns:
        tuple: A tuple containing:
               - The generated graph (Graph object).
               - A dictionary of the parameters used to create the graph.
    """
    match graph_type:
        case "barabasi_albert":
            graph = nx.barabasi_albert_graph(kwargs.get("n", 500), kwargs.get("m", 2))
        case "erdos_renyi":
            graph = nx.erdos_renyi_graph(kwargs.get("n", 500), kwargs.get("p", 0.1))
        case "watts_strogatz":
            graph = nx.watts_strogatz_graph(kwargs.get("n", 500),kwargs.get("k",4), kwargs.get("p", 0.1))
        case _:
            raise ValueError(f"Unknown graph type: {graph_type}")
        
    return graph, kwargs
        
def draw_graph(graph: Graph) -> None:
    """Draw the given graph.
    Args:
        graph (networkx.Graph): The graph to be visualized. This should be a NetworkX graph object.
    """
    nx.draw(graph, with_labels=True)
    plt.show()
