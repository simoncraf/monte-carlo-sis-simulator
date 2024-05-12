import os
import matplotlib.pyplot as plt

def save_plot(graph_type, graph_params, mus, beta_values, results, output_dir="results"):
    """
    Save plots of the infection fraction (ρ) as a function of infection probability (β) for all µ values,
    including graph parameters in the legend.
    
    Args:
        graph_type (str): Type of the graph used in the simulation.
        graph_params (dict): Parameters used to generate the graph.
        mus (list): List of recovery probabilities µ.
        beta_values (list): The values of β (infection probabilities) used.
        results (dict): Dictionary of results, keys are µ values, values are lists of infected fractions.
        output_dir (str): Directory where the plot will be stored.
    """
    plt.figure(figsize=(8, 6))
    param_str = ', '.join(f'{key}={value}' for key, value in graph_params.items())
    param_title = "_".join(f'{key}={value}' for key, value in graph_params.items())
    for mu in mus:
        plt.plot(beta_values, results[mu], label=f'µ={mu}, {param_str}')
    
    plt.xlabel('Infection Probability (β)')
    plt.ylabel('Infected Fraction (ρ)')
    plt.title(f'SIS Model Stationary States on {graph_type} Network')
    plt.legend()
    plt.grid(True)
    plt.xlim(min(beta_values), max(beta_values))
    plt.ylim(0, 1)

    plot_filename = f"{graph_type}_{param_title}.png"
    plot_path = os.path.join(output_dir, plot_filename)
    os.makedirs(output_dir, exist_ok=True)
    plt.savefig(plot_path)
    plt.close()
