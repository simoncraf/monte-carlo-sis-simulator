import random
from networkx import Graph
import numpy as np
from loguru import logger

def monte_carlo_sis(graph: Graph, beta: float, mu: float, rho_initial: float, num_steps: int, num_repeats: int, transient: int) -> list[float]:
    """Simulate the SIS model using Monte Carlo averaging, ignoring the transient period.

    Args:
        graph (networkx.Graph): The network structure to simulate on.
        beta (float): Infection probability.
        mu (float): Recovery probability.
        rho_initial (float): Initial fraction of infected nodes.
        num_steps (int): Total number of steps per simulation.
        num_repeats (int): Number of Monte Carlo simulation repetitions.
        transient (int): Number of steps to skip during the transient period.

    Returns:
        np.array: Average fraction of infected nodes over time after transient period.
    """
    results = np.zeros(num_steps - transient)
    nodes = list(graph.nodes())

    for _ in range(num_repeats):
        infected = set(random.sample(nodes, max(1,int(rho_initial * len(nodes)))))
        susceptible = set(nodes) - infected
        fraction_infected = []

        for _ in range(num_steps):
            new_infected = set()
            new_susceptible = set()

            for node in infected:
                if random.random() < mu:
                    new_susceptible.add(node)
                else:
                    new_infected.add(node)

            for node in susceptible:
                for neighbor in graph.neighbors(node):
                    if neighbor in infected and random.random() < beta:
                        new_infected.add(node)
                        break
                else:
                    new_susceptible.add(node)

            infected = new_infected
            susceptible = new_susceptible

            fraction_infected.append(len(infected) / len(nodes))

        results += np.array(fraction_infected[transient:])
        
    if not num_repeats:
        logger.warning("No repetitions were run or all were zero.")
    elif not np.any(results):
        logger.warning(f"No infections recorded, check initial conditions and parameters. mu: {mu}, beta:{beta}")

    results /= max(1,num_repeats)
    return results
