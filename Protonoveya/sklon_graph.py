# sklon_graph.py — визуализация падежной структуры слова как семантического древа Логоса

import json
import networkx as nx
import matplotlib.pyplot as plt
from sklonos_logic import PadezhSklonLogic

class SklonGraphVisualizer:
    def __init__(self, word):
        self.word = word
        self.forms = PadezhSklonLogic(word).forms
        self.graph = nx.DiGraph()

    def build_graph(self):
        """
        Построение дерева склонения со связями падеж → форма → роль
        """
        self.graph.add_node(self.word, layer='core')

        for case, data in self.forms.items():
            case_node = f"{case.title()}"
            self.graph.add_node(case_node, layer='case')
            self.graph.add_node(data['form'], layer='form')
            self.graph.add_node(data['role'], layer='role')

            self.graph.add_edge(self.word, case_node)
            self.graph.add_edge(case_node, data['form'])
            self.graph.add_edge(data['form'], data['role'])

    def visualize(self):
        """
        Отображение графа с цветовой дифференциацией слоёв.
        """
        pos = nx.spring_layout(self.graph, seed=42)
        layers = nx.get_node_attributes(self.graph, 'layer')

        colors = {
            'core': 'gold',
            'case': 'skyblue',
            'form': 'lightgreen',
            'role': 'plum'
        }

        node_colors = [colors.get(layers.get(node, 'core'), 'gray') for node in self.graph.nodes()]

        plt.figure(figsize=(12, 8))
        nx.draw_networkx(self.graph, pos,
                         node_color=node_colors,
                         with_labels=True,
                         node_size=1800,
                         font_size=8,
                         font_family='DejaVu Sans')
        plt.title(f"Σ-FDL Graph: Склонение слова '{self.word}'")
        plt.axis('off')
        plt.tight_layout()
        plt.show()

# Пример запуска
if __name__ == "__main__":
    vis = SklonGraphVisualizer("Logos")
    vis.build_graph()
    vis.visualize()
