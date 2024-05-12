import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
from loguru import logger

from networks import create_graph
from simulation import monte_carlo_sis
from plots import save_plot
from utils import store_results, load_results

GRAPH_TYPE = "watts_strogatz"
NUM_NODES = 500
NUM_STEPS = 1000  # Total number of steps per simulation
TRANSIENT = 900  # Number of steps in the transient period
NUM_REPEATS = 50  # Number of Monte Carlo repetitions
INITIAL_RHO = 0.2  # Initial fraction of infected nodes
BETAS = np.linspace(0, 1, 51)  # 51 values from 0 to 1
MUS = [0.1, 0.5, 0.9]  # Different recovery probabilities

def main():
    results = {mu: [] for mu in MUS}
    graph, params = create_graph(GRAPH_TYPE, n=NUM_NODES, k=5, p=0.5)

    for mu in tqdm(MUS, desc="Running simulations for different mu"):
        infection_values = []
        for beta in tqdm(BETAS, desc=f"Running betas for mu={mu}"):
            fraction_infected = monte_carlo_sis(graph, beta, mu, INITIAL_RHO, NUM_STEPS, NUM_REPEATS, TRANSIENT)
            mean_infections = np.mean(fraction_infected)
            logger.info(mean_infections)
            infection_values.append(mean_infections)
        logger.info(f"Infection Values: {infection_values}")
        results[mu] = infection_values
        logger.info(f"Results: {results}")
    
    store_results(results, GRAPH_TYPE, params)
    save_plot(GRAPH_TYPE, params, MUS, BETAS, results, output_dir="results")
    
if __name__ == "__main__":
    main()
