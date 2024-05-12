import networkx as nx
import matplotlib.pyplot as plt

def create_graph(graph_type: str, **kwargs):
    """Generate a graph of a given type with the given parameters."""
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
        
def draw_graph(graph):
    """Draw the given graph."""
    nx.draw(graph, with_labels=True)
    plt.show()
