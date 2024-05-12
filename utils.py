import pickle

def store_results(data, graph_type, params, filename=None):
    params_name = "_".join(f'{key}={value}' for key, value in params.items())
    filename = f"results/{graph_type}_{params_name}.pickle"
    with open(filename, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_results(graph_type, params, filename=None):
    params_name = "_".join(f'{key}={value}' for key, value in params.items())
    filename = f"results/{graph_type}_{params_name}.pickle"
    with open(filename, 'rb') as handle:
        return pickle.load(handle)
