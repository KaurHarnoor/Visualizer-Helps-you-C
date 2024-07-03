import tkinter as tk
from collections import deque

class GraphVisualizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Graph Traversal Visualization")
        
        self.instruction_label = tk.Label(self, text="Press 'B' for BFS and 'D' for DFS", font=("Arial", 14))
        self.instruction_label.pack(pady=10)
        
        self.canvas = tk.Canvas(self, width=800, height=600, bg="white")
        self.canvas.pack()
        
        self.nodes = {}
        self.edges = []
        self.node_positions = {}
        self.create_graph()
        self.draw_graph()
        self.bind("<Key>", self.on_key_press)

    def create_graph(self):
        # Example graph
        self.nodes = {i: [] for i in range(1, 7)}
        self.add_edge(1, 2)
        self.add_edge(1, 3)
        self.add_edge(2, 4)
        self.add_edge(3, 5)
        self.add_edge(4, 6)
        self.add_edge(5, 6)
        
        # Positions for drawing nodes (manually set for simplicity)
        self.node_positions = {
            1: (100, 100), 2: (200, 200), 3: (100, 300),
            4: (300, 200), 5: (100, 500), 6: (300, 400)
        }

    def add_edge(self, u, v):
        self.nodes[u].append(v)
        self.nodes[v].append(u)
        self.edges.append((u, v))

    def draw_graph(self):
        self.canvas.delete("all")
        for u, v in self.edges:
            x1, y1 = self.node_positions[u]
            x2, y2 = self.node_positions[v]
            self.canvas.create_line(x1, y1, x2, y2, fill="black")
        
        for node, (x, y) in self.node_positions.items():
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="lightblue")
            self.canvas.create_text(x, y, text=str(node), font=("Arial", 12))

    def on_key_press(self, event):
        print(f"Key pressed: {event.char}")
        if event.char == 'b':
            print("Starting BFS")
            self.bfs(1)
        elif event.char == 'd':
            print("Starting DFS")
            self.dfs(1)

    def bfs(self, start):
        queue = deque([start])
        visited = set()
        self.animate(queue, visited, is_bfs=True)

    def dfs(self, start):
        stack = [start]
        visited = set()
        self.animate(stack, visited, is_bfs=False)

    def animate(self, container, visited, is_bfs):
        if not container:
            return
        
        current = container.popleft() if is_bfs else container.pop()
        if current in visited:
            self.after(500, self.animate, container, visited, is_bfs)
            return

        visited.add(current)
        x, y = self.node_positions[current]
        self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="orange")
        self.canvas.create_text(x, y, text=str(current), font=("Arial", 12))

        for neighbor in self.nodes[current]:
            if neighbor not in visited:
                container.append(neighbor)

        self.after(500, self.animate, container, visited, is_bfs)

if __name__ == "__main__":
    app = GraphVisualizer()
    app.mainloop()
