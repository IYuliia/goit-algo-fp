import uuid
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color 
        self.id = str(uuid.uuid4())  


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) 
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} 

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


class BinaryHeap:
    def __init__(self, heap_type="min"):
        self.heap = []
        self.heap_type = heap_type  

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, idx):
        parent_idx = (idx - 1) // 2
        if parent_idx >= 0:
            if (self.heap_type == "min" and self.heap[idx] < self.heap[parent_idx]) or \
               (self.heap_type == "max" and self.heap[idx] > self.heap[parent_idx]):
                self.heap[idx], self.heap[parent_idx] = self.heap[parent_idx], self.heap[idx]
                self._heapify_up(parent_idx)

    def build_heap(self, array):
        self.heap = array
        for i in range(len(self.heap) // 2, -1, -1):
            self._heapify_down(i)

    def _heapify_down(self, idx):
        left_child_idx = 2 * idx + 1
        right_child_idx = 2 * idx + 2
        smallest_largest = idx

        if left_child_idx < len(self.heap) and \
           ((self.heap_type == "min" and self.heap[left_child_idx] < self.heap[smallest_largest]) or
            (self.heap_type == "max" and self.heap[left_child_idx] > self.heap[smallest_largest])):
            smallest_largest = left_child_idx

        if right_child_idx < len(self.heap) and \
           ((self.heap_type == "min" and self.heap[right_child_idx] < self.heap[smallest_largest]) or
            (self.heap_type == "max" and self.heap[right_child_idx] > self.heap[smallest_largest])):
            smallest_largest = right_child_idx

        if smallest_largest != idx:
            self.heap[idx], self.heap[smallest_largest] = self.heap[smallest_largest], self.heap[idx]
            self._heapify_down(smallest_largest)

    def get_heap(self):
        return self.heap

    def get_root(self):
        return self.heap[0] if self.heap else None


binary_heap = BinaryHeap(heap_type="min")  

binary_heap.insert(10)
binary_heap.insert(20)
binary_heap.insert(5)
binary_heap.insert(30)
binary_heap.insert(15)


def create_heap_tree(heap):
    def create_tree(idx):
        if idx >= len(heap.get_heap()):
            return None
        node = Node(heap.get_heap()[idx])
        node.left = create_tree(2 * idx + 1)
        node.right = create_tree(2 * idx + 2)
        return node

    return create_tree(0)

heap_root = create_heap_tree(binary_heap)

draw_tree(heap_root)
