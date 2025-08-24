# visualization_module.py :: Смыслограф FDL

import matplotlib.pyplot as plt
import networkx as nx

class FDLGraphEngine:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, node_id, label=None):
        self.graph.add_node(node_id, label=label or node_id)

    def add_edge(self, from_node, to_node, relation="→"):
        self.graph.add_edge(from_node, to_node, label=relation)

    def visualize(self, title="Смысловая структура", layout="spring"):
        pos = nx.spring_layout(self.graph) if layout == "spring" else nx.circular_layout(self.graph)
        labels = nx.get_node_attributes(self.graph, 'label')
        edge_labels = nx.get_edge_attributes(self.graph, 'label')

        plt.figure(figsize=(10, 7))
        nx.draw(self.graph, pos, labels=labels, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels, font_size=9)
        plt.title(title)
        plt.axis('off')
        plt.show()

    def reset(self):
        self.graph.clear()

    def load_from_structure(self, structure):
        self.reset()
        for node in structure.get("nodes", []):
            self.add_node(node["id"], label=node.get("label"))
        for edge in structure.get("edges", []):
            self.add_edge(edge["from"], edge["to"], relation=edge.get("label", "→"))


# Пример структуры
# structure = {
#     "nodes": [
#         {"id": "Thesis", "label": "Тезис"},
#         {"id": "Antithesis", "label": "Антитезис"},
#         {"id": "Synthesis", "label": "Синтез"}
#     ],
#     "edges": [
#         {"from": "Thesis", "to": "Synthesis", "label": "⊕"},
#         {"from": "Antithesis", "to": "Synthesis", "label": "⊖"}
#     ]
# }
