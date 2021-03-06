import random
import networkx as nx
from littleballoffur.sampler import Sampler

class RandomNodeNeighborSampler(Sampler):
    r"""An implementation of random node-neighbor sampling. The process uniformly
    samples  a fixed number of nodes first. Later it induces the neighboring nodes
    as the node set and the edges between all of the nodes. `"For details about the algorithm see this paper." <https://cs.stanford.edu/people/jure/pubs/sampling-kdd06.pdf>`_


    Args:
        number_of_nodes (int): Number of nodes. Default is 100.
        seed (int): Random seed. Default is 42.
    """
    def __init__(self, number_of_nodes=100, seed=42):
        self.number_of_nodes = number_of_nodes
        self.seed = seed
        self._set_seed()

    def _create_initial_node_set(self):
        """
        Choosing initial nodes.
        """
        nodes = [node for node in range(self._graph.number_of_nodes())]
        self._sampled_nodes = random.sample(nodes, self.number_of_nodes)
        neighbors = [neighbor for node in self._sampled_nodes for neighbor in self._graph.neighbors(node)]
        self._sampled_nodes = set(self._sampled_nodes + neighbors)

    def sample(self, graph):
        """
        Sampling nodes randomly.

        Arg types:
            * **graph** *(NetworkX graph)* - The graph to be sampled from.

        Return types:
            * **new_graph** *(NetworkX graph)* - The graph of sampled nodes.
        """
        self._check_graph(graph)
        self._check_number_of_nodes(graph)
        self._graph = graph
        self._create_initial_node_set()
        new_graph = self._graph.subgraph(self._sampled_nodes)
        return new_graph
