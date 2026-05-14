import matplotlib.pyplot as plt
import networkx as nx



def plot_route(coords, route):

    G = nx.Graph()

    for i, (x, y) in enumerate(coords):
        G.add_node(i, pos=(x, y))

    for i in range(len(route) - 1):
        G.add_edge(route[i], route[i + 1])

    G.add_edge(route[-1], route[0])

    pos = nx.get_node_attributes(G, 'pos')

    fig, ax = plt.subplots(figsize=(8, 6))

    nx.draw(
        G,
        pos,
        with_labels=True,
        node_size=500,
        ax=ax
    )


    return fig



def plot_convergence(history):

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.plot(history)

    ax.set_title('Convergence Graph')
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Best Distance')

    return fig